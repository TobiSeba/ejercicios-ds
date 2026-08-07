import sys

def ejercicio2(palabra):
    print("¡Hola " + palabra.capitalize() + "!")

if __name__ == "__main__":
    palabra = sys.argv[1]
    ejercicio2(palabra)

