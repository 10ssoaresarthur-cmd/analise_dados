"""
Aula - Exercicios de Pandas DataFrame
Como usar:
1) Leia o enunciado de cada bloco.
2) Complete o codigo onde estiver RESOLUCAO.
3) Rode o arquivo e valide os resultados.

Requisito:
- Instalar pandas: pip install pandas

Regra da aula:
- Pense no DataFrame como uma planilha.
- Resolva um exercicio por vez.
"""
# -------------------------------------------------
# BLOCO 1: criar DataFrame e inspecionar estrutura
# -------------------------------------------------
import pandas as pd
dados_vendas = {
    "mes": ["Jan", "Jan", "Fev", "Fev", "Mar", "Mar"],
    "filial": ["Centro", "Norte", "Centro", "Norte", "Centro", "Norte"],
    "vendas": [12000, 9500, 13500, 10200, 14100, 11000],
    "clientes": [210, 180, 225, 190, 235, 205],
}

# Exercicio 1:
# a) Crie o DataFrame df_vendas usando dados_vendas
# b) Mostre as 5 primeiras linhas
# c) Mostre o formato (linhas, colunas)
# d) Mostre os tipos de dados das colunas

# RESOLUCAO: complete aqui



# -------------------------------------------------
# BLOCO 2: selecionar colunas e linhas
# -------------------------------------------------

# Exercicio 2:
# a) Mostre apenas as colunas "mes" e "vendas"
# b) Mostre somente a primeira linha
# c) Mostre as linhas de indice 2 ate 4

# RESOLUCAO: complete aqui


# -------------------------------------------------
# BLOCO 3: filtros com condicoes de negocio
# -------------------------------------------------

# Exercicio 3:
# a) Filtre vendas acima de 12000
# b) Filtre apenas a filial "Centro"
# c) Filtre vendas acima de 11000 na filial "Norte"

# RESOLUCAO: complete aqui


# -------------------------------------------------
# BLOCO 4: novas colunas e metricas
# -------------------------------------------------

# Exercicio 4:
# a) Crie a coluna "ticket_medio" = vendas / clientes
# b) Crie a coluna "meta_batida" com True para vendas >= 13000
# c) Mostre apenas "filial", "mes", "ticket_medio", "meta_batida"

# RESOLUCAO: complete aqui


# -------------------------------------------------
# BLOCO 5: agregacao com groupby
# -------------------------------------------------

# Exercicio 5:
# a) Calcule total de vendas por filial
# b) Calcule media de clientes por mes
# c) Descubra a filial com maior total de vendas

# RESOLUCAO: complete aqui


# -------------------------------------------------
# BLOCO 6: ordenacao e ranking
# -------------------------------------------------

# Exercicio 6:
# a) Ordene df_vendas por "vendas" em ordem decrescente
# b) Pegue os 3 maiores resultados de vendas
# c) Mostre um ranking com "filial", "mes", "vendas"

# RESOLUCAO: complete aqui


# -------------------------------------------------
# BLOCO 7: desafio final de analise
# -------------------------------------------------

# Exercicio 7 (desafio):
# 1) Gere um resumo por filial com:
#    - total_vendas
#    - media_ticket_medio
#    - total_clientes
# 2) Ordene o resumo por total_vendas (desc)
# 3) Exiba qual filial teve melhor desempenho geral

# RESOLUCAO: complete aqui






# ===========================================================
# PARTE 1 – Estrutura lista + dicionário
# ===========================================================

dados_list_dict = [{
    "Column A":[1, 2, 3],
    "Column B":[4, 5, 6],
    "Column C":[7, 8, 9]
}]


# -----------------------------------------------------------
# EXERCÍCIO 1 – Explorando a estrutura
# -----------------------------------------------------------

# 1. Qual é o tipo de dados_list_dict?
# 2. Qual é o tipo do primeiro elemento?
# 3. Como acessar a lista da "Column A"?
# 4. Como acessar o segundo elemento da "Column C"?

# RESPONDA AQUI:



# -----------------------------------------------------------
# EXERCÍCIO 2 – Convertendo para DataFrame
# -----------------------------------------------------------

# 1. Converta dados_list_dict[0] em um DataFrame chamado df1
# 2. Mostre:
#    - shape
#    - tipos das colunas
# 3. Calcule:
#    - soma de cada coluna
#    - média de cada coluna

# RESOLVA AQUI:



# -----------------------------------------------------------
# EXERCÍCIO 3 – Criando novas colunas
# -----------------------------------------------------------

