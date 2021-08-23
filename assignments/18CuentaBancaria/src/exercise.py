def main():
    #escribe tu código abajo de esta línea
smp=float(input("Dame el saldo del mes anterior: "))
ingresos=float(input("Dame los ingresos: "))
egresos=float(input("Dame los egresos: "))
cheque=int(input("Dame el número de cheques: "))
cheques=cheque*13
total=((smp+ingresos-egresos-cheques)*92.5)/100
print("El saldo final de la cuenta es: ", total)
    pass

if __name__ == '__main__':
    main()
