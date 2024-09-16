if __name__ =='__main__':
    palabra=input('Escribe palabra')
    letra=input('Que letra quieres buscar')
    cont=0
    contiene=False
    while cont<len(palabra) and contiene==False:
        if palabra[cont]==letra:
            print(cont+1)
            contiene=True
        cont=cont+1
    if contiene==False:
        print(-1)

            