def recogerDiccionario(dic,valorBuscado):
    return valorBuscado in dic.values()
if __name__ =='__main__':
    diccion={
        "mp3":1,
        "mp4":2,
        "nuevo movil":3
    }
    print(recogerDiccionario(diccion,1))
