# ============================================================
# ATIVIDADE – CONSULTA DE DADOS VIA API
# OBJETIVO:
# - Consultar APIs públicas usando requests
# - Entender estrutura JSON
# - Transformar resposta em DataFrame
# - Trabalhar com parâmetros e TOKENS
# - Explorar dados externos
# REGRAS:
# - NÃO apagar os enunciados.
# - Organizar o código.
# - Comentar cada etapa importante.
# - Mostrar os resultados com print() ou DataFrame.
# ============================================================

import os
import requests
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# FUNÇÕES AUXILIARES (organização do código)
# ============================================================

def fetch_json(url: str, params: dict | None = None, headers: dict | None = None, timeout: int = 20):
    """
    Faz GET em uma URL e retorna o JSON (dict/list).
    Também imprime o status_code para conferência.
    """
    resp = requests.get(url, params=params, headers=headers, timeout=timeout)
    print(f"GET {resp.url}")
    print("Status code:", resp.status_code)
    resp.raise_for_status()  # se der erro HTTP, para aqui
    return resp.json()


def sidra_to_dataframe(sidra_json: list) -> pd.DataFrame:
    """
    A API SIDRA costuma retornar uma lista onde a linha 0 é o 'cabeçalho' (nomes das colunas),
    e as linhas seguintes são os dados.
    """
    if not isinstance(sidra_json, list) or len(sidra_json) < 2:
        return pd.DataFrame()

    # A primeira linha contém o "cabeçalho" (nomes humanizados)
    header_map = sidra_json[0]  # dict com chaves como "NC", "NN", "V", etc.
    df = pd.DataFrame(sidra_json[1:]).copy()  # dados

    # Renomeia colunas usando o cabeçalho (quando existir)
    rename_dict = {}
    for col_code in df.columns:
        if col_code in header_map:
            rename_dict[col_code] = header_map[col_code]
    df.rename(columns=rename_dict, inplace=True)
    return df


# ===========================================================
# PARTE 1 – INTRODUÇÃO
# ===========================================================
"""
O que é uma API?
API (Application Programming Interface) permite que um sistema
se comunique com outro.
Quando usamos requests.get(), estamos enviando uma requisição
HTTP para um servidor que retorna dados, geralmente em JSON.
Fluxo básico:
1. Definir URL
2. Enviar requisição
3. Verificar status_code
4. Converter para JSON
5. Transformar em DataFrame (quando necessário)
"""


# ===========================================================
# PARTE 2 – VIACEP (Consulta de CEP)
# ===========================================================
"""
Site: https://viacep.com.br/
Exemplo de consulta:
https://viacep.com.br/ws/01001000/json/

Exercícios:
1. Consulte um CEP da sua escolha.
2. Verifique o status da requisição.
3. Converta a resposta para JSON.
4. Transforme em DataFrame.
5. Mostre as principais informações.
"""
# RESOLVA AQUI:

print("\n" + "=" * 60)
print("PARTE 2 – VIACEP")

cep = "01001000"  # escolha livre (exemplo: Praça da Sé - SP)
url_viacep = f"https://viacep.com.br/ws/{cep}/json/"

viacep_json = fetch_json(url_viacep)

# Mostra o JSON (estrutura e principais chaves)
print("Tipo do JSON:", type(viacep_json))
print("Chaves retornadas:", list(viacep_json.keys()))
print("JSON completo:", viacep_json)

# Transforma em DataFrame (um registro)
df_viacep = pd.DataFrame([viacep_json])
print("\nDataFrame (ViaCEP):")
print(df_viacep)

# Principais informações
cols_principais = ["cep", "logradouro", "bairro", "localidade", "uf"]
print("\nPrincipais informações:")
print(df_viacep[cols_principais])


