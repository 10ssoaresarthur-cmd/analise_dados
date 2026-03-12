import pandas as pd

df = pd.read_csv("ds_salaries.csv")   # troque pelo nome correto do arquivo
col_salario = "salary"   # se existir salary_in_usd, pode usar: col_salario = "salary_in_usd"

# 1. Quantas linhas e quantas colunas tem o dataset?
print("1)", df.shape)

# 2. Qual a média salarial? Qual é o maior salário? O menor salário?
print("2) Média salarial:", df[col_salario].mean())
print("   Maior salário:", df[col_salario].max())
print("   Menor salário:", df[col_salario].min())

# 3. Crie um df com apenas as colunas job_title, salary, company_location, company_size, remote_ratio
df2 = df[["job_title", col_salario, "company_location", "company_size", "remote_ratio"]]
print("3)")
print(df2.head())

# 4. Qual é o maior e menor salário de um “Data Scientist”? Onde fica essas empresas?
ds = df[df["job_title"] == "Data Scientist"]

maior_ds = ds.loc[ds[col_salario].idxmax(), ["job_title", col_salario, "company_location"]]
menor_ds = ds.loc[ds[col_salario].idxmin(), ["job_title", col_salario, "company_location"]]

print("4) Maior salário de Data Scientist:")
print(maior_ds)
print("   Menor salário de Data Scientist:")
print(menor_ds)

# 5. Qual a profissão com a maior média salarial? E a menor?
media_prof = df.groupby("job_title")[col_salario].mean().sort_values()

print("5) Profissão com menor média salarial:")
print(media_prof.head(1))
print("   Profissão com maior média salarial:")
print(media_prof.tail(1))

# 6. Quais as profissões com a média salarial maior que a média geral?
media_geral = df[col_salario].mean()
prof_acima_media = df.groupby("job_title")[col_salario].mean()
prof_acima_media = prof_acima_media[prof_acima_media > media_geral].sort_values(ascending=False)

print("6)")
print(prof_acima_media)

# 7. Qual a localização com maior média salarial?
media_local = df.groupby("company_location")[col_salario].mean().sort_values(ascending=False)
print("7)")
print(media_local.head(1))

# 8. Quais as profissões que existem no Brasil (BR)?
prof_br = df[df["company_location"] == "BR"]["job_title"].drop_duplicates().sort_values()
print("8)")
print(prof_br)

# 9. Qual a média salarial no Brasil?
media_br = df[df["company_location"] == "BR"][col_salario].mean()
print("9)", media_br)

# 10. Quantas profissões existem no Brasil?
qtd_prof_br = df[df["company_location"] == "BR"]["job_title"].nunique()
print("10)", qtd_prof_br)

# 11. Qual a profissão que mais ganha no Brasil?
prof_mais_ganha_br = (
    df[df["company_location"] == "BR"]
    .groupby("job_title")[col_salario]
    .mean()
    .sort_values(ascending=False)
)

print("11)")
print(prof_mais_ganha_br.head(1))

# 12. Quantas profissões tem nos US e que trabalham em empresas grandes (L)?
qtd_prof_us_l = df[
    (df["company_location"] == "US") & (df["company_size"] == "L")
]["job_title"].nunique()

print("12)", qtd_prof_us_l)

# 13. Qual é a média salarial das empresas médias (M) na Canada (CA)?
media_ca_m = df[
    (df["company_location"] == "CA") & (df["company_size"] == "M")
][col_salario].mean()

print("13)", media_ca_m)

# 14. Qual é o país com mais profissões? E qual é o país com menos?
prof_por_pais = df.groupby("company_location")["job_title"].nunique().sort_values()

print("14) País com menos profissões:")
print(prof_por_pais.head(1))
print("    País com mais profissões:")
print(prof_por_pais.tail(1))

# 15. Quem ganha mais: remoto, presencial ou híbrido?
# remote_ratio: 0 = presencial, 50 = híbrido, 100 = remoto
media_remoto = df.groupby("remote_ratio")[col_salario].mean()

print("15) Média salarial por tipo de trabalho:")
print(media_remoto)

# se quiser mostrar com nomes
mapa = {0: "Presencial", 50: "Híbrido", 100: "Remoto"}
media_remoto_nome = media_remoto.rename(index=mapa).sort_values(ascending=False)

print("   Ranking:")
print(media_remoto_nome)

# 16. Qual o país com maior número de profissões trabalhando 100% remoto?
pais_100_remoto = (
    df[df["remote_ratio"] == 100]
    .groupby("company_location")["job_title"]
    .nunique()
    .sort_values(ascending=False)
)

print("16)")
print(pais_100_remoto.head(1))