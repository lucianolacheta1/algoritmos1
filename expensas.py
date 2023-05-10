
"""
Un consorcio desea controlar la cobranza de las expensas en un edificio de 5 pisos
donde existen 15 departamentos en cada piso. 
El valor de las expensas es de $ 10000. 
Para registrar la cobranza se ingresa el número de piso (1 a 5) y el número de departamento
(correlativo de 1 a 7 en cada piso). 
El ingreso finaliza con un piso igual a 99.
Al finalizar mostrar el dinero total recaudado y una tabla con una X indicando aquellos
departamentos deudores de la siguiente manera:

     TOTAL RECAUDADO  $XXXXXXX.XX
DEPARTAMENTOS DEUDORES
PISO       DPTO 1 DPTO2 … DPTO 7
PISO 1       X
PISO 2       X      X
PISO 3                       X
PISO 4       X      X
PISO 5       X         X
"""
def mostrarm( m, vl, filas, columnas):

    print("\n\n\n  DEPARTAMENTOS DEUDORES->>\n")
    print ("LISTA\t01\t02\t03\t04\t05\t06\t07")
    for i in range (filas):
        mensaje=""
        mensaje="\n%s\t" %vl[i]
        for j in range (columnas):
            
            mensaje=mensaje + "%3d\t" %m[i][j]
        print(mensaje)

vlista = ["PISO 1","PISO 2","PISO 3","PISO 4","PISO 5"]
medificio=[[0] * 10 for i in range (10)]

mostrarm(medificio,vlista,5,7)
