# =========================================
# Exercício sobre Listas
# =========================================

# 1. Crie uma lista frutas contendo as seguintes frutas:
frutas = ["maçã", "banana", "laranja", "uva"]

# 2. Imprima o primeiro e o último elemento da lista.
print("Primeiro elemento:", frutas[0])
print("Último elemento:", frutas[-1])

# 3. Adicione a fruta "manga" ao final da lista.
frutas.append("manga")
print("Após adicionar manga:", frutas)

# 4. Remova a fruta "banana" da lista.
frutas.remove("banana")
print("Após remover banana:", frutas)

# 5. Substitua "laranja" por "abacaxi".
indice_laranja = frutas.index("laranja")
frutas[indice_laranja] = "abacaxi"
print("Após substituir laranja por abacaxi:", frutas)

# 6. Crie uma lista numeros contendo os números de 1 a 10.
numeros = list(range(1, 11))
print("Lista números:", numeros)

# 7. Calcule e imprima a soma de todos os números da lista.
print("Soma dos números:", sum(numeros))

# 8. Encontre e imprima o maior e o menor número da lista.
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))

# 9. Inverta a ordem dos elementos na lista e imprima a lista invertida.
numeros_invertidos = numeros[::-1]
print("Lista invertida:", numeros_invertidos)

# 10. Crie uma lista cidades contendo as seguintes cidades:
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]

# 11. Ordene a lista cidades em ordem alfabética.
cidades.sort()
print("Cidades em ordem alfabética:", cidades)

# 12. Adicione a cidade "Porto Alegre" ao final da lista.
cidades.append("Porto Alegre")
print("Após adicionar Porto Alegre:", cidades)

# 13. Encontre o índice da cidade "Curitiba" na lista.
print("Índice de Curitiba:", cidades.index("Curitiba"))

# 14. Remova a cidade "Rio de Janeiro" da lista.
cidades.remove("Rio de Janeiro")
print("Após remover Rio de Janeiro:", cidades)

# 15. Crie duas listas lista1 e lista2
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# 16. Concatene lista1 e lista2 em uma nova lista lista3.
lista3 = lista1 + lista2

# 17. Imprima lista3.
print("Lista3:", lista3)

# 18. Crie duas listas animais_domesticos e animais_selvagens
animais_domesticos = ["cachorro", "gato", "coelho"]
animais_selvagens = ["leão", "tigre", "urso"]

# 19. Concatene as duas listas em uma nova lista todos_animais.
todos_animais = animais_domesticos + animais_selvagens

# 20. Imprima todos_animais.
print("Todos os animais:", todos_animais)


# =========================================
# Looping com for
# =========================================

# 21. Crie uma lista nomes
nomes = ["Ana", "Pedro", "Maria", "João"]

# 22. Utilize um loop for para imprimir cada nome da lista.
print("\nNomes:")
for nome in nomes:
    print(nome)

# 23. Crie uma nova lista nomes_maiusculos usando for.
nomes_maiusculos = []
for nome in nomes:
    nomes_maiusculos.append(nome.upper())

print("Nomes em maiúsculo:", nomes_maiusculos)

# 24. Crie uma lista numeros contendo os números de 1 a 20.
numeros = list(range(1, 21))
print("\nNúmeros pares de 1 a 20:")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)

# 25. Usando a lista numeros, crie uma nova lista quadrados.
quadrados = []
for numero in numeros:
    quadrados.append(numero ** 2)

print("Quadrados:", quadrados)

# 26. Crie uma lista palavras e imprima o tamanho de cada palavra.
palavras = ["python", "java", "c", "javascript"]
print("\nTamanho das palavras:")
for palavra in palavras:
    print(palavra, "->", len(palavra))

# 27. Crie uma lista idades e informe maior/menor de idade.
idades = [12, 18, 25, 40, 60]
print("\nClassificação das idades:")
for idade in idades:
    if idade >= 18:
        print(idade, "- maior de idade")
    else:
        print(idade, "- menor de idade")

# 28. Crie uma lista notas e conte aprovados e reprovados.
notas = [5.5, 7.0, 8.3, 4.9, 6.2]
aprovados = 0
reprovados = 0

for nota in notas:
    if nota >= 7:
        aprovados += 1
    else:
        reprovados += 1

print("\nAprovados:", aprovados)
print("Reprovados:", reprovados)

# 29. Crie uma lista compras e imprima cada item.
compras = ["arroz", "feijão", "batata", "carne"]
print("\nLista de compras:")
for item in compras:
    print("Preciso comprar:", item)


# =========================================
# Looping usando while
# =========================================

# 30. Use um loop while para imprimir os números de 1 a 10.
print("\nNúmeros de 1 a 10:")
contador = 1
while contador <= 10:
    print(contador)
    contador += 1

# 31. Peça para o usuário digitar um número inteiro até digitar 0.
print("\nDigite números inteiros. O programa para quando você digitar 0.")
numero = None
while numero != 0:
    numero = int(input("Digite um número: "))

# 32. Utilize um loop while para calcular a soma dos números de 1 a 100.
soma = 0
contador = 1
while contador <= 100:
    soma += contador
    contador += 1

print("Soma de 1 até 100:", soma)

# 33. Peça para o usuário adivinhar um número secreto.
numero_secreto = 7
palpite = None

while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número secreto: "))
    if palpite != numero_secreto:
        print("Tente novamente!")

print("Parabéns! Você acertou.")

# 34. Crie um loop while que imprima todos os números pares de 2 até 20.
print("Números pares de 2 até 20:")
numero = 2
while numero <= 20:
    print(numero)
    numero += 2
    