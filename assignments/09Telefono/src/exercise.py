def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
    nm=int(input("Dame el número de mensajes: "))
    nme=float(input("Dame el número de megas: "))
    nmin=int(input("Dame el número de minutos: "))
    numm=nm*0.8
    numme=nme*0.8
    numin=nmin*0.8
    cm=numm+numme+numin
print("El costo mensual es: ",cm)
    pass


if __name__ == '__main__':
    main()
