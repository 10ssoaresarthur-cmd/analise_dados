"""

TCC - Determinantes do Endividamento das Famílias Brasileiras
Uma Análise Econométrica: Taxa de Juros, Renda e Crédito Rotativo (2012-2023)

Estrutura do projeto:
    1. Coleta de dados via API do BCB (SGS)
    2. Coleta da PEIC (CNC) - arquivo manual
    3. Tratamento e deflacionamento das séries
    4. Análise exploratória
    5. Testes de raiz unitária (ADF)
    6. Estimação do modelo OLS
    7. Diagnósticos do modelo
    8. Exportação dos resultados

Dependências: - Ainda Preciso Fazer 

    pip install pandas numpy requests matplotlib statsmodels scipy openpyxl
"""


# 0. IMPORTS

import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from statsmodels.tsa.stattools import adfuller
from statsmodels.regression.linear_model import OLS
from statsmodels.tools import add_constant
from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.diagnostic import het_breuschpagan
from scipy import stats
import warnings
warnings.filterwarnings('ignore')


# 1. COLETA DE DADOS — API BCB/SGS


# Padrão da API:
# https://api.bcb.gov.br/dados/serie/bcdata.sgs.{SERIE}/dados?formato=csv&dataInicial=DD/MM/AAAA&dataFinal=DD/MM/AAAA
# IMPORTANTE: A partir de 26/03/2025 o limite por consulta é de 10 anos.
# Por isso fazemos duas consultas (2012-2021 e 2022-2023) e concatenamos.

DATA_INICIO_1 = "01/01/2012"
DATA_FIM_1    = "31/12/2021"
DATA_INICIO_2 = "01/01/2022"
DATA_FIM_2    = "31/12/2023"

# Séries BCB utilizadas
SERIES = {
    # Variável dependente
    "endividamento_total":    29037,   # Endividamento famílias / renda anual (%)
    "endividamento_ex_imob":  29038,   # Idem, excluindo crédito imobiliário (%)
    "comprometimento_renda":  29265,   # Comprometimento de renda com serviço da dívida (%)
    # Variáveis independentes
    "juros_rotativo":         22024,   # Taxa de juros cartão rotativo PF (% a.m.)
    "selic":                  4390,    # Taxa Selic acumulada no mês (% a.m.)
    "ipca":                   433,     # IPCA variação mensal (%)
}

# Links diretos para download manual (caso a API falhe):
LINKS_MANUAIS = {
    "endividamento_total":
        "https://api.bcb.gov.br/dados/serie/bcdata.sgs.29037/dados?formato=csv&dataInicial=01/01/2012&dataFinal=31/12/2023",
    "endividamento_ex_imob":
        "https://api.bcb.gov.br/dados/serie/bcdata.sgs.29038/dados?formato=csv&dataInicial=01/01/2012&dataFinal=31/12/2023",
    "comprometimento_renda":
        "https://api.bcb.gov.br/dados/serie/bcdata.sgs.29265/dados?formato=csv&dataInicial=01/01/2012&dataFinal=31/12/2023",
    "juros_rotativo":
        "https://api.bcb.gov.br/dados/serie/bcdata.sgs.22024/dados?formato=csv&dataInicial=01/01/2012&dataFinal=31/12/2023",
    "selic":
        "https://api.bcb.gov.br/dados/serie/bcdata.sgs.4390/dados?formato=csv&dataInicial=01/01/2012&dataFinal=31/12/2023",
    "ipca":
        "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=csv&dataInicial=01/01/2012&dataFinal=31/12/2023",
}