# No df1:
# 1. Crie coluna "Total" = soma das colunas
# 2. Crie coluna "Media" = média por linha
# 3. Filtre linhas onde Total > 10

# RESOLVA AQUI:



# -----------------------------------------------------------
# EXERCÍCIO 4 – Conversões estruturais
# -----------------------------------------------------------

# 1. Converta df1 para:
#    - lista de dicionários [ {linha1}, {linha2}, {linha3} ]
#    - dicionário de listas { coluna1: [valores], coluna2: [valores] }
# Dica:
# orient="records":
#   Cada elemento representa uma linha.
#   Estrutura ideal para APIs e JSON.

# orient="list":
#   Cada chave representa uma coluna.
#   Estrutura colunar, útil para reconstruir DataFrame.


# RESOLVA AQUI:


# -----------------------------------------------------------
# EXERCÍCIO 5 – Trabalhando com lista
# -----------------------------------------------------------

# 1. Transforme a coluna "Column A" em uma lista chamada lista_a.
# 2. Multiplique cada elemento da lista por 10.
# 3. Crie uma nova coluna chamada "Column A x10" com essa nova lista.

# RESOLVA AQUI:



# ===========================================================
# BASE DE DADOS
# ===========================================================
import pandas as pd
dados = [
    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 5000},

    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 3000},

    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 4000},

    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 6000},

    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-03", "valor": 7000},
]


# ===========================================================
# PARTE 1 – EXPLORAÇÃO INICIAL
# ===========================================================

# Exercício 1
# 1. Qual o tipo da variável dados?
# 2. Quantos registros existem?
# 3. Quais são as chaves do primeiro dicionário?
# 4. Liste todos os países existentes (sem repetição).

# RESOLVA AQUI:



# ===========================================================
# PARTE 2 – CONVERSÃO PARA DATAFRAME
# ===========================================================

# Exercício 2
# 1. Converta dados para DataFrame chamado df
# 2. Mostre shape, tipos e primeiras linhas
# 3. Converta a coluna periodo para datetime

# RESOLVA AQUI:



# ===========================================================
# PARTE 3 – FILTROS E ORDENAÇÃO
# ===========================================================

# Exercício 3 – Filtros
# 1. Filtre apenas Brasil
# 2. Filtre apenas Produto A
# 3. Filtre valor > 4000
# 4. Combine Brasil + Produto A

# RESOLVA AQUI:


# Exercício 4 – Ordenação
# 1. Ordene por valor crescente
# 2. Ordene por valor decrescente
# 3. Ordene por periodo e depois por valor

# RESOLVA AQUI:



# ===========================================================
# PARTE 4 – AGREGAÇÕES
# ===========================================================

# Exercício 5 – GroupBy Simples
# 1. Total exportado por país
# 2. Total exportado por produto
# 3. Média por país
# 4. Quantidade de operações por país

# RESOLVA AQUI:


# Exercício 6 – GroupBy Múltiplo
# Agrupe por nome_pais e descricao
# Calcule soma, média e contagem

# Explique em comentário o que essa tabela representa

# RESOLVA AQUI:



# ===========================================================
# PARTE 5 – PIVOT TABLE
# ===========================================================

# Exercício 7 – Pivot por Produto
# Linhas: periodo
# Colunas: descricao
# Valores: soma de valor

# Responda:
# 1. Qual produto vendeu mais?
# 2. Qual mês teve maior valor total?
# 3. Existe mês sem venda?

# RESOLVA AQUI:


# Exercício 8 – Pivot por País
# Linhas: periodo
# Colunas: nome_pais
# Valores: soma de valor

# Explique o que podemos interpretar dessa tabela

# RESOLVA AQUI:



# ===========================================================
# PARTE 6 – FEATURE ENGINEERING
# ===========================================================

# Exercício 9
# 1. Extraia ano e mês da coluna periodo
# 2. Crie coluna valor_mil (valor / 1000)
# 3. Calcule crescimento percentual por produto mês a mês

# RESOLVA AQUI:



# ===========================================================
# PARTE 7 – QUALIDADE DE DADOS
# ===========================================================

# Exercício 10
# 1. Verifique valores nulos
# 2. Verifique valores negativos
# 3. Verifique duplicatas

# RESOLVA AQUI:
"""
Aula - Exercicios de Pandas DataFrame
Como usar:
1) Leia o enunciado de cada bloco.
2) Complete o codigo onde estiver RESOLUCAO.
3) Rode o arquivo e valide os resultados.

Requisito:
- Instalar pandas: pip install pandas

Regra da aula:
- Pense no DataFrame como uma planilha.
- Resolva um exercicio por vez.
"""

