
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