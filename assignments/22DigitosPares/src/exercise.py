def main():
    #escribe tu código abajo de esta línea
    numero=int(input("Dame un número: "))
    dPar=0
    if numero>1000 and numero<=1000 or numero>=1000 and numero<1000:
        while(numero>0):
            if numero%2==0:
                dPar=dPar+1
            else:
                dPar=dPar+0
            numero=numero//10
        print("El número de dígitos pares es:",dPar)
    else:
        print("El número debe de ser de 4 dígitos:")
    pass
 
if __name__ == '__main__':
    main()
