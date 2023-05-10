"""
Se desea desarrollar un sistema de reservas de entradas para un teatro
La sala consta de 12 filas numeradas de la 1 a la 12 
y cada fila tiene 9 butacas numeradas a partir de la columna central
 con las butacas impares a la derecha y las pares a la izquierda, 
 como en el siguiente esquema:

           8 6 4 2 1 3 5 7 9

 

Para la carga, se debe mostrar al usuario un esquema con las butacas 
disponibles y reservadas, marcando con la letra D las disponibles y con 
la letra R las reservadas.
Por cada reserva se debe solicitar la fila y número de butaca a reservar.

 

Cada vez que se realice una reserva se deberá actualizar el esquema que 
muestra las butacas. 
Si la butaca seleccionada ya estaba ocupada se debe informar al usuario 
para que seleccione otra.
El proceso de reserva finaliza con una fila con un número negativo.

 

a finalizar mostrar:
    a) la cantidad de asientos disponibles y la cantidad de asientos 
    reservados
    b) los numeros de filas que quedaron vacias
    c) la o las filas con mayor cantidad de espectadores
    d) un listado con la cantidad de personas que se sentaron en los 
    mismos numeros de butacas
    en todo el cine ordenado de mayor a menor por ejemplo:
    
                                              butaca cantidad
                                                1        20
                                                3        15
                                                2        10
                                            ..................
    
    """

def indices_butaca (numero):
    orden = [8,6,4,2,1,3,5,7,9]
    indice = orden.index(numero)
    return indice

def reservar_butaca(matriz):
    c=int(input("Ingrese el numero de columna: "))
    if c != -1:
        f=int(input("Ingrese numero de fila: "))-1
        c = indices_butaca(c)


        estado = comprobar_estado(matriz,f,c)

        if estado != -1:
            matriz[f][c] = "R"
    else: estado = c

    return estado

def comprobar_estado(matriz,f,c):
    c = indices_butaca(c)
    estado = 0

    if matriz[f][c] == "R":
        print("La butaca NO esta disponible")
        estado = -1
    else:
        print("La butaca esta disponible")

    return estado

def printmatriz(matriz,cf,cc):
    for i in range (cf):
        print(matriz[i])

def inicializar_mat(mat,cf,cc):
    for f in range (cf):
        mat.append([])
        for c in range(cc):
            matriz[f].append("D")

#MAIN
cc, cf = 9,12
matriz = []
inicializar_mat(matriz,cf,cc)


orden = ["8","6","4","2","1","3","5","7","9"]

print("Plano de butacas: \n",orden)
printmatriz(matriz,cf,cc)

reserva_realiz=0
while reserva_realiz != -1:
    reserva_realiz = reservar_butaca(matriz)
    printmatriz(matriz,cf,cc)