def validarUsuario():
    nombre=input("Ingrese un nombre de usuario alfanumerio de 6 a 12 caracteres")
    
    while (len(nombre)<6 or len(nombre)>12)and nombre.isalnum()==False:
        print("Error - Nombre menor a 6 caracteres / alfanumerico")
        nombre=input("Ingrese un nombre de usuario alfanumerio de 6 a 12 caracteres")
       
    return nombre


def ejercicio3():
    print("EJERCICIO 3")
    listaPorComprension=[i for i in range(100,200) if i%2!=0]
    print(listaPorComprension)
    

def ingresa_valida(vector,linf,lsup,mensaje):
    unico = True
    nro=int(input(mensaje))
    if nro in vector:
        unico=False 
        
    while(nro < linf or nro > lsup or not unico):
        nro=int(input(mensaje))
        if nro in vector:
            unico= False
        else:
            unico=True
    return nro

def ingresa_valida2( valor,mensaje):
    nro=int(input(mensaje))
    while(nro <= valor):
        nro=int(input(mensaje))
    return nro

def leeControlRango(mensaje,li,ls):
    nro=int(input(mensaje))
    while(nro<li or nro>ls):
        nro=int(input(mensaje))
    return nro

def carga_codigos( vec,  cant):
    print("Ingrese los " + str(cant) + " codigos de modelo  ")
    for i in range (cant):        
        vec.append(ingresa_valida(vec,100,999,"ingrese un codigo de modelo de 3 cifras [" + str(i) +"]"))
        

def inicializar_matriz(matriz,cf,cc):  
    for f in range (cf):
        matriz.append([])
        for c in range (cc):
            matriz[f].append(0)
            
def sumarfilas(matriz, vSalida):

    for i in range (len(matriz)):
    
        for j in range(len(matriz[0])):
                vSalida[j]+=matriz[i][j]

            
            
def ListadoCantidad(vCodigos,matriz,filas,columnas):


    print("CANTIDAD CONFECCIONADA\n")
    print("        CODIGO MODELO/ USO")
    
    titulo=""
    for i in range(columnas):
        titulo=titulo+str(i+1).rjust(4," ")
    

    print("     "+titulo + "\n")

    for i in range(filas):
        print(str(vCodigos[i])+" ",end=" ")
        for j in range (columnas):
            print(str(matriz[i][j]).rjust(3," "),end=" ")
        print()

def ModelosSinConfeccionar(matriz,vCodigos):


    print("Modelos sin produccion en ningun uso:\n")    
    
    for i in range(len(matriz)):
        encontrado=False
        for j in range (len(matriz[0])):
            if matriz[i][j]!=0:
                encontrado=True
                
        if not encontrado:
            print(str(vCodigos[i])+"\n")

def BusquedaMod(vector,codigo):
    return codigo not in vector

def ordenar( v1, v2):
          
    print("\nUSO CANTIDAD\n")

    for cant, uso in sorted(zip(v2, v1), reverse = False):
        print(str(uso+1) +"\t" + str(cant) + "\n")



def __main__():
    

    vCodigos=[]
    CantCodigos=5
    m=[]
    
    carga_codigos(vCodigos,CantCodigos)
    print(vCodigos)
   
    inicializar_matriz(m,CantCodigos,3)
    print(m)
    
    print("\n Ingresar de la produccion ")

    codigo=int(input("ingrese codigo:"))
    while codigo!=-10:        
        
        while(BusquedaMod(vCodigos,codigo) and codigo!=-10):
            print("\nCODIGO ERRONEO.\n")
            codigo=int(input("ingrese codigo"))
        
        if codigo!=-10:
            uso=leeControlRango("Ingresar uso",1,3)
            cant=ingresa_valida2(0,"Ingresar cantidad producida")
            m[vCodigos.index(codigo)][uso-1]+=cant
        
        codigo=int(input("ingrese codigo:"))
        
    ListadoCantidad(vCodigos,m,CantCodigos,3)     

    vTotalPorUso=[0]*3
    sumarfilas(m,vTotalPorUso)
    ordenar([0,1,2],vTotalPorUso)

    ModelosSinConfeccionar(m,vCodigos)

    print(m)


if __name__ == "__main__":
    __main__()
