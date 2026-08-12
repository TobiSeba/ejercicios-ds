class CuentaBancaria:
    def __init__(self, titular, saldo = 0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Se deposito ${monto} en la cuenta bancaria")
        else:
            print("ERROR: El monto a depositar debe ser positivo")

    def retirar(self, monto):
        if monto < 0:
            print("ERROR: El monto a retirar debe ser positivo")
        elif monto > self.saldo:
            print("ERROR: El monto a retirar es mayor al saldo disponible")
        else:
            self.saldo -= monto
            print(f"Se retiro ${monto} de la cuenta bancaria")

    def mostrarInfo(self):
        print("Informacion de la cuenta:")
        print(f"Titular de la cuenta: {self.titular}")
        print(f"Saldo actual de la cuenta: ${self.saldo}")

if __name__ == "__main__":
    c1 = CuentaBancaria("Tobias Sabbione")
    c1.mostrarInfo()
    print()
    c1.depositar(-1)
    print()
    c1.depositar(1000)
    print()
    c1.mostrarInfo()
    print()
    c1.retirar(-3)
    print()
    c1.retirar(2000)
    print()
    c1.retirar(500)
    print()
    c1.mostrarInfo()
    print()
    print("=======================================")
    print()
    c2 = CuentaBancaria("Lionel Messi", 100000.4)
    c2.mostrarInfo()
    print()
    c2.depositar(123450)
    print()
    c2.mostrarInfo()
    print()
    c2.retirar(9876)
    print()
    c2.mostrarInfo()