if __name__ =='__main__':
    palabra=input('Escribe palabra')
    letra=input('Que letra quieres buscar')
    if palabra.find(letra)!=-1:
        print(palabra.index(letra)+1)
    else:
        print('-1')
