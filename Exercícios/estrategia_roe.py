import requests
import pandas as pd

url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2NTEzMTk1LCJpYXQiOjE3NzM5MjExOTUsImp0aSI6ImU2ZGFhM2U5ZGEzMzQzNzJiMzAwMTNmNzNkMTVkNzczIiwidXNlcl9pZCI6IjExMCJ9.aNw1HPkLXRviOgrZmrX7eCp6ZSBv0M-gLcQ6XT3nz2c"
resp = requests.get(
    f"{url}/bolsa/planilhao",
    headers = {"Authorization": f"Bearer {token}"},
    params = {'data_base': '2025-03-21',}
)
dados = resp.json()
df = pd.DataFrame(dados)
df2 = df[["ticker", "roe", "p_vp"]]
df2['rank_roe'] = df2['roe'].rank()
df2['rank_p_vp']= df2['p_vp'].rank(ascending=True)
df2["rank_final"] = (df2['rank_roe'] + df2['rank_p_vp'] / 2)
df2.sort_values("rank_final", ascending=False)


import requests

base_url = "https://laboratoriodefinancas.com/api/v2"
params = {"ticker": "PETR4", "data_ini": "2024-01-01", "data_fim": "2024-12-31"}
resp = requests.get(
    f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
print(resp.json())
dados=resp.json=()
df_preco = pd.DataFrame(dados)

filtro = df_p (variable) df_preco: dataframe
preco_final = df_preco.loc[filtro1, 'fechamento'].iloc[0]
preco_final = float(preco_final)

filtro2 = df_preco["data"]=="2025-03-21"
precos_inicial = = df_preco.loc[filtro2,' fechamento'].loc[0]
precos_inicial = float(precos_inicial)
preco_final/precos_inicial - 1