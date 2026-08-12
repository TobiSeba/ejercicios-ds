def menu():
    while True:
        print("Funciones")
        print("a. Calcular la suma de los primeros N números naturales")
        print("b. Encontrar todos los números divisibles por 3 en un rango dado por el usuario")
        print("c. Salir")
        opcion = input("Ingrese una opcion: ").lower()
        if opcion == "a" or opcion == "b" or opcion == "c":
            return opcion
        else:
            print("ERROR: La opcion ingresada no existe, por favor ingrese una opcion valida")

def pedirNumero(mensaje):
    while True:
            try:
                numero = int(input(mensaje))
                return numero
            except ValueError:
                print("ERROR: Debe ingresar un numero valido")

def sumaNaturales():
    while True:
        numero = pedirNumero("Ingrese un numero natural: ")
        if numero >= 0:
            suma = 0
            for i in range(numero + 1):
                suma += i
            print(f"La suma de los primeros {numero} numeros naturales es: {suma}")
            break
        else:  
            print("ERROR: El numero debe ser natural y mayor o igual a 0")

def encontrarDivisiblesXTres():
    while True:
        inicio = pedirNumero("Ingrese un numero como inicio del rango de numeros: ")
        final = pedirNumero("Ingrese un numero como final del rango de numeros: ")
        if inicio <= final:
            break
        else:
            print("ERROR: El valor de inicio debe ser menor o igual que el valor del final")
    print("Los numeros divisibles por 3 en el rango ingresado son:")
    for i in range(inicio, final + 1):
        if i % 3 == 0:
            print(i)


def irAOpcion(opcion):
    match opcion:
        case "a":
            sumaNaturales()
        case "b":
            encontrarDivisiblesXTres()
        case "c":
            print("Saliendo del programa")
            exit()


if __name__ == "__main__":
    while True:
        opcion = menu()
        irAOpcion(opcion)
