import pandas as pd
import requests

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgwNTcwNzA4LCJpYXQiOjE3Nzc5Nzg3MDgsImp0aSI6IjNmNTBiZWM4OWVkZDQzMWI5NTljZWFkYmFkZTdiNjYyIiwidXNlcl9pZCI6IjExOCJ9.4m2iY0iB32ZKdO6_uZb-H1Cu9zwOXJcenbCHAv-qTFE"
params = {"ticker": "ibov", "data_ini": "2000-01-01", "data_fim": "2025-12-31"}
resp = requests.get(
    f"{base_url}/preco/diversos",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
data = resp.json()
ibov = pd.DataFrame(data)
print (ibov)

####

import pandas as pd
import requests

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgwNTcwNzA4LCJpYXQiOjE3Nzc5Nzg3MDgsImp0aSI6IjNmNTBiZWM4OWVkZDQzMWI5NTljZWFkYmFkZTdiNjYyIiwidXNlcl9pZCI6IjExOCJ9.4m2iY0iB32ZKdO6_uZb-H1Cu9zwOXJcenbCHAv-qTFE"
params = {"ticker": "usd_brl", "data_ini": "2000-01-01", "data_fim": "2025-12-31"}
resp = requests.get(
    f"{base_url}/preco/diversos",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
data = resp.json()
dolar = pd.DataFrame(data)
print(dolar)
    
ibov ["data"] = pd.to_datetime(ibov["data"])
dolar ["data"] = pd.to_datetime(dolar["data"])

ibov = ibov[["data", "fechamento"]]
dolar = dolar[["data", "fechamento"]]

ibov = ibov.rename(columns={"fechamento": "ibov"})
dolar = dolar.rename(columns={"fechamento": "dolar"})

ibov ["ibov"] = ibov["ibov"].astype(float)
dolar ["dolar"] = dolar["dolar"].astype(float)

df = pd.merge(ibov,dolar, on="data", how="inner")

df[[ "ibov" , "dolar"]].corr()

datas = pd.date_range("2000-01-01", "2025-12-31", freq="B")
df_base = pd.DataFrame({"data": datas})
df_base = pd.merge(df_base,ibov, on = "data", how = "left")
df_base = pd.merge(df_base,dolar, on = "data", how = "left")

df_base.isna().sum()
df_base.dropna()

####
df_base.isna().sum()
df_base.dropna()
df_base.ffill()
df_base.bfill()
#
df["ret_ibov"] = df["ibov"].pct_change()
df["ret_dolar"] = df["dolar"].pct_change()

#cprre 
import seaborn as sn
corr = df[["ret_ibov", "ret_dolar"]].corr()
sn.heatmap(corr, annot=True)
#Histograma
sn.histplot(df["ret_ibov"], kde=True)
#Boxplot 
sn.boxplot(df[])