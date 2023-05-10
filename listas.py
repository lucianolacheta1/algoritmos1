from random import randint


frutas = ["manzana","banana", "pera"]

print(frutas)

frutas.remove('banana')

print(frutas)

frutas.pop()

print(frutas)

frutas.insert(1,'mandarina')

print(frutas)

frutas.append('naranja')

print(frutas)

frutas.pop(1)

print(frutas)

if 'manzana' in frutas:
    indice_manzana = frutas.index('manzana')

print("'manzana' esta en el indice:",indice_manzana)

count_manzana = frutas.count('manzana')

print("'manzana' aparece tantas veces:",count_manzana)

frutas.clear()

print(frutas)

lista = [0] * 10

frutas.extend(lista)

for i in range(len(frutas)):
    frutas[i] = randint(0,10)

print(frutas)

frutas.sort()

print(frutas)

frutas.reverse()

print(frutas)

frutas.clear()

nombre = ['Juan','Pedro','Maria','Lucia']
edad = [25,32,18,27]
altura = [1.80,1.70,1.60,1.50]

datos = list(zip(nombre, edad, altura))

datos.sort(key=lambda x: x[1])

for nombre, edad, altura in datos:
    print(nombre,edad,altura)