def baixar_serie_bcb(codigo_serie, data_inicio, data_fim):
    """Baixa uma série do SGS/BCB e retorna um DataFrame com data e valor."""
    url = (
        f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados"
        f"?formato=csv&dataInicial={data_inicio}&dataFinal={data_fim}"
    )
    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        from io import StringIO
        df = pd.read_csv(StringIO(resp.text), sep=";", decimal=",")
        df.columns = ["data", "valor"]
        df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")
        df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
        return df.dropna()
    except Exception as e:
        print(f"  ERRO ao baixar série {codigo_serie}: {e}")
        print(f"  → Baixe manualmente em: {LINKS_MANUAIS.get(str(codigo_serie), 'N/A')}")
        return pd.DataFrame(columns=["data", "valor"])


def baixar_todas_series():
    """Baixa todas as séries do BCB em dois blocos (limite de 10 anos da API)."""
    dados = {}
    for nome, codigo in SERIES.items():
        print(f"Baixando: {nome} (série {codigo})...")
        df1 = baixar_serie_bcb(codigo, DATA_INICIO_1, DATA_FIM_1)
        df2 = baixar_serie_bcb(codigo, DATA_INICIO_2, DATA_FIM_2)
        df = pd.concat([df1, df2]).drop_duplicates("data").sort_values("data")
        df = df.set_index("data").rename(columns={"valor": nome})
        dados[nome] = df
        print(f"  OK — {len(df)} observações")
    return dados



# 2. DADOS MANUAIS — PEIC/CNC e PNAD Contínua - ( PRECISO BAIXAR 2 E 3)


# A PEIC e a PNAD Contínua não têm API; devem ser baixadas manualmente:
#
# PEIC (% famílias endividadas — mensal):
#   URL: https://pesquisascnc.com.br/pesquisa-peic/
#   → Clique em "Série Histórica" → baixe o Excel
#   → Salve como: dados/peic_serie_historica.xlsx
#   → Coluna esperada: data (MM/AAAA), perc_endividadas (%)
#
# PNAD Contínua (renda domiciliar per capita — trimestral):
#   URL: https://www.ibge.gov.br/estatisticas/sociais/trabalho/17270-pnad-continua.html
#   → Microdados → Visita → por ano
#   → Variável: VD5008 (rendimento domiciliar per capita)
#   → Salve a média trimestral como: dados/pnad_renda_trimestral.xlsx
#   → Colunas esperadas: ano, trimestre, renda_per_capita

def carregar_peic(caminho="dados/peic_serie_historica.xlsx"):
    """Carrega a PEIC do arquivo Excel baixado manualmente."""
    try:
        df = pd.read_excel(caminho)
        df.columns = [c.lower().strip() for c in df.columns]
        df["data"] = pd.to_datetime(df["data"], format="%m/%Y")
        df = df.set_index("data")[["perc_endividadas"]]
        print(f"PEIC carregada: {len(df)} observações")
        return df
    except FileNotFoundError:
        print("ATENÇÃO: arquivo PEIC não encontrado.")
        print(f"Baixe em https://pesquisascnc.com.br/pesquisa-peic/ e salve em '{caminho}'")
        return pd.DataFrame()


def carregar_pnad(caminho="dados/pnad_renda_trimestral.xlsx"):
    """Carrega a PNAD Contínua do arquivo Excel e converte para mensal."""
    try:
        df = pd.read_excel(caminho)
        df.columns = [c.lower().strip() for c in df.columns]
        # Cria data de referência (mês central do trimestre)
        trimestre_para_mes = {1: 2, 2: 5, 3: 8, 4: 11}
        df["mes"] = df["trimestre"].map(trimestre_para_mes)
        df["data"] = pd.to_datetime(
            df["ano"].astype(str) + "-" + df["mes"].astype(str) + "-01"
        )
        df = df.set_index("data")[["renda_per_capita"]].sort_index()
        # Interpolação linear para frequência mensal
        df_mensal = df.resample("MS").interpolate(method="linear")
        print(f"PNAD carregada e interpolada: {len(df_mensal)} observações mensais")
        return df_mensal
    except FileNotFoundError:
        print("ATENÇÃO: arquivo PNAD não encontrado.")
        print(f"Baixe em https://www.ibge.gov.br/estatisticas/sociais/trabalho/17270-pnad-continua.html")
        print(f"e salve em '{caminho}'")
        return pd.DataFrame()



# 3. TRATAMENTO DOS DADOS


def montar_painel(dados_bcb, df_peic, df_pnad):
    """Combina todas as séries em um único DataFrame mensal."""

    # Une todas as séries do BCB
    df = pd.concat([v for v in dados_bcb.values()], axis=1)
    df.index = pd.DatetimeIndex(df.index).to_period("M").to_timestamp()

    # Agrega por mês (para séries com dados diários)
    df = df.resample("MS").mean()

    # Adiciona PEIC e PNAD se disponíveis
    if not df_peic.empty:
        df_peic.index = pd.DatetimeIndex(df_peic.index).to_period("M").to_timestamp()
        df = df.join(df_peic, how="left")

    if not df_pnad.empty:
        df = df.join(df_pnad, how="left")

    # Filtro do período de análise
    df = df.loc["2012-01-01":"2023-12-31"]

    print(f"\nPainel montado: {len(df)} observações ({df.index[0].strftime('%m/%Y')} a {df.index[-1].strftime('%m/%Y')})")
    print(f"Variáveis: {list(df.columns)}")
    return df


def deflacionar(df, coluna_ipca="ipca", ano_base_dezembro="2023"):
    """
    Deflaciona todas as séries nominais pelo IPCA.
    Ano-base: dezembro de 2023 (índice = 100).
    """
    if coluna_ipca not in df.columns:
        print("Coluna IPCA não encontrada — séries não deflacionadas.")
        return df

    # Constrói índice de preços acumulado
    df = df.copy()
    df["indice_preco"] = (1 + df[coluna_ipca] / 100).cumprod()

    # Normaliza para dezembro de 2023 = 100
    base = df.loc["2023-12-01", "indice_preco"] if "2023-12-01" in df.index else df["indice_preco"].iloc[-1]
    df["indice_preco"] = df["indice_preco"] / base * 100

    # Deflaciona a renda (única série em valor nominal)
    if "renda_per_capita" in df.columns:
        df["renda_real"] = df["renda_per_capita"] / df["indice_preco"] * 100
        df["log_renda_real"] = np.log(df["renda_real"])

    return df



# 4. ANÁLISE EXPLORATÓRIA


def plotar_series(df, salvar=True):
    """Gráficos das principais séries para análise visual."""
    fig, axes = plt.subplots(3, 2, figsize=(14, 12))
    fig.suptitle("Séries Temporais — Endividamento das Famílias Brasileiras (2012–2023)",
                 fontsize=13, fontweight="bold", y=1.01)

    variaveis = [
        ("endividamento_ex_imob", "Endividamento (excl. imobiliário) % renda", "navy"),
        ("comprometimento_renda", "Comprometimento de renda (%)", "darkred"),
        ("juros_rotativo",        "Juros Rotativo Cartão (% a.m.)", "darkorange"),
        ("selic",                 "Taxa Selic (% a.m.)", "darkgreen"),
        ("log_renda_real",        "Log da Renda Real Per Capita", "purple"),
        ("ipca",                  "IPCA — variação mensal (%)", "gray"),
    ]

    for ax, (col, titulo, cor) in zip(axes.flatten(), variaveis):
        if col in df.columns:
            ax.plot(df.index, df[col], color=cor, linewidth=1.5)
            ax.set_title(titulo, fontsize=10)
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
            ax.xaxis.set_major_locator(mdates.YearLocator(2))
            ax.tick_params(axis="x", rotation=45, labelsize=8)
            ax.grid(alpha=0.3)
        else:
            ax.set_visible(False)

    plt.tight_layout()
    if salvar:
        plt.savefig("resultados/graficos_series.png", dpi=150, bbox_inches="tight")
        print("Gráfico salvo em: resultados/graficos_series.png")
    plt.show()


# 5. TESTES DE RAIZ UNITÁRIA (ADF)


def teste_adf(df, variaveis):
    """
    Aplica o teste ADF (Augmented Dickey-Fuller) para verificar estacionariedade.
    H0: série possui raiz unitária (não estacionária)
    Se p-value < 0.05: rejeita H0 → série estacionária
    """
    print("\n" + "="*60)
    print("TESTES DE RAIZ UNITÁRIA — Dickey-Fuller Aumentado (ADF)")
    print("="*60)
    resultados = []
    for var in variaveis:
        if var not in df.columns:
            continue
        serie = df[var].dropna()
        resultado = adfuller(serie, autolag="AIC")
        estatistica, pvalor = resultado[0], resultado[1]
        estacionaria = "✓ Estacionária" if pvalor < 0.05 else "✗ Raiz unitária"
        print(f"{var:<30} | ADF: {estatistica:7.3f} | p-valor: {pvalor:.4f} | {estacionaria}")
        resultados.append({"variavel": var, "adf": estatistica, "p_valor": pvalor,
                            "estacionaria": pvalor < 0.05})

    print("\nNOTA: Se a variável tiver raiz unitária, usar a 1ª diferença (diff).")
    return pd.DataFrame(resultados)



# 6. DEFINIÇÃO E ESTIMAÇÃO DO MODELO

#
# MODELO ECONOMÉTRICO:
#
#   ENDIV_t = β0 + β1·JUROS_t + β2·LOG_RENDA_t + β3·ROTATIVO_t + β4·SELIC_t + ε_t
#
# Onde:
#   ENDIV_t      = endividamento das famílias excluindo crédito imobiliário (% renda) no mês t
#   JUROS_t      = taxa de juros do cartão rotativo (% a.m.) no mês t
#   LOG_RENDA_t  = logaritmo natural da renda domiciliar real per capita no mês t
#   ROTATIVO_t   = volume de crédito rotativo concedido (R$ bi, se disponível) no mês t
#   SELIC_t      = taxa Selic acumulada no mês (% a.m.) no mês t
#   ε_t          = termo de erro
#
# Hipóteses esperadas:
#   β1 > 0  (juros mais altos → mais endividamento)
#   β2 < 0  (renda maior → menos endividamento relativo)
#   β3 > 0  (mais crédito rotativo → mais endividamento)
#   β4 > 0  (Selic mais alta → juros em cascata → mais endividamento)

def estimar_modelo(df):
    """Estima o modelo OLS e retorna os resultados."""

    variaveis_x = ["juros_rotativo", "log_renda_real", "selic"]
    variavel_y  = "endividamento_ex_imob"

    # Verifica disponibilidade das variáveis
    disponiveis = [v for v in variaveis_x if v in df.columns]
    if variavel_y not in df.columns:
        print(f"ERRO: variável dependente '{variavel_y}' não encontrada.")
        return None

    df_modelo = df[[variavel_y] + disponiveis].dropna()
    print(f"\nAmostra do modelo: {len(df_modelo)} observações")

    Y = df_modelo[variavel_y]
    X = add_constant(df_modelo[disponiveis])

    modelo = OLS(Y, X).fit(cov_type="HC3")  # Erros robustos a heterocedasticidade

    print("\n" + "="*60)
    print("RESULTADO DO MODELO OLS")
    print("="*60)
    print(modelo.summary())

    return modelo, df_modelo

# 7. DIAGNÓSTICOS DO MODELO


def diagnosticos(modelo, df_modelo, variavel_y="endividamento_ex_imob"):
    """Testes de diagnóstico: autocorrelação, heterocedasticidade e normalidade."""
    residuos = modelo.resid

    print("\n" + "="*60)
    print("DIAGNÓSTICOS DO MODELO")
    print("="*60)

    # Durbin-Watson (autocorrelação)
    dw = durbin_watson(residuos)
    print(f"Durbin-Watson: {dw:.4f}  (ideal entre 1.5 e 2.5)")

    # Breusch-Pagan (heterocedasticidade)
    bp_stat, bp_pval, _, _ = het_breuschpagan(residuos, modelo.model.exog)
    print(f"Breusch-Pagan: stat={bp_stat:.4f}, p-valor={bp_pval:.4f}",
          "→ Homocedasticidade" if bp_pval > 0.05 else "→ Heterocedasticidade (usar HC3)")

    # Jarque-Bera (normalidade dos resíduos)
    jb_stat, jb_pval = stats.jarque_bera(residuos)
    print(f"Jarque-Bera:   stat={jb_stat:.4f}, p-valor={jb_pval:.4f}",
          "→ Resíduos normais" if jb_pval > 0.05 else "→ Resíduos não normais")

    # Gráfico de resíduos
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].plot(df_modelo.index, residuos, color="navy", linewidth=1)
    axes[0].axhline(0, color="red", linestyle="--")
    axes[0].set_title("Resíduos ao longo do tempo")
    axes[0].grid(alpha=0.3)

    axes[1].hist(residuos, bins=20, color="navy", edgecolor="white", alpha=0.8)
    axes[1].set_title("Distribuição dos resíduos")
    axes[1].grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig("resultados/diagnosticos_residuos.png", dpi=150, bbox_inches="tight")
    print("Gráfico de resíduos salvo em: resultados/diagnosticos_residuos.png")
    plt.show()



# 8. EXPORTAÇÃO DOS RESULTADOS


def exportar_resultados(df, modelo):
    """Salva os dados tratados e os resultados do modelo em Excel."""
    import os
    os.makedirs("resultados", exist_ok=True)

    # Dados tratados
    df.to_excel("resultados/dados_tratados.xlsx")
    print("Dados exportados: resultados/dados_tratados.xlsx")

    # Coeficientes do modelo
    coef = pd.DataFrame({
        "coeficiente": modelo.params,
        "erro_padrao": modelo.bse,
        "t_stat": modelo.tvalues,
        "p_valor": modelo.pvalues,
        "ic_lower": modelo.conf_int()[0],
        "ic_upper": modelo.conf_int()[1],
    })
    coef.to_excel("resultados/coeficientes_modelo.xlsx")
    print("Coeficientes exportados: resultados/coeficientes_modelo.xlsx")



# 9. EXECUÇÃO PRINCIPAL


if __name__ == "__main__":
    import os
    os.makedirs("dados", exist_ok=True)
    os.makedirs("resultados", exist_ok=True)

    print("=" * 60)
    print("TCC — Endividamento das Famílias Brasileiras (2012–2023)")
    print("=" * 60)

    # 1. Coleta
    print("\n[1/6] Coletando dados do BCB...")
    dados_bcb = baixar_todas_series()

    print("\n[2/6] Carregando PEIC e PNAD (arquivos manuais)...")
    df_peic = carregar_peic()
    df_pnad = carregar_pnad()

    # 2. Tratamento
    print("\n[3/6] Montando painel e deflacionando...")
    df = montar_painel(dados_bcb, df_peic, df_pnad)
    df = deflacionar(df)

    # 3. Análise exploratória
    print("\n[4/6] Gerando gráficos exploratórios...")
    plotar_series(df)

    # 4. Testes ADF
    print("\n[5/6] Testes de estacionariedade...")
    variaveis_teste = ["endividamento_ex_imob", "comprometimento_renda",
                       "juros_rotativo", "selic", "log_renda_real", "ipca"]
    df_adf = teste_adf(df, variaveis_teste)

    # 5. Modelo
    print("\n[6/6] Estimando modelo OLS...")
    resultado = estimar_modelo(df)
    if resultado:
        modelo, df_modelo = resultado
        diagnosticos(modelo, df_modelo)
        exportar_resultados(df, modelo)

    print("\n✓ Concluído! Verifique a pasta 'resultados/'")