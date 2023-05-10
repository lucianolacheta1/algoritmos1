"""Desarrollar una función que reciba tres números positivos 
y devuelva el mayor de los tres, sólo si éste es único (mayor estricto).
En caso de no existir el mayor es-tricto devolver -1.
No utilizar operadores lógicos (and, or, not).
Desarrollar también un programa para ingresar los tres valores, 
invocar a la función y mostrar el máximo hallado, 
o un mensaje informativo si éste no existe."""

import random

def mayor(n1, n2, n3):
    #Toma 3 numeros positivos y devuelve el mayor
    x = -1
    #if n1>0 and n2>0 and n3>0:
    if n1>n2:
        if n1>n3: x = n1
    elif n2>n3: x = n2
    elif n3>n1:
        if n3>n2: x = n3

    
    return x

list = []

print("Escribir 3 numeros positivos:")
for i in range(3):
    #print("Ingrese el valor del n",i+1)
    #list.append(int(input()))
    list.append(random.randint(0,10))
    print(list[i])

res = mayor(list[0],list[1],list[2])

if res == -1: print("No fue posible encontrar el mayor")
else: print("El numero mayor es: ",res)