# -------------------------------------------------
# BLOCO 1: criar DataFrame e inspecionar estrutura
# -------------------------------------------------
import pandas as pd

dados_vendas = {
    "mes": ["Jan", "Jan", "Fev", "Fev", "Mar", "Mar"],
    "filial": ["Centro", "Norte", "Centro", "Norte", "Centro", "Norte"],
    "vendas": [12000, 9500, 13500, 10200, 14100, 11000],
    "clientes": [210, 180, 225, 190, 235, 205],
}

# Exercicio 1:
# a) Crie o DataFrame df_vendas usando dados_vendas
# b) Mostre as 5 primeiras linhas
# c) Mostre o formato (linhas, colunas)
# d) Mostre os tipos de dados das colunas

# RESOLUCAO: complete aqui
df_vendas = pd.DataFrame(dados_vendas)

print("\n=== BLOCO 1 ===")
print("5 primeiras linhas:")
print(df_vendas.head())

print("\nFormato (linhas, colunas):")
print(df_vendas.shape)

print("\nTipos de dados:")
print(df_vendas.dtypes)


# -------------------------------------------------
# BLOCO 2: selecionar colunas e linhas
# -------------------------------------------------

# Exercicio 2:
# a) Mostre apenas as colunas "mes" e "vendas"
# b) Mostre somente a primeira linha
# c) Mostre as linhas de indice 2 ate 4

# RESOLUCAO: complete aqui
print("\n=== BLOCO 2 ===")
print("Colunas mes e vendas:")
print(df_vendas[["mes", "vendas"]])

print("\nPrimeira linha:")
print(df_vendas.iloc[0])

print("\nLinhas de indice 2 ate 4:")
print(df_vendas.iloc[2:5])


# -------------------------------------------------
# BLOCO 3: filtros com condicoes de negocio
# -------------------------------------------------

# Exercicio 3:
# a) Filtre vendas acima de 12000
# b) Filtre apenas a filial "Centro"
# c) Filtre vendas acima de 11000 na filial "Norte"

# RESOLUCAO: complete aqui
print("\n=== BLOCO 3 ===")
print("Vendas acima de 12000:")
print(df_vendas[df_vendas["vendas"] > 12000])

print("\nApenas filial Centro:")
print(df_vendas[df_vendas["filial"] == "Centro"])

print("\nVendas acima de 11000 na filial Norte:")
print(df_vendas[(df_vendas["filial"] == "Norte") & (df_vendas["vendas"] > 11000)])


# -------------------------------------------------
# BLOCO 4: novas colunas e metricas
# -------------------------------------------------

# Exercicio 4:
# a) Crie a coluna "ticket_medio" = vendas / clientes
# b) Crie a coluna "meta_batida" com True para vendas >= 13000
# c) Mostre apenas "filial", "mes", "ticket_medio", "meta_batida"

# RESOLUCAO: complete aqui
df_vendas["ticket_medio"] = df_vendas["vendas"] / df_vendas["clientes"]
df_vendas["meta_batida"] = df_vendas["vendas"] >= 13000

print("\n=== BLOCO 4 ===")
print(df_vendas[["filial", "mes", "ticket_medio", "meta_batida"]])


# -------------------------------------------------
# BLOCO 5: agregacao com groupby
# -------------------------------------------------

# Exercicio 5:
# a) Calcule total de vendas por filial
# b) Calcule media de clientes por mes
# c) Descubra a filial com maior total de vendas

# RESOLUCAO: complete aqui
total_vendas_filial = df_vendas.groupby("filial")["vendas"].sum()
media_clientes_mes = df_vendas.groupby("mes")["clientes"].mean()
filial_maior_total = total_vendas_filial.idxmax()

print("\n=== BLOCO 5 ===")
print("Total de vendas por filial:")
print(total_vendas_filial)

print("\nMedia de clientes por mes:")
print(media_clientes_mes)

print("\nFilial com maior total de vendas:")
print(filial_maior_total)


# -------------------------------------------------
# BLOCO 6: ordenacao e ranking
# -------------------------------------------------

# Exercicio 6:
# a) Ordene df_vendas por "vendas" em ordem decrescente
# b) Pegue os 3 maiores resultados de vendas
# c) Mostre um ranking com "filial", "mes", "vendas"

