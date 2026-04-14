import pandas as pd #importar o pandas 
df = pd.read_csv("nome.csv") #trazer a pasta
df = pd.read_excel(".nome.xlsa")
filtro = (df[df["idade"]]>10) & (df["nome"].str.contains(a) )
#filtro duplo 
#case false - pra ignorar o maiusculo do minuscolo 
filtro = df["nome"].str.contains("pedro", case = False)

#rankear empresas escolhemos as empresas e filtramos 
df["roic"] .rank(ascending=false) #maior pro metro "false"
df.sort_values(["roic"], ascending= False) #aqui só ordena e dá uma nota
 #criar nova coluna 
 df["nova_col"] = 0 
#se for pra multiplicar a gente troca o 0 por multiplicação 
 #calcular min, max e méd 
 df["nov.col"]


import requests 
url = 
requests. get (url)
#gravamos em um
response = requests.get(ulr)
#status de retorno dele 
responde.status_code() 
#chama api vem no json, o status 200 é que foi um sucesso - gravamos ele em dados
dados = response.json


#exemplo prático api 

import requests 
import pandas as pd 
url= 
response requests. get(url) 


#grupby 