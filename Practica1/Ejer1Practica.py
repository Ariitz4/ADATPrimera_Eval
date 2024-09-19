def encriptarPalabra(palabra,clave):
    
    palabra=palabra.upper()
    clave=clave.upper()
    cont=0
    encriptada=''
    for letraPal in palabra:
        letraClav=ord(clave[cont])-ord('A')
        letraPal=ord(letraPal)-ord('A')
        cont=cont+1
        letraEncrip=letraClav+letraPal
        if letraEncrip<0:
            letraEncrip=letraEncrip+26
        if letraEncrip>25:
            letraEncrip=letraEncrip-26
        letraEncrip=chr(letraEncrip+ord('A'))
        encriptada=encriptada+letraEncrip
    return encriptada

def desencriptarPalabra(encriptada,clave):
    clave=clave.upper()
    cont=0
    palaOrig=''
    for letraEnc in encriptada:
        letraClav=ord(clave[cont])-ord('A')
        letraEnc=ord(letraEnc)-ord('A')
        cont=cont+1
        letraFin=letraEnc-letraClav
        if letraFin<0:
            letraFin=letraFin+26
        if letraFin>25:
            letraFin=letraFin-26
        letraFin=chr(letraFin+ord('A'))
        palaOrig=palaOrig+letraFin
    return palaOrig

def arreglaClave(clave):
    cont=0
    for i in range(len(clave),len(palabra)):
        clave=clave+clave[cont]
        cont=cont+1
        
    return clave

if __name__ == "__main__":
    palabra="ataque"
    clave="clave"
    clave=arreglaClave(clave)
    print(encriptarPalabra(palabra,clave))
    palabraEncrip=encriptarPalabra(palabra,clave)
    print(desencriptarPalabra(palabraEncrip,clave))