# ===========================================================
# PARTE 3 – BRASILAPI
# ===========================================================
"""
Documentação:
https://brasilapi.com.br/docs
Exercícios:
1. Consulte a lista de bancos.
2. Transforme o resultado em DataFrame.
3. Conte quantos bancos existem.
4. Filtre bancos cujo nome contenha "Brasil".
Explique:
O que você percebe sobre a estrutura do JSON retornado?
"""
# RESOLVA AQUI:

print("\n" + "=" * 60)
print("PARTE 3 – BRASILAPI (Bancos)")

url_bancos = "https://brasilapi.com.br/api/banks/v1"
bancos_json = fetch_json(url_bancos)

# Explicando estrutura (na prática):
print("Tipo do JSON:", type(bancos_json))
print("Quantidade de itens (lista):", len(bancos_json))
print("Exemplo de item (primeiro registro):", bancos_json[0])

# Transforma em DataFrame
df_bancos = pd.DataFrame(bancos_json)
print("\nDataFrame (Bancos) – primeiras linhas:")
print(df_bancos.head())

# Conta bancos
print("\nTotal de bancos:", df_bancos.shape[0])

# Filtra bancos com "Brasil" no nome
mask_brasil = df_bancos["name"].str.contains("Brasil", case=False, na=False)
df_bancos_brasil = df_bancos[mask_brasil].copy()
print("\nBancos cujo nome contém 'Brasil':")
print(df_bancos_brasil[["name", "code", "ispb"]].head(20))

# Explicação (texto no próprio código):
# - O JSON retornado é uma LISTA de OBJETOS (list[dict]).
# - Cada dict representa um banco, com chaves como: ispb, name, code, fullName.


# ===========================================================
# PARTE 4 – SERVIÇO DE DADOS IBGE
# ===========================================================
"""
Documentação:
https://servicodados.ibge.gov.br/api/docs/
Exercícios:
1. Consulte os estados brasileiros.
2. Transforme em DataFrame.
3. Mostre apenas:
   - nome
   - sigla
   - região
4. Pesquise como consultar dados de população.
Desafio:
Consultar a população total de um estado específico.
"""
# RESOLVA AQUI:

print("\n" + "=" * 60)
print("PARTE 4 – IBGE (Estados)")

# 1) Estados brasileiros (UFs)
url_ufs = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
ufs_json = fetch_json(url_ufs)

print("Tipo do JSON:", type(ufs_json))
print("Quantidade de estados:", len(ufs_json))
print("Exemplo (primeiro item):", ufs_json[0])

# 2) DataFrame (normalizando campo aninhado "regiao")
df_ufs = pd.json_normalize(ufs_json, sep="_")
print("\nDataFrame (UFs) – primeiras linhas:")
print(df_ufs.head())

# 3) Mostrar apenas nome, sigla e região
df_ufs_resumo = df_ufs[["nome", "sigla", "regiao_nome"]].copy()
df_ufs_resumo.rename(columns={"regiao_nome": "regiao"}, inplace=True)
print("\nUFs (nome, sigla, região):")
print(df_ufs_resumo)

# 4) População: usando a API SIDRA (IBGE) para tabelas estatísticas.
# A consulta segue o padrão:
# https://apisidra.ibge.gov.br/values/t/{tabela}/n{nivel}/{codigo}/v/{variavel}/p/{periodo}
#
# Desafio: população total de um estado específico.
# Exemplo: estimativas de população (tabela 6579, variável 9324).
# Vamos buscar o último valor (p/last) para o DF (código UF = 53).

print("\n" + "-" * 60)
print("DESAFIO – População (SIDRA)")

uf_escolhida = "DF"
codigo_uf = 53  # DF = 53 (códigos IBGE de UF)
tabela = 6579   # estimativas (EstimaPop)
variavel = 9324 # população estimada (total)

url_pop = f"https://apisidra.ibge.gov.br/values/t/{tabela}/n3/{codigo_uf}/v/{variavel}/p/last"
pop_json = fetch_json(url_pop)

# Converte para DataFrame e organiza
df_pop_raw = sidra_to_dataframe(pop_json)
print("\nDataFrame (SIDRA) – bruto (primeiras linhas):")
print(df_pop_raw.head())

# Normalmente existe uma coluna "Valor" (ou similar) com números em string
# Vamos tentar localizar a coluna de valor e a de período.
colunas = df_pop_raw.columns.tolist()
print("\nColunas disponíveis (SIDRA):", colunas)

# Estratégia robusta: procurar a coluna que contém "Valor" e a que contém "Ano" ou "Período"
col_valor = next((c for c in colunas if "Valor" in c), None)
col_periodo = next((c for c in colunas if "Ano" in c or "Período" in c), None)

if col_valor:
    df_pop_raw[col_valor] = pd.to_numeric(df_pop_raw[col_valor], errors="coerce")

print("\nPopulação (estado):")
if col_periodo and col_valor:
    print(df_pop_raw[[col_periodo, col_valor]].tail(10))
else:
    print(df_pop_raw.tail(10))


# ===========================================================
# PARTE 5 – IPEA DATA
# ===========================================================
"""
Documentação:
https://www.ipeadata.gov.br/api/
Exercícios:
1. Consulte os metadados de uma série.
2. Identifique:
   - nome da série
   - descrição
   - unidade
3. Consulte os valores históricos da série.
4. Transforme em DataFrame.
"""
# RESOLVA AQUI:

print("\n" + "=" * 60)
print("PARTE 5 – IPEA DATA (OData)")

# Série escolhida (exemplo comum em materiais): PRECOS12_IPCA12
# Você pode trocar por outra, desde que exista no Ipeadata.
serie_code = "PRECOS12_IPCA12"

base_ipea = "http://www.ipeadata.gov.br/api/odata4"

# 1) Metadados
url_meta = f"{base_ipea}/Metadados('{serie_code}')?$format=json"
meta_json = fetch_json(url_meta)

# O retorno pode ser um dict (entidade única). Vamos imprimir as chaves:
print("\nMetadados – tipo:", type(meta_json))
if isinstance(meta_json, dict):
    print("Metadados – chaves:", list(meta_json.keys()))
    # Alguns serviços OData retornam direto o objeto; outros podem retornar em "value".
    meta_obj = meta_json.get("value", meta_json)
else:
    meta_obj = meta_json

print("\nMetadados – objeto (resumo):")
print(meta_obj)

# 2) Identificar nome, descrição e unidade (tentando campos mais comuns)
# (Como pode variar, mostramos a estratégia: procurar por chaves relevantes.)
def pick_first_key(d: dict, candidates: list[str]):
    for k in candidates:
        if isinstance(d, dict) and k in d and d[k] not in (None, ""):
            return d[k]
    return None

nome_serie = pick_first_key(meta_obj, ["SERNOME", "SERNOMEBR", "SERTITULO", "SERNOMEEN"])
descricao = pick_first_key(meta_obj, ["SERCOMENTARIO", "SERCOMENTARIOBR", "SERDESCRICAO", "SERDESCRICAOBR"])
unidade = pick_first_key(meta_obj, ["UNINOME", "SERUNIDADE", "UNIDADE", "UNIUNIDADE"])

print("\nCampos principais (extraídos):")
print("Nome da série:", nome_serie)
print("Descrição:", descricao)
print("Unidade:", unidade)

# 3) Valores históricos
# Opção A (ValoresSerie): retorna somente a série em si
url_valores = f"{base_ipea}/ValoresSerie(SERCODIGO='{serie_code}')?$top=100000&$format=json"
valores_json = fetch_json(url_valores)

# 4) Transformar em DataFrame (OData costuma vir em "value")
valores_lista = valores_json.get("value", []) if isinstance(valores_json, dict) else valores_json
df_ipea = pd.DataFrame(valores_lista)

print("\nDataFrame (IPEA) – primeiras linhas:")
print(df_ipea.head())
print("\nQuantidade de registros históricos:", df_ipea.shape[0])