# RESOLUCAO: complete aqui
df_ordenado = df_vendas.sort_values(by="vendas", ascending=False)
top3_vendas = df_ordenado.head(3)
ranking = df_ordenado[["filial", "mes", "vendas"]]

print("\n=== BLOCO 6 ===")
print("DataFrame ordenado por vendas (decrescente):")
print(df_ordenado)

print("\nTop 3 vendas:")
print(top3_vendas)

print("\nRanking:")
print(ranking)


# -------------------------------------------------
# BLOCO 7: desafio final de analise
# -------------------------------------------------

# Exercicio 7 (desafio):
# 1) Gere um resumo por filial com:
#    - total_vendas
#    - media_ticket_medio
#    - total_clientes
# 2) Ordene o resumo por total_vendas (desc)
# 3) Exiba qual filial teve melhor desempenho geral

# RESOLUCAO: complete aqui
resumo_filial = df_vendas.groupby("filial").agg(
    total_vendas=("vendas", "sum"),
    media_ticket_medio=("ticket_medio", "mean"),
    total_clientes=("clientes", "sum")
).sort_values(by="total_vendas", ascending=False)

melhor_filial = resumo_filial.index[0]

print("\n=== BLOCO 7 ===")
print("Resumo por filial:")
print(resumo_filial)

print("\nFilial com melhor desempenho geral:")
print(melhor_filial)





# ===========================================================
# PARTE 1 – Estrutura lista + dicionário
# ===========================================================

dados_list_dict = [{
    "Column A": [1, 2, 3],
    "Column B": [4, 5, 6],
    "Column C": [7, 8, 9]
}]


# -----------------------------------------------------------
# EXERCÍCIO 1 – Explorando a estrutura
# -----------------------------------------------------------

# 1. Qual é o tipo de dados_list_dict?
# 2. Qual é o tipo do primeiro elemento?
# 3. Como acessar a lista da "Column A"?
# 4. Como acessar o segundo elemento da "Column C"?

# RESPONDA AQUI:
print("\n=== PARTE 1 - EXERCICIO 1 ===")
print("Tipo de dados_list_dict:", type(dados_list_dict))
print("Tipo do primeiro elemento:", type(dados_list_dict[0]))
print('Lista da "Column A":', dados_list_dict[0]["Column A"])
print('Segundo elemento da "Column C":', dados_list_dict[0]["Column C"][1])


# -----------------------------------------------------------
# EXERCÍCIO 2 – Convertendo para DataFrame
# -----------------------------------------------------------

# 1. Converta dados_list_dict[0] em um DataFrame chamado df1
# 2. Mostre:
#    - shape
#    - tipos das colunas
# 3. Calcule:
#    - soma de cada coluna
#    - média de cada coluna

# RESOLVA AQUI:
df1 = pd.DataFrame(dados_list_dict[0])

print("\n=== PARTE 1 - EXERCICIO 2 ===")
print("df1:")
print(df1)

print("\nShape:")
print(df1.shape)

print("\nTipos das colunas:")
print(df1.dtypes)

print("\nSoma de cada coluna:")
print(df1.sum())

print("\nMedia de cada coluna:")
print(df1.mean())


# -----------------------------------------------------------
# EXERCÍCIO 3 – Criando novas colunas
# -----------------------------------------------------------

# No df1:
# 1. Crie coluna "Total" = soma das colunas
# 2. Crie coluna "Media" = média por linha
# 3. Filtre linhas onde Total > 10

# RESOLVA AQUI:
df1["Total"] = df1.sum(axis=1)
df1["Media"] = df1[["Column A", "Column B", "Column C"]].mean(axis=1)
linhas_total_maior_10 = df1[df1["Total"] > 10]

print("\n=== PARTE 1 - EXERCICIO 3 ===")
print("df1 com novas colunas:")
print(df1)

print("\nLinhas onde Total > 10:")
print(linhas_total_maior_10)


# -----------------------------------------------------------
# EXERCÍCIO 4 – Conversões estruturais
# -----------------------------------------------------------

# 1. Converta df1 para:
#    - lista de dicionários [ {linha1}, {linha2}, {linha3} ]
#    - dicionário de listas { coluna1: [valores], coluna2: [valores] }
# Dica:
# orient="records":
#   Cada elemento representa uma linha.
#   Estrutura ideal para APIs e JSON.

# orient="list":
#   Cada chave representa uma coluna.
#   Estrutura colunar, útil para reconstruir DataFrame.

# RESOLVA AQUI:
lista_de_dicionarios = df1.to_dict(orient="records")
dicionario_de_listas = df1.to_dict(orient="list")

