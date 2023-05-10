'''

EJERCICIO
 
VAMOS A CARGAR LA EDAD DE LOS ESTUDIANTES DE UN CURSO DE PROGRAMACION.
LAS EDADES ADMITIDAS ES A PARTIR DE LOS 17 ANIOS. CUALQUIER EDAD INFERIOR DEBE INDICAR UN ERROR
EL CURSO TIENE COMO MAXIMO 10 ALUMNOS. CONTROLAR DICHO CUPO, la carga finaliza con una edad -1
 
UTILIZAR LA FUNCION
 
- ingresaValidaEdad que recibe por parametro el valor minimo admitido de una edad y devuelve el valor
ingresado y validado
- cargaEdades que solicita el ingreso y carga de las edades, utilizar una lista para manejar estos datos
- mostrarEdades que recibe una lista cargada y la muestra en pantalla
- mostrar la mayor edad
- mostrar la menor edad
- mostrar cuantos alumnos hay en el curso
- generar una funcion calculaPromedio que recibe la lista, y devuelve la edad promedio
- generar una copia de la lista original y ordenarla de manera ascendente. La copia y el ordenamiento
se realiza en la funcion:copiaYOrdena
- generar una funcion llamada contarCuantos que reciba la lista y una edad especifica, devuelve cuantos
alumnos de esa edad hay en el curso
 
'''

"""
def ingresaValidaEdad(edadmin,corte):
    edad = int(input("Ingrese una edad valida: "))

    while edad < edadmin and edad != corte:
        edad = int(input("Ingrese una edad valida: "))

    return edad


def cargaEdades(lista, total):
    edad = ingresaValidaEdad(18,-1)

    while len(lista)< total and edad != -1:
        lista.append(edad)

        if len(lista) < total: edad = ingresaValidaEdad(18,-1)


def mostrarEdades(lista):
    for elements in lista:
        print(elements)

    print("-----------------------")



edades = []

cargaEdades(edades,10)

if len(edades) > 0:

    mostrarEdades(edades)

"""
'''
Generar una lista con números al azar entre 0 y 100, donde su cantidad de
elementos será un número par también obtenido al azar entre 10 y 50. 
Luego se solicita partir la lista por la mitad a través de la técnica de 
las rebanadas, creando dos nuevas listas. Imprimir las tres listas por
pantalla.
'''
from random import randint

cant = randint(10,50)
lista=[]
for i in range (cant):
    lista.append(randint(0,100))

lista1 = lista[cant//2:]
lista2 = lista[:cant//2]

print(lista)
print(lista1)
print(lista2)

'''
Utilizar la técnica de listas por comprensión para construir
una lista con todos los números impares comprendidos entre 
100 y 200.
'''

lista3 = [x for x in range(100,200) if x%2==1]

print(lista3)