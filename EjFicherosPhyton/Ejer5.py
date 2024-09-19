def crearLibro():

    nomLib=input("Introduce nombre del libro")
    nomAut=input("Introduce nombre de autor")
    precLib=input("Introduce precio del libro")
    precDesc=input("Introduc el precio despues del descuento")
    numPags=input("Introduce el numero de paginas")

    libro={
        'nombre':nomLib,
        'autor':nomAut,
        'precio':precLib,
        'descuento':precDesc,
        'paginas':numPags
    }
    return libro

def guardarLibro(archivo,libros):
    file=open(archivo,'w')
    for libro in libros:
        file.write(repr(libro)+"\n")


def main():
    archivo="/home/dm2/Escritorio/ADAT/EjFicherosPhyton/libros.txt"
    libros=[]
    resp="si"
    while resp=="si":
        libro=crearLibro()
        libros.append(libro)

        resp=input("Quieres introducir mas libros?[si/no]")
    
    guardarLibro(archivo,libros)

if __name__ == "__main__":
    main()
        