print("\n=== PARTE 1 - EXERCICIO 4 ===")
print("Lista de dicionarios:")
print(lista_de_dicionarios)

print("\nDicionario de listas:")
print(dicionario_de_listas)


# -----------------------------------------------------------
# EXERCÍCIO 5 – Trabalhando com lista
# -----------------------------------------------------------

# 1. Transforme a coluna "Column A" em uma lista chamada lista_a.
# 2. Multiplique cada elemento da lista por 10.
# 3. Crie uma nova coluna chamada "Column A x10" com essa nova lista.

# RESOLVA AQUI:
lista_a = df1["Column A"].tolist()
lista_a_x10 = [x * 10 for x in lista_a]
df1["Column A x10"] = lista_a_x10

print("\n=== PARTE 1 - EXERCICIO 5 ===")
print("lista_a:")
print(lista_a)

print("\nlista_a_x10:")
print(lista_a_x10)

print("\ndf1 atualizado:")
print(df1)




# ===========================================================
# BASE DE DADOS
# ===========================================================
dados = [
    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 5000},

    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 3000},

    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 4000},

    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 6000},

    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-03", "valor": 7000},
]


# ===========================================================
# PARTE 1 – EXPLORAÇÃO INICIAL
# ===========================================================

# Exercício 1
# 1. Qual o tipo da variável dados?
# 2. Quantos registros existem?
# 3. Quais são as chaves do primeiro dicionário?
# 4. Liste todos os países existentes (sem repetição).

# RESOLVA AQUI:
print("\n=== BASE DE DADOS - PARTE 1 ===")
print("Tipo da variável dados:", type(dados))
print("Quantidade de registros:", len(dados))
print("Chaves do primeiro dicionário:", dados[0].keys())

paises_unicos = list({item["nome_pais"] for item in dados})
print("Países sem repetição:", paises_unicos)


# ===========================================================
# PARTE 2 – CONVERSÃO PARA DATAFRAME
# ===========================================================

# Exercício 2
# 1. Converta dados para DataFrame chamado df
# 2. Mostre shape, tipos e primeiras linhas
# 3. Converta a coluna periodo para datetime

# RESOLVA AQUI:
df = pd.DataFrame(dados)
df["periodo"] = pd.to_datetime(df["periodo"])

print("\n=== BASE DE DADOS - PARTE 2 ===")
print("Shape:")
print(df.shape)

print("\nTipos:")
print(df.dtypes)

print("\nPrimeiras linhas:")
print(df.head())


# ===========================================================
# PARTE 3 – FILTROS E ORDENAÇÃO
# ===========================================================

# Exercício 3 – Filtros
# 1. Filtre apenas Brasil
# 2. Filtre apenas Produto A
# 3. Filtre valor > 4000
# 4. Combine Brasil + Produto A

# RESOLVA AQUI:
df_brasil = df[df["nome_pais"] == "Brasil"]
df_produto_a = df[df["descricao"] == "Produto A"]
df_valor_maior_4000 = df[df["valor"] > 4000]
df_brasil_produto_a = df[(df["nome_pais"] == "Brasil") & (df["descricao"] == "Produto A")]

print("\n=== BASE DE DADOS - PARTE 3 / EXERCICIO 3 ===")
print("Apenas Brasil:")
print(df_brasil)

print("\nApenas Produto A:")
print(df_produto_a)

print("\nValor > 4000:")
print(df_valor_maior_4000)

print("\nBrasil + Produto A:")
print(df_brasil_produto_a)


# Exercício 4 – Ordenação
# 1. Ordene por valor crescente
# 2. Ordene por valor decrescente
# 3. Ordene por periodo e depois por valor

# RESOLVA AQUI:
valor_crescente = df.sort_values(by="valor", ascending=True)
valor_decrescente = df.sort_values(by="valor", ascending=False)
periodo_valor = df.sort_values(by=["periodo", "valor"], ascending=[True, True])

print("\n=== BASE DE DADOS - PARTE 3 / EXERCICIO 4 ===")
print("Ordenado por valor crescente:")
print(valor_crescente)

print("\nOrdenado por valor decrescente:")
print(valor_decrescente)

print("\nOrdenado por periodo e valor:")
print(periodo_valor)


# ===========================================================
# PARTE 4 – AGREGAÇÕES
# ===========================================================

# Exercício 5 – GroupBy Simples
# 1. Total exportado por país
# 2. Total exportado por produto
# 3. Média por país
# 4. Quantidade de operações por país

