import random
import pickle
def crearLista():

    lista=[]
    for i in range(20):
        lista.append(random.randint(-100,100))
    print(lista)
    fitx= open('lista.txt','w')
    pickle.dump(lista,file)
    fitx.close
