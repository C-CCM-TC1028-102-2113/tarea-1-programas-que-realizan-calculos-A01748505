def main():
#escribe tu código abajo de esta línea
new=int(input("Dame la cantidad de juegos nuevos: "))
used=int(input("Dame la cantidad de juegos usados: "))
newgame=new*1000
usedgame=used*350
result=newgame+usedgame
print("El total de la compra es: ",result)
   pass



if __name__ == '__main__':
    main()
