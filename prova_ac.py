
# Questão 1: Carregar o DataFrame
# LER arquivo titanic.csv em um DataFrame pandas chamado df?
df = pd.read_csv("titanic.csv")


# Questão 2: Filtrar passageiros do sexo feminino
# Filtrar o DataFrame para mostrar apenas as Mulheres?
# (Dica: Filtar onde a coluna "Sex" é igual a "female")
mulheres = df[df["Sex"] == "female"]
print("Passageiras do sexo feminino:")
print(mulheres)

# Questão 3: Contar sobreviventes
# Quantos passageiros Sobreviveram?
# (Dica: Sobreviventes têm o valor 1 na coluna "Survived")
sobreviventes = (df["Survived"] == 1).sum()
print("Quantidade de sobreviventes:", sobreviventes)

# Questão 4: Calcular a média da idade
# Quantos Homens Sobreviveram?
homens_sobreviveram = ((df["Sex"] == "male") & (df["Survived"] == 1)).sum()
print("Quantidade de homens que sobreviveram:", homens_sobreviveram)

# Questão 5: Calcular Nome "John"
# Calcular quantos passageiros tem o nome "John"?
# (Dica: Usar a coluna "Name")
qtd_john = df["Name"].str.contains("John", case=False, na=False).sum()
print("Quantidade de passageiros com nome 'John':", qtd_john)