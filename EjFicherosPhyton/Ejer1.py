import random
def rnd_world(fitxategi1,fitxategi2):
    file=open(fitxategi1,'r')
    lista=[]
    for linea in file:
        listaP=linea.split(' ')
        lista.append(random.choice(listaP))
    file.close()
    file2=open(fitxategi2,'a')
    for i in lista:
        print(i)
        file2.write(i+'\n')
    file2.close()

rnd_world('/home/dm2/Escritorio/ADAT/EjFicherosPhyton/comida.txt','/home/dm2/Escritorio/ADAT/EjFicherosPhyton/menu.txt')