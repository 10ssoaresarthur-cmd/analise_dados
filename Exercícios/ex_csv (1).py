# LISTA DE EXERCÍCIOS – ANÁLISE DE DADOS COM PANDAS Dataset: Ranking
# Mundial de Universidades (notas.csv)

# ============================================================
# EXPLORAÇÃO INICIAL (EDA BÁSICA)
# ============================================================

# Exercício 1 – Conhecendo o Dataset 
# 1. Quantas linhas e colunas existem?
# 2. Quais são os tipos de dados? 
# 3. Existe coluna com valores ausentes?
# 4. Qual é o período de anos disponível? 
# 5. Quantos países diferentes
# existem?

# Exercício 2 – Estatísticas Gerais 
# 1. Média do score 
# 2. Maior score 
# 3.Menor score 
# 4. Média do score por ano 
# 5. Desvio padrão do score

# ============================================================
# FILTROS E SELEÇÕES
# ============================================================

# Exercício 3 – Top Universidades 
# 1. Mostre as 10 melhores universidades do mundo (menor world_rank) 
# 2. Mostre as 5 melhores universidades do Brasil (se existirem) 
# 3. Mostre universidades com score maior que 90 
# 4. Mostre universidades dos EUA com score maior que 80

# Exercício 4 – Seleção Avançada 
# 1. Mostre apenas as colunas: institution,
# country e score 
# 2. Mostre universidades entre rank 50 e 100 
# 3. Mostre universidades cujo país é “United Kingdom”

# ============================================================ PARTE 3 –
# MISSING VALUES
# ============================================================

# Exercício 5 – Valores Ausentes 
# 1. Quantos valores nulos existem na coluna broad_impact? 
# 2. Qual percentual do dataset é nulo? 
# 3. Remova linhas com broad_impact nulo 
# 4. Preencha valores nulos com a média 
# 5. Compare a média antes e depois do preenchimento

# ============================================================ PARTE 4 –
# GROUPBY (ANÁLISE POR PAÍS E ANO)
# ============================================================

# Exercício 6 – Análise por País 
# 1. Média do score por país 
# 2. País com maior média de score 
# 3. Quantidade de universidades por país 
# 4. Top 10 países com mais universidades

# Exercício 7 – Análise por Ano 
# 1. Média do score por ano 
# 2. Qual ano teve maior média? 
# 3. Faça um gráfico da evolução do score médio ao longo do tempo

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("notas.csv")

# ============================================================
# EXERCÍCIO 1 – Conhecendo o Dataset
# ============================================================
print("1) Linhas e colunas:", df.shape)
print("\n2) Tipos de dados:")
print(df.dtypes)

print("\n3) Valores ausentes por coluna:")
print(df.isnull().sum())

print("\n4) Período de anos:")
print(df["year"].min(), "até", df["year"].max())

print("\n5) Quantidade de países diferentes:")
print(df["country"].nunique())

# ============================================================
# EXERCÍCIO 2 – Estatísticas Gerais
# ============================================================
print("\nMédia do score:", df["score"].mean())
print("Maior score:", df["score"].max())
print("Menor score:", df["score"].min())

print("\nMédia do score por ano:")
print(df.groupby("year")["score"].mean())

print("\nDesvio padrão do score:")
print(df["score"].std())

# ============================================================
# EXERCÍCIO 3 – Top Universidades
# ============================================================
print("\n10 melhores universidades do mundo:")
print(df.nsmallest(10, "world_rank")[["world_rank", "institution", "country", "score", "year"]])

print("\n5 melhores universidades do Brasil:")
print(
    df[df["country"] == "Brazil"]
    .nsmallest(5, "world_rank")[["world_rank", "institution", "country", "score", "year"]]
)

print("\nUniversidades com score > 90:")
print(df[df["score"] > 90][["world_rank", "institution", "country", "score", "year"]])

print("\nUniversidades dos EUA com score > 80:")
print(
    df[(df["country"] == "USA") & (df["score"] > 80)]
    [["world_rank", "institution", "country", "score", "year"]]
)

# ============================================================
# EXERCÍCIO 4 – Seleção Avançada
# ============================================================
print("\nApenas institution, country e score:")
print(df[["institution", "country", "score"]])

print("\nUniversidades entre rank 50 e 100:")
print(df[df["world_rank"].between(50, 100)])

print("\nUniversidades do United Kingdom:")
print(df[df["country"] == "United Kingdom"])

# ============================================================
# EXERCÍCIO 5 – Valores Ausentes
# ============================================================
print("\nNulos em broad_impact:")
print(df["broad_impact"].isnull().sum())

print("\nPercentual nulo em broad_impact:")
print(df["broad_impact"].isnull().mean() * 100)

media_antes = df["broad_impact"].mean()

df_sem_nulos = df.dropna(subset=["broad_impact"])
print("\nDataset sem nulos em broad_impact:")
print(df_sem_nulos.shape)

df_preenchido = df.copy()
df_preenchido["broad_impact"] = df_preenchido["broad_impact"].fillna(media_antes)

media_depois = df_preenchido["broad_impact"].mean()

print("\nMédia antes:", media_antes)
print("Média depois:", media_depois)

# ============================================================
# EXERCÍCIO 6 – Análise por País
# ============================================================
print("\nMédia do score por país:")
print(df.groupby("country")["score"].mean())

print("\nPaís com maior média de score:")
print(df.groupby("country")["score"].mean().idxmax())

print("\nQuantidade de universidades por país:")
print(df.groupby("country")["institution"].count())

print("\nTop 10 países com mais universidades:")
print(df.groupby("country")["institution"].count().sort_values(ascending=False).head(10))

# ============================================================
# EXERCÍCIO 7 – Análise por Ano
# ============================================================
media_ano = df.groupby("year")["score"].mean()
print("\nMédia do score por ano:")
print(media_ano)

print("\nAno com maior média:")
print(media_ano.idxmax())

media_ano.plot(marker="o", figsize=(8, 4), title="Evolução do score médio por ano")
plt.xlabel("Ano")
plt.ylabel("Score médio")
plt.grid(True)
plt.show()