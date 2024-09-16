if __name__ =='__main__':
    texto=input('Escribe un texto')
    palabras= texto.split()
    contPalabras=0
    contPalabrasSinA=0
    for palabra in palabras:
        if palabra.find('a')==-1:
           contPalabrasSinA+=1
        contPalabras+=1
    porcen=(contPalabrasSinA*100)/contPalabras
    print(porcen)
    