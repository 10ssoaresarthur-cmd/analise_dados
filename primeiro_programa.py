x = 4
idade = 4
objeto ="palhaço"
lista = [x, idade, objeto]
lista[2]

lista_mista = ["cavalo", "pato", 16, 17]
animal =[]
numero =[]

for item in lista_mista:
 if type(item) == str:
  animal.append(item)
 elif type(item) == int:
  numero.append(item)





dict_mista= {
 0 :"cavalo",
 1 :"pato",
 2 : 16,
 3 : 17
}

dict_mista[1]


