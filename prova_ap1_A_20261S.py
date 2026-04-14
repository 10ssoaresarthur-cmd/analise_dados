# O dataset NCR Ride Bookings contém registros de corridas urbanas realizadas em regiões da National Capital Region (NCR), que abrange Delhi, Gurgaon, Noida, Ghaziabad, Faridabad e áreas próximas.
# Utilize os arquivos : ncr_ride_bookings.csv para resolver as questoes.
# Principais informaçoes no dataset:
# Date → Data da corrida
# Time → Horário da corrida
# Booking ID → Identificador da corrida
# Booking Status → Status da corrida
# Customer ID → Identificador do cliente
# Vehicle Type → Tipo de veículo
# Pickup Location → Local de embarque
# Drop Location → Local de desembarque
# Booking Value → Valor da corrida
# Ride Distance → Distância percorrida
# Driver Ratings → Avaliação do motorista
# Customer Rating → Avaliação do cliente
# Payment Method → Método de pagamento
# Questões:
# (0,5) 1 - Quantas corridas estão com Status da Corrida como Completada ("Completed") no dataset? 
import pandas as pd 
df = pd.read_csv("ncr_ride_bookings.csv")  
filtro = (df['Booking Status'])




# (0,5) 2 - Qual a proporção em relação ao total de corridas?
totalcorridas = (df["Booking ID"] == 1).sum()
df.loc[totalcorridas], ["Booking ID"]


# (0,5) 3 - Calcule a média da Distância ("Ride Distance") percorrida por cada Tipo de veículo.
filtro = df["Ride Distance"].str.contains
# (0,5) 4 - Qual o Metodo de Pagamento ("Payment Method") mais utilizado pelas bicicletas ("Bike") ?


# (0,5) 5 - Qual o valor total arrecadado ("Booking Value") apenas das corridas Completed?


# (0,5) 6 - E qual o ticket médio ("Booking Value")dessas corridas Completed?



# (1,5) 7 - O IPEA disponibiliza uma API pública com diversas séries econômicas. 
# Para encontrar a série de interesse, é necessário primeiro acessar o endpoint de metadados.
# Acesse o endpoint de metadados: "http://www.ipeadata.gov.br/api/odata4/Metadados";
# Transforme em um DataFrame;
# Filtre para encontrar as séries da Fipe relacionadas a venda de imoveis (“vendas - Brasil”).
# Dica: 
# Utilize a coluna FNTSIGLA para encontrar a serie da Fipe;
# Utilize a coluna SERNOME para encontrar as vendas de imoveis no Brasil;

import pandas as pd
import requests
import yfinance as yf
# Período -> 5 anos

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTgwNzA5NjM3MiwiaWF0IjoxNzc1NTYwMzcyLCJqdGkiOiJlNDdiZjIxZTVjZGU0MDk2YjRlMTQ1MmUzN2M4ZDY0YiIsInVzZXJfaWQiOiI5OSJ9.eMgu6ySiRUTkoAjWJOGGXXh4u9BO1gtXeP4p9vtD2tc"
resp = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2021-04-01"},
)
dados = resp.json()
df = pd.DataFrame(dados)

df2 = df[["ticker", "roic", "earning_yield"]]
df2['rank_roic'] = df2['roic'].rank(ascending=False)
df2['rank_p_ey'] = df2['earning_yield'].rank(ascending=False)
df2['rank_final'] = (df2['rank_roic'] + df2['rank_p_ey']) / 2
carteira = df2.sort_values('rank_final', ascending=False)['ticker'][:20]

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTgwNzA5NjM3MiwiaWF0IjoxNzc1NTYwMzcyLCJqdGkiOiJlNDdiZjIxZTVjZGU0MDk2YjRlMTQ1MmUzN2M4ZDY0YiIsInVzZXJfaWQiOiI5OSJ9.eMgu6ySiRUTkoAjWJOGGXXh4u9BO1gtXeP4p9vtD2tc"
params = {"ticker": "BRKM5", "data_ini": "2021-04-01", "data_fim": "2026-03-23"}
resp = requests.get(
    f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
dados = resp.json()
df_preco = pd.DataFrame(dados)

#----------------------------------------------------------------------------------

data_ini = "2021-04-01"
data_fim = "2026-03-30"

carteira

retornos = []
for ticker in carteira:
    try:
        resp = requests.get(
            f"{base_url}/preco/corrigido",
            headers={"Authorization": f"Bearer {token}"},
            params={"ticker": ticker, "data_ini": data_ini, "data_fim": data_fim},
        )
        df_preco = pd.DataFrame(resp.json())
        if df_preco.empty or len(df_preco) < 2:
            print(f"  Sem dados: {ticker}")
            continue
        preco_ini = float(df_preco["fechamento"].iloc[0])
        preco_fim = float(df_preco["fechamento"].iloc[-1])
        retorno = (preco_fim / preco_ini - 1) * 100
        retornos.append({"ticker": ticker, "retorno_5Y_%": round(retorno, 2)})
    except Exception as e:
        print(f"  Erro {ticker}: {e}")

df_ret = pd.DataFrame(retornos).sort_values("retorno_5Y_%", ascending=False)

retornos

# Ibovespa no mesmo período

ibov = yf.download("^BVSP", start=data_ini, end=data_fim, auto_adjust=True, progress=False)
close = ibov["Close"].squeeze()  # resolve o MultiIndex
ret_ibov = (float(close.iloc[-1]) / float(close.iloc[0]) - 1) * 100

df_ret["peso"] = 0.05  # 20 ações × 5% = 100%
ret_carteira = (df_ret["retorno_5Y_%"] * df_ret["peso"]).sum()

print(df_ret.to_string(index=False))
print(f"\nRetorno médio carteira : {ret_carteira:.2f}%")
print(f"Retorno Ibovespa       : {ret_ibov:.2f}%")
print(f"Alpha                  : {ret_carteira - ret_ibov:.2f}%")
# (1,5) 8 -  Descubra qual é o código da série correspondente (coluna: SERCODIGO).
# CODIGO_ENCONTRADO=''
# Usando o código encontrado, acesse a API de valores: f"http://ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='{CODIGO_ENCONTRADO}')"
# Construa um DataFrame através da chave 'value' do retorno da api
# Selecione apenas as colunas datas (VALDATA) e os valores (VALVALOR).
# Exiba a Data e o Valor que teve o valor maximo de vendas.


# (1,5) 9 - Descubra quanto rendeu a VALE no ano de 2025
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# params = {"ticker": "VALE3", "data_ini": "2001-01-01", "data_fim": "2026-12-31"}
# response = requests.get(
#     f"{base_url}/preco/corrigido",
#     headers={"Authorization": f"Bearer {token}"},
#     params=params,
# )

# (1,5) 10 - Você tem acesso à API do Laboratório de Finanças, que fornece dados do Planilhão em formato JSON. 
# Selecione a empresa do setor de "tecnologia" que apresenta o maior ROE (Return on Equity) na data base 2024-04-01.
# Exiba APENAS AS COLUNAS "ticker", "setor" e o "roe"
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )


# (1,5) 11 - Faça a Magic Formula através dos indicadores Return on Capital (roc) e Earning Yield (ey) no dia 2024-04-01.
# Monte uma carteira de investimento com 10 ações baseado na estratégia Magic Formula.
# base_url = "https://laboratoriodefinancas.com/api/v2"
# token = "SEU_JWT"
# response = requests.get(
#     f"{base_url}/bolsa/planilhao",
#     headers={"Authorization": f"Bearer {token}"},
#     params={"data_base": "2026-04-01"},
# )
import pandas as pd
import requests
import yfinance as yf
# Período -> 5 anos

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTgwNzA5NjM3MiwiaWF0IjoxNzc1NTYwMzcyLCJqdGkiOiJlNDdiZjIxZTVjZGU0MDk2YjRlMTQ1MmUzN2M4ZDY0YiIsInVzZXJfaWQiOiI5OSJ9.eMgu6ySiRUTkoAjWJOGGXXh4u9BO1gtXeP4p9vtD2tc"
resp = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2021-04-01"},
)
dados = resp.json()
df = pd.DataFrame(dados)

df2 = df[["ticker", "roic", "earning_yield"]]
df2['rank_roic'] = df2['roic'].rank(ascending=False)
df2['rank_p_ey'] = df2['earning_yield'].rank(ascending=False)
df2['rank_final'] = (df2['rank_roic'] + df2['rank_p_ey']) / 2
carteira = df2.sort_values('rank_final', ascending=False)['ticker'][:20]

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTgwNzA5NjM3MiwiaWF0IjoxNzc1NTYwMzcyLCJqdGkiOiJlNDdiZjIxZTVjZGU0MDk2YjRlMTQ1MmUzN2M4ZDY0YiIsInVzZXJfaWQiOiI5OSJ9.eMgu6ySiRUTkoAjWJOGGXXh4u9BO1gtXeP4p9vtD2tc"
params = {"ticker": "BRKM5", "data_ini": "2021-04-01", "data_fim": "2026-03-23"}
resp = requests.get(
    f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
dados = resp.json()
df_preco = pd.DataFrame(dados)

#----------------------------------------------------------------------------------

data_ini = "2021-04-01"
data_fim = "2026-03-30"

carteira

retornos = []
for ticker in carteira:
    try:
        resp = requests.get(
            f"{base_url}/preco/corrigido",
            headers={"Authorization": f"Bearer {token}"},
            params={"ticker": ticker, "data_ini": data_ini, "data_fim": data_fim},
        )
        df_preco = pd.DataFrame(resp.json())
        if df_preco.empty or len(df_preco) < 2:
            print(f"  Sem dados: {ticker}")
            continue
        preco_ini = float(df_preco["fechamento"].iloc[0])
        preco_fim = float(df_preco["fechamento"].iloc[-1])
        retorno = (preco_fim / preco_ini - 1) * 100
        retornos.append({"ticker": ticker, "retorno_5Y_%": round(retorno, 2)})
    except Exception as e:
        print(f"  Erro {ticker}: {e}")

df_ret = pd.DataFrame(retornos).sort_values("retorno_5Y_%", ascending=False)

retornos

# Ibovespa no mesmo período

ibov = yf.download("^BVSP", start=data_ini, end=data_fim, auto_adjust=True, progress=False)
close = ibov["Close"].squeeze()  # resolve o MultiIndex
ret_ibov = (float(close.iloc[-1]) / float(close.iloc[0]) - 1) * 100

df_ret["peso"] = 0.05  # 20 ações × 5% = 100%
ret_carteira = (df_ret["retorno_5Y_%"] * df_ret["peso"]).sum()

print(df_ret.to_string(index=False))
print(f"\nRetorno médio carteira : {ret_carteira:.2f}%")
print(f"Retorno Ibovespa       : {ret_ibov:.2f}%")
print(f"Alpha                  : {ret_carteira - ret_ibov:.2f}%")

# (1,5) 12 - Quantos setores ("setor") tem essa carteira formada por 10 ações?
