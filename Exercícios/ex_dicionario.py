# =========================================
# Lista de Exercícios sobre Dicionário
# =========================================

# -------------------------------------------------
# Exercício 1: Criando um Dicionário
# -------------------------------------------------
aluno = {
    "nome": "Lucas",
    "idade": 19,
    "curso": "Análise e Desenvolvimento de Sistemas"
}

print("Exercício 1")
print("Nome:", aluno["nome"])
print("Idade:", aluno["idade"])
print("Curso:", aluno["curso"])


# -------------------------------------------------
# Exercício 2: Manipulação de Dicionário
# -------------------------------------------------
produto = {
    "nome": "Teclado Mecânico",
    "preco": 350.00,
    "estoque": 10
}

produto["marca"] = "Redragon"
produto["preco"] = 320.00
produto["estoque"] -= 2
del produto["marca"]

print("\nExercício 2")
print(produto)


# -------------------------------------------------
# Exercício 3: Iterando sobre um Dicionário
# -------------------------------------------------
notas = {
    "Alice": 8.5,
    "Bruno": 7.0,
    "Carla": 9.2,
    "Daniel": 6.8
}

print("\nExercício 3")
soma_notas = 0

for nome, nota in notas.items():
    print(f"{nome}: {nota}")
    soma_notas += nota

media = soma_notas / len(notas)
print("Média das notas:", media)


# -------------------------------------------------
# Exercício 4: Soma de Valores
# -------------------------------------------------
numeros = {"a": 10, "b": 20, "c": 30}

soma = 0
for valor in numeros.values():
    soma += valor

print("\nExercício 4")
print("Soma dos valores:", soma)


# -------------------------------------------------
# Exercício 5: Contagem de Itens Repetidos
# -------------------------------------------------
lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]

frequencia = {}
for item in lista:
    if item in frequencia:
        frequencia[item] += 1
    else:
        frequencia[item] = 1

print("\nExercício 5")
print(frequencia)


# -------------------------------------------------
# Exercício 6: Filtrando Dicionário
# -------------------------------------------------
produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}

produtos_filtrados = {}
for nome, preco in produtos.items():
    if preco > 50:
        produtos_filtrados[nome] = preco

print("\nExercício 6")
print(produtos_filtrados)


# -------------------------------------------------
# Exercício 7: Tradutor Simples
# -------------------------------------------------
tradutor = {
    "book": "livro",
    "house": "casa",
    "car": "carro",
    "dog": "cachorro",
    "cat": "gato"
}

print("\nExercício 7")
palavra = input("Digite uma palavra em inglês: ").lower()

if palavra in tradutor:
    print("Tradução:", tradutor[palavra])
else:
    print("Palavra não encontrada")


# -------------------------------------------------
# Exercício 8: Lista de Compras
# -------------------------------------------------
print("\nExercício 8")
lista_compras = {}

while True:
    print("\n1 - Adicionar produto")
    print("2 - Atualizar quantidade")
    print("3 - Remover produto")
    print("4 - Exibir lista")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        produto = input("Nome do produto: ")
        quantidade = int(input("Quantidade: "))
        lista_compras[produto] = quantidade

    elif opcao == "2":
        produto = input("Produto para atualizar: ")
        if produto in lista_compras:
            quantidade = int(input("Nova quantidade: "))
            lista_compras[produto] = quantidade
        else:
            print("Produto não encontrado.")

    elif opcao == "3":
        produto = input("Produto para remover: ")
        if produto in lista_compras:
            del lista_compras[produto]
            print("Produto removido.")
        else:
            print("Produto não encontrado.")

    elif opcao == "4":
        print("Lista de compras:")
        for produto, quantidade in lista_compras.items():
            print(f"{produto}: {quantidade}")

    elif opcao == "0":
        break

    else:
        print("Opção inválida.")

print("Lista final de compras:", lista_compras)


# -------------------------------------------------
# Exercício 9: Dicionário Aninhado
# -------------------------------------------------
turma = {
    "Ana": {"idade": 17, "notas": [8, 9, 7]},
    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]}
}

# 1. Adicione um novo aluno
turma["Carlos"] = {"idade": 16, "notas": [7, 8, 9]}

print("\nExercício 9")
maior_media = -1
melhor_aluno = ""

# 2. Calcule a média de cada aluno
for nome, dados in turma.items():
    media = sum(dados["notas"]) / len(dados["notas"])
    print(f"{nome}: Média {media:.1f}")

    # 3. Encontre o aluno com a maior média
    if media > maior_media:
        maior_media = media
        melhor_aluno = nome

print("Aluno com a maior média:", melhor_aluno)


# -------------------------------------------------
# Exercício 10: Cadastro de Funcionários
# -------------------------------------------------
print("\nExercício 10")
funcionarios = {}

while True:
    print("\n1 - Cadastrar funcionário")
    print("2 - Consultar funcionário")
    print("3 - Exibir todos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        cargo = input("Cargo: ")
        salario = float(input("Salário: "))

        funcionarios[nome] = {
            "cargo": cargo,
            "salario": salario
        }
        print("Funcionário cadastrado com sucesso.")

    elif opcao == "2":
        nome = input("Digite o nome do funcionário: ")
        if nome in funcionarios:
            print(f"Nome: {nome}")
            print(f"Cargo: {funcionarios[nome]['cargo']}")
            print(f"Salário: R$ {funcionarios[nome]['salario']:.2f}")
        else:
            print("Funcionário não encontrado.")

    elif opcao == "3":
        print("Funcionários cadastrados:")
        for nome, dados in funcionarios.items():
            print(f"{nome} - Cargo: {dados['cargo']} - Salário: R$ {dados['salario']:.2f}")

    elif opcao == "0":
        break

    else:
        print("Opção inválida.")