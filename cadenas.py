"""
Ejercicio 1:
Enunciado: Dada una cadena de caracteres, devuelve una nueva cadena que contenga los
primeros tres caracteres y los últimos tres caracteres de la cadena original.
Cadena de ejemplo: "abcdefghij"
Salida : "ablij"

ej = "abcdefghij"

cad = ej[0:3] + ej[(len(ej)-3):len(ej)]

print(ej)
print(cad)
"""

"""
Ejercicio 2:
Enunciado: Dada una lista de números, devuelve una nueva lista que contenga el segundo
y tercer elemento de la lista original.
Lista de ejemplo: [10, 20, 30, 40, 50]
Salida : [20, 30]

ej = [10, 20, 30, 40, 50]
cad = ej[1:3]

print(ej)
print(cad)
"""

"""
Ejercicio 3:
Enunciado: Dada una lista de cadenas de caracteres, devuelve una nueva lista que contenga
las cadenas que tienen una longitud mayor o igual a cinco caracteres.
Lista de ejemplo: ["manzana", "pera", "banana", "uva", "sandia"]
Salida esperada: ["manzana", "banana", "sandia"]


lista_ej = ["manzana", "pera", "banana", "uva", "sandia"]
lista = [x for x in lista_ej if len(x)>=5]

print(lista)
"""

"""
Ejercicio 4:
Enunciado: Dada una cadena de caracteres, devuelve una nueva cadena que contenga
los caracteres de la cadena original en orden inverso.
Cadena de ejemplo: "Hola mundo!"
Salida: "!odnum aloH"

ej = "Hola mundo!"
zever = ej[::-1]
print(zever)
"""

"""
Ejercicio 5:
Enunciado: Dada una lista de números, devuelve una nueva lista que contenga solo los números pares de la lista original.
Lista de ejemplo: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Salida: [2, 4, 6, 8]
"""


"""
Ejercicio 6
Enunciado: Dada una lista de números, crea una lista que contenga
los números impares multiplicados por 3 y los números pares divididos por 2.
"""

"""
Ejercicio 7

Dada una lista de palabras, crea una lista que contenga todas las
palabras que tengan más de 4 letras y que empiecen y terminen con
la misma letra.

"""



"""
Ejercicio 8

Dada una lista de strings, crea una lista que contenga todas las palabras
que empiezan por vocal y terminan por consonante.

"""


"""
Ejercicio 9

Dada una lista de números, crea una lista que contenga la
suma acumulada de los números de la lista.
Ejemplo:
lista = [1, 2, 3, 4, 5]
resultado = [1, 3, 6, 10, 15]

"""