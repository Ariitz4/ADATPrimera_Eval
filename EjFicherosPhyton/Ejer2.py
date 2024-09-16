import random
def crearOra(oracion):
    lista=oracion.split(' ')
    palabra1=random.choice(lista)
    palabra2=palabra1
    palabraFin=[]
    cont=0
    while palabra1==palabra2:
        palabra2=random.choice(lista)
    print(palabra1)
    print(palabra2)
    for char1,char2 in zip(palabra1,palabra2):
        palabraFin.append(random.choice([char1,char2]))
    
    if len(palabra1)-len(palabra2)>0:
        cont=len(palabra2)
        while cont<len(palabra1):
            palabraFin.append(palabra1[cont])
            cont=cont+1
    elif len(palabra2)-len(palabra1)>0:
        cont=len(palabra1)
        while cont<len(palabra2):
            palabraFin.append(palabra2[cont])
            cont=cont+1
    print(''.join(palabraFin))

crearOra("Buenas prueba para adat en clase")
