def main():
    #escribe tu código abajo de esta línea
    import math
    numeropag=int(input("Dame el número de palabras: "))
    paginas=(math.ceil(numeropag/475))
    costo=(((paginas*60))*.90)
    costo=round(costo,1)
    print("El costo de la publicación es:",costo)
    pass


if __name__ == '__main__':
    main()
