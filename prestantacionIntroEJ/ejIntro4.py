if __name__ =='__main__':
    palabra=input('escribe palabra')
    cont=0
    aux=''
    while cont<len(palabra)*2:
        aux+=' '
        cont+=1
    aux+=palabra
    print(aux)