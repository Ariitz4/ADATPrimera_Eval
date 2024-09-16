if __name__ =='__main__':
    numD=int(input('Escribe numero decimal'))
    aux=0
    cont=1
    while numD>1:
        aux+=(numD%2)*cont
        numD=int(numD/2)
        cont*=10
    aux+=1*cont
    print(aux)