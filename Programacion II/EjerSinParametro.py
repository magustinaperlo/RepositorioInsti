
import random

def randomOne ():
    cont = 0
    lista = []
   
    while cont < 6:
        num=random.randint(10,60)
        lista.append(num)
        cont += 1
    print(lista)
randomOne()


def lecturaLista ():
    lista= [68,69,10,11,33,56,90] #(lista cargada con antelacion)
    lista_par = []
    lista_impar = []
    for i in range (0,len(lista)): #(recorre la lista y guarda los numeros pares e impares en otras dos listas)
        if (lista[i] % 2 == 0):
            lista_par.append(lista[i])
        else:
            lista_impar.append(lista[i])

    print("Los numeros pares son:" + str(lista_par))
    print("Los numeros impares son:" + str(lista_impar))

lecturaLista()

#sugerencia

def lecturaLista():
    lista = [68, 69, 10, 11, 33, 56, 90]  # Lista cargada con antelación
    lista_par = []
    lista_impar = []
    for num in lista:  # Recorre la lista y guarda los números pares e impares en otras dos listas
        if num % 2 == 0:
            lista_par.append(num)
        else:
            lista_impar.append(num)

    print("Los números pares son: " + str(lista_par))
    print("Los números impares son: " + str(lista_impar))

lecturaLista()


def listaDivisores():

    lista= [64,8,10,2,33,11,90,9] #(lista cargada con antelacion)
    division= 0
    cont = 0
    for i in range (0,int(len(lista)/2)): 
        division= lista[cont] / lista[cont+1]
        cont += 2
        print("La division da:  " + str(division))
       
listaDivisores ()


def textoXD ():
    msj=""
    msj=msj + "                                   " + "Bienvenidos" + "                                            " + "\n" +"_______________________________________________________________________________"
    msj= msj + "\n" + "                        A mi prototipo de calculadora..............."
    print(msj)
textoXD ()

#def multiplisdelUnoalNueve(): 
def multiplosDelUnoAlNueve():
    #multiplos=0
    listaNum=[1,2,3,4,5,6,7,8,9,10]
    for i in listaNum:
        #cont=1
        listaMultiplos=[]
        for k in range(1,11):
            # multiplos= i * cont
            multiplos = i * k
            listaMultiplos.append(multiplos)
            #cont+=1
        print("Las tablas del:  " + str(i) +"\n" +str(listaMultiplos))
multiplosDelUnoAlNueve()