# RESOLVA AQUI:
total_por_pais = df.groupby("nome_pais")["valor"].sum()
total_por_produto = df.groupby("descricao")["valor"].sum()
media_por_pais = df.groupby("nome_pais")["valor"].mean()
qtd_operacoes_pais = df.groupby("nome_pais")["valor"].count()

print("\n=== BASE DE DADOS - PARTE 4 / EXERCICIO 5 ===")
print("Total exportado por país:")
print(total_por_pais)

print("\nTotal exportado por produto:")
print(total_por_produto)

print("\nMédia por país:")
print(media_por_pais)

print("\nQuantidade de operações por país:")
print(qtd_operacoes_pais)


# Exercício 6 – GroupBy Múltiplo
# Agrupe por nome_pais e descricao
# Calcule soma, média e contagem

# Explique em comentário o que essa tabela representa

# RESOLVA AQUI:
# Essa tabela representa o desempenho de cada produto dentro de cada país,
# mostrando o total exportado, a média dos valores e quantas operações ocorreram.
grupo_multiplo = df.groupby(["nome_pais", "descricao"])["valor"].agg(["sum", "mean", "count"])

print("\n=== BASE DE DADOS - PARTE 4 / EXERCICIO 6 ===")
print(grupo_multiplo)


# ===========================================================
# PARTE 5 – PIVOT TABLE
# ===========================================================

# Exercício 7 – Pivot por Produto
# Linhas: periodo
# Colunas: descricao
# Valores: soma de valor

# Responda:
# 1. Qual produto vendeu mais?
# 2. Qual mês teve maior valor total?
# 3. Existe mês sem venda?

# RESOLVA AQUI:
pivot_produto = df.pivot_table(
    index="periodo",
    columns="descricao",
    values="valor",
    aggfunc="sum",
    fill_value=0
)

produto_mais_vendeu = pivot_produto.sum().idxmax()
mes_maior_total = pivot_produto.sum(axis=1).idxmax()
existe_mes_sem_venda = (pivot_produto.sum(axis=1) == 0).any()

print("\n=== BASE DE DADOS - PARTE 5 / EXERCICIO 7 ===")
print("Pivot por produto:")
print(pivot_produto)

print("\nProduto que vendeu mais:")
print(produto_mais_vendeu)

print("\nMês com maior valor total:")
print(mes_maior_total)

print("\nExiste mês sem venda?")
print(existe_mes_sem_venda)


# Exercício 8 – Pivot por País
# Linhas: periodo
# Colunas: nome_pais
# Valores: soma de valor

# Explique o que podemos interpretar dessa tabela

# RESOLVA AQUI:
# Essa tabela permite comparar quanto cada país exportou em cada período,
# facilitando enxergar concentração de vendas e evolução mensal.
pivot_pais = df.pivot_table(
    index="periodo",
    columns="nome_pais",
    values="valor",
    aggfunc="sum",
    fill_value=0
)

print("\n=== BASE DE DADOS - PARTE 5 / EXERCICIO 8 ===")
print(pivot_pais)


# ===========================================================
# PARTE 6 – FEATURE ENGINEERING
# ===========================================================

# Exercício 9
# 1. Extraia ano e mês da coluna periodo
# 2. Crie coluna valor_mil (valor / 1000)
# 3. Calcule crescimento percentual por produto mês a mês

# RESOLVA AQUI:
df["ano"] = df["periodo"].dt.year
df["mes"] = df["periodo"].dt.month
df["valor_mil"] = df["valor"] / 1000

df = df.sort_values(by=["descricao", "periodo"])
df["crescimento_pct"] = df.groupby("descricao")["valor"].pct_change() * 100

print("\n=== BASE DE DADOS - PARTE 6 / EXERCICIO 9 ===")
print(df[["descricao", "periodo", "valor", "ano", "mes", "valor_mil", "crescimento_pct"]])


# ===========================================================
# PARTE 7 – QUALIDADE DE DADOS
# ===========================================================

# Exercício 10
# 1. Verifique valores nulos
# 2. Verifique valores negativos
# 3. Verifique duplicatas

# RESOLVA AQUI:
valores_nulos = df.isnull().sum()
valores_negativos = df[df["valor"] < 0]
duplicatas = df[df.duplicated()]

print("\n=== BASE DE DADOS - PARTE 7 / EXERCICIO 10 ===")
print("Valores nulos por coluna:")
print(valores_nulos)

print("\nValores negativos:")
print(valores_negativos)

print("\nDuplicatas:")
print(duplicatas)