# Se existirem colunas de data/valor, vamos tentar converter:
for c in df_ipea.columns:
    if "DATA" in c.upper():
        df_ipea[c] = pd.to_datetime(df_ipea[c], errors="coerce")

for c in df_ipea.columns:
    if "VALOR" in c.upper():
        df_ipea[c] = pd.to_numeric(df_ipea[c], errors="coerce")

print("\nDataFrame (IPEA) – info:")
print(df_ipea.info())


# ===========================================================
# PARTE 6 – BANCO CENTRAL DO BRASIL (BCB)
# ===========================================================
"""
Dados Abertos BCB:
https://dadosabertos.bcb.gov.br/
Exemplo: Consulta PTAX
Parâmetros:
{
 "formato": "json",
 "dataInicial": "01/01/2024",
 "dataFinal": "31/12/2024"
}
Exercícios:
1. Consulte a cotação do dólar em 2024.
2. Transforme em DataFrame.
3. Calcule:
   - média
   - valor máximo
   - valor mínimo
4. Plote gráfico de linha.
"""
# RESOLVA AQUI:

print("\n" + "=" * 60)
print("PARTE 6 – BCB (PTAX / Cotação do Dólar por Período)")

# Importante: a API PTAX do BCB usa datas no formato MM-DD-YYYY em muitos exemplos práticos.
data_inicial = "01-01-2024"
data_final = "12-31-2024"

base_bcb = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
url_ptax = (
    base_bcb
    + "CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"
    + f"?@dataInicial='{data_inicial}'&@dataFinalCotacao='{data_final}'&$top=100000&$format=json"
)

ptax_json = fetch_json(url_ptax)

ptax_lista = ptax_json.get("value", [])
df_ptax = pd.DataFrame(ptax_lista)

print("\nDataFrame (PTAX) – primeiras linhas:")
print(df_ptax.head())
print("\nTotal de registros (PTAX):", df_ptax.shape[0])

# Converte tipos
if "dataHoraCotacao" in df_ptax.columns:
    df_ptax["dataHoraCotacao"] = pd.to_datetime(df_ptax["dataHoraCotacao"], errors="coerce")

for col in ["cotacaoCompra", "cotacaoVenda"]:
    if col in df_ptax.columns:
        df_ptax[col] = pd.to_numeric(df_ptax[col], errors="coerce")

# Em geral, há vários "tipos de boletim". Vamos filtrar "Fechamento" se existir:
if "tipoBoletim" in df_ptax.columns:
    df_ptax_fech = df_ptax[df_ptax["tipoBoletim"].astype(str).str.contains("Fechamento", case=False, na=False)].copy()
    if not df_ptax_fech.empty:
        df_ptax = df_ptax_fech

print("\nApós filtro (se aplicável) – total:", df_ptax.shape[0])

# 3) Estatísticas (vamos usar cotacaoVenda como referência)
if "cotacaoVenda" in df_ptax.columns:
    media = df_ptax["cotacaoVenda"].mean()
    maximo = df_ptax["cotacaoVenda"].max()
    minimo = df_ptax["cotacaoVenda"].min()

    print("\nEstatísticas (cotacaoVenda):")
    print("Média:", media)
    print("Máximo:", maximo)
    print("Mínimo:", minimo)

# 4) Gráfico de linha
if "dataHoraCotacao" in df_ptax.columns and "cotacaoVenda" in df_ptax.columns:
    df_plot = df_ptax.dropna(subset=["dataHoraCotacao", "cotacaoVenda"]).sort_values("dataHoraCotacao")
    plt.figure()
    plt.plot(df_plot["dataHoraCotacao"], df_plot["cotacaoVenda"])
    plt.title("PTAX – Cotação do Dólar (Venda) em 2024")
    plt.xlabel("Data")
    plt.ylabel("R$ (Venda)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# ===========================================================
# PARTE 7 – FOOTBALL-DATA.ORG
# ===========================================================
"""
Documentação:
https://www.football-data.org/documentation/quickstart
Observação:
Essa API exige API-KEY.
Exercícios:
1. Consulte as áreas (countries).
2. Filtre o Brasil (CountryCode = "BRA").
3. Consulte competições do Brasil.
4. Consulte os times da temporada 2025.
Explique:
O que são parâmetros de consulta?
"""
# RESOLVA AQUI:

print("\n" + "=" * 60)
print("PARTE 7 – FOOTBALL-DATA.ORG (com API-KEY)")

# BOA PRÁTICA: guardar token em variável de ambiente
# Ex.: no Windows (PowerShell): $env:FOOTBALL_DATA_TOKEN="SEU_TOKEN"
# Ex.: no Linux/Mac: export FOOTBALL_DATA_TOKEN="SEU_TOKEN"
football_token = os.getenv("FOOTBALL_DATA_TOKEN", "")

if not football_token:
    print("⚠️ Token não encontrado. Defina a variável de ambiente FOOTBALL_DATA_TOKEN para executar esta parte.")
else:
    base_fd = "https://api.football-data.org/v4"
    headers_fd = {"X-Auth-Token": football_token}

    # 1) Áreas (countries)
    areas_json = fetch_json(f"{base_fd}/areas", headers=headers_fd)
    areas_list = areas_json.get("areas", [])
    df_areas = pd.DataFrame(areas_list)
    print("\nÁreas – primeiras linhas:")
    print(df_areas.head())

    # 2) Filtrar Brasil (CountryCode = "BRA")
    # A chave pode variar (ex.: "countryCode" ou "code"). Vamos tentar as duas.
    if "countryCode" in df_areas.columns:
        df_bra = df_areas[df_areas["countryCode"] == "BRA"]
    elif "code" in df_areas.columns:
        df_bra = df_areas[df_areas["code"] == "BRA"]
    else:
        df_bra = pd.DataFrame()

    print("\nBrasil (filtro BRA):")
    print(df_bra)

    # 3) Competições do Brasil (vamos listar competições e filtrar por area.name == "Brazil")
    comps_json = fetch_json(f"{base_fd}/competitions", headers=headers_fd)
    comps_list = comps_json.get("competitions", [])
    df_comps = pd.json_normalize(comps_list, sep="_")
    print("\nCompetições – primeiras linhas:")
    print(df_comps[["id", "name", "code", "area_name"]].head())

    df_comps_br = df_comps[df_comps["area_name"].astype(str).str.contains("Brazil", case=False, na=False)]
    print("\nCompetições do Brasil (area_name contém 'Brazil'):")
    print(df_comps_br[["id", "name", "code", "area_name"]].head(20))

    # 4) Times da temporada 2025
    # Exemplo: Brasileirão Série A costuma usar o code "BSA" (quando disponível no seu plano).
    competition_code = "BSA"
    teams_json = fetch_json(f"{base_fd}/competitions/{competition_code}/teams", headers=headers_fd, params={"season": 2025})
    teams_list = teams_json.get("teams", [])
    df_teams = pd.json_normalize(teams_list, sep="_")
    print("\nTimes (temporada 2025) – primeiras linhas:")
    print(df_teams[["id", "name", "tla", "area_name"]].head(30))

    # Explique (no código):
    # Parâmetros de consulta são valores que você coloca na URL (query string),
    # como ?season=2025, para filtrar/ajustar o que a API retorna.


# ===========================================================
# PARTE 8 – RAPIDAPI (EXEMPLOS)
# ===========================================================
"""
Exemplos:
Tripadvisor – SearchLocation
querystring = {"query":"brasilia"}
NBA – Estatísticas de jogadores
querystring = {"game":"8133"}
Exercícios:
1. Escolha uma API do RapidAPI.
2. Faça uma consulta.
3. Transforme a resposta em DataFrame.
4. Descreva a estrutura do JSON retornado.
Desafio:
Identifique níveis aninhados no JSON.
"""
# RESOLVA AQUI:

print("\n" + "=" * 60)
print("PARTE 8 – RAPIDAPI (com API-KEY)")

rapidapi_key = os.getenv("RAPIDAPI_KEY", "")
if not rapidapi_key:
    print("⚠️ Defina a variável de ambiente RAPIDAPI_KEY para executar esta parte.")
else:
    # Exemplo escolhido: GeoDB Cities (bem comum no RapidAPI)
    # Endpoint: /v1/geo/cities com filtros
    url_geodb = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
    headers_rapid = {
        "X-RapidAPI-Key": rapidapi_key,
        "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com",
    }
    params = {"namePrefix": "Brasilia", "countryIds": "BR", "limit": 10}

    geodb_json = fetch_json(url_geodb, headers=headers_rapid, params=params)
    print("\nTipo do JSON:", type(geodb_json))
    print("Chaves de topo:", list(geodb_json.keys()))

    # Estrutura típica: dict com chave "data" contendo lista de cidades
    cidades = geodb_json.get("data", [])
    df_cidades = pd.DataFrame(cidades)
    print("\nDataFrame (cidades):")
    print(df_cidades.head())

    # Desafio (níveis aninhados):
    # Muitas APIs retornam JSON com níveis, por exemplo:
    # topo -> "data" (lista) -> cada item tem subcampos (às vezes dicts dentro).
    # Você identifica isso olhando type() e as chaves/valores de cada nível.


# ===========================================================
# PARTE 9 – EXPLORAÇÃO LIVRE
# ===========================================================
"""
Pesquise APIs públicas em:
https://github.com/public-apis/public-apis
https://apilayer.com/marketplace
https://app.balldontlie.io/
Exercícios:
1. Escolha uma API pública.
2. Consulte dados.
3. Transforme em DataFrame.
4. Faça uma pequena análise exploratória.
"""
# RESOLVA AQUI:

print("\n" + "=" * 60)
print("PARTE 9 – EXPLORAÇÃO LIVRE (API pública sem token)")

# Escolha: PokeAPI (pública, fácil para treino)
url_poke = "https://pokeapi.co/api/v2/pokemon"
poke_json = fetch_json(url_poke, params={"limit": 50, "offset": 0})

# Estrutura: dict com "results" (lista) e algumas infos
print("Chaves do topo:", list(poke_json.keys()))
lista_pokemon = poke_json.get("results", [])

df_poke = pd.DataFrame(lista_pokemon)
print("\nDataFrame (Pokémon) – primeiras linhas:")
print(df_poke.head())

# Pequena análise exploratória:
print("\nQuantidade de Pokémon retornados:", df_poke.shape[0])
df_poke["name_len"] = df_poke["name"].astype(str).str.len()
print("\nEstatísticas do tamanho do nome (name_len):")
print(df_poke["name_len"].describe())

print("\nTop 10 maiores nomes:")
print(df_poke.sort_values("name_len", ascending=False)[["name", "name_len"]].head(10))


# ===========================================================
# Revisão FINAL
# ===========================================================
"""
Responda:

1. O que é uma API?
2. O que é um endpoint?
3. O que são parâmetros?
4. O que é JSON?
5. O que é Headers?
6. O que é Token?
"""

print("\n" + "=" * 60)
print("REVISÃO FINAL – RESPOSTAS")

print("1) API: interface que permite que sistemas diferentes se comuniquem, normalmente via HTTP, trocando dados (muito comum em JSON).")
print("2) Endpoint: a rota/URL específica dentro de uma API que entrega um recurso (ex.: /api/banks/v1).")
print("3) Parâmetros: valores enviados na URL (query string) ou no corpo para filtrar/ordenar/definir a consulta (ex.: ?season=2025).")
print("4) JSON: formato de dados (texto) em estrutura de dicionários e listas (chave/valor), muito usado em APIs.")
print("5) Headers: 'metadados' da requisição/resposta HTTP (ex.: Authorization, Content-Type, X-Auth-Token).")
print("6) Token: credencial (chave) usada para autenticar/autorizar acesso em APIs (geralmente enviado em headers).")