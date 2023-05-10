from random import randint


def ingresar_cod_modelo(modelos):
    codigo = randint(100,999)
    while len(modelos) < 100:
        if codigo in modelos:
            codigo = randint(100,999)
        else: 
            modelos.append(codigo)


def aux_modelos(modelos,n):
    for i in range(n):
        modelos.append(100+i)


def busquedaMod (modelos,cod):
    return modelos.index(cod)


def ingresar_produccion(matriz,modelos,cod,uso):
    cant = int(input("Ingrese un numero entero y positivo: "))
    if cant > 0:
        matriz[busquedaMod(modelos,cod)][uso-1] += cant
    else: print("Numero ingresado es incorrecto")


def inicializar_mat(mat,cf,cc):
    for f in range (cf):
        mat.append([])
        for c in range(cc):
            mat[f].append(0)


def pedir_modelo(produccion,modelos):

    cod = int(input("Ingrese el codigo del producto: "))

    while cod != -10:
        uso = randint(1,3)
        if cod in modelos:
            ingresar_produccion(produccion,modelos,cod,uso)
        else: 
            print("Codigo erroneo")
            #cod = int(input("Ingrese el codigo del producto: "))
        cod = int(input("Ingrese el codigo del producto: "))


def listadoCantidad(modelos,matriz):
    print("CANTIDAD CONFECCIONADA\n")
    print("CODIGO MODELO / USO \t INTERIOR \t PUBLICO \t GDES.SUP")
    for i in range(len(modelos)):
        print(modelos[i],"\t\t\t", matriz[i][0],"\t\t", matriz[i][1],"\t\t", matriz[i][2])

def imprimir_ordenado(matriz):
    print("USOS EN ORDEN")
    vsalida = [0]*3
    v1 = [0,1,2]
    for i in range (len(matriz)):
        for j in range (len(matriz[0])):
            vsalida[j] += matriz[i][j]


    for cant, uso in sorted(zip(vsalida,v1)):
        print(uso+1,"\t", cant)    

def sin_uso(matriz,modelos):
    v = []
    print("Modelos sin produccion en ningun uso:\n")

    for i in range(len(modelos)):
        if matriz[i][0] == 0 and matriz[i][1] == 0 and matriz[i][2] == 0:  
            v.append(modelos[i])
    print(v)
        
def valida_usuario(usuario):
    num = 0
    alpha = 0
    for char in usuario:
        if char.isdigit(): num += 1
        if char.isalpha(): alpha += 1
     
    if alpha>0 and num>0 and 6<=len(usuario)<=12: 
            print("Bienvenido " + usuario)
    if len(usuario)<6: print("El nombre de usuario es menor a 6 caracteres")
    if len(usuario)>12: print("El nombre de usuario es mayor a 12 caracteres")
    if num<=0 or alpha<=0: print("El nombre de usuario no es alphanumerico")

def lista_impares():
    lista = [i for i in range(100,200) if i%2!=0]
    print(lista)


#MAIN
modelos = []
produccion = []
usuario = "luciano97"

aux_modelos(modelos,20)
#ingresar_cod_modelo(modelos)
inicializar_mat(produccion,len(modelos),3)
#print(produccion)

pedir_modelo(produccion,modelos)

listadoCantidad(modelos,produccion)

imprimir_ordenado(produccion)

sin_uso(produccion,modelos)

valida_usuario(usuario)

lista_impares()
#aux_modelos(modelos)
#print(indice_modelo(modelos,modelos[0]))
#ingresar_produccion(matriz,modelos)
#print(modelos[1])
#print(matriz)

