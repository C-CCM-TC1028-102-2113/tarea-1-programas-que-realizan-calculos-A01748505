def main():
    #escribe tu código abajo de esta línea
    gramos=int(input("Dame la harina en gramos: "))
    levadura=(((gramos/1000))*50)
    levadura=round(levadura,1)
    print("Necesitas estos gramos de levadura:",levadura)
    pass


if __name__ == '__main__':
    main()
