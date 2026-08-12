CONTRASENIA_CORRECTA = "Admin1234"

def pedirContrasenia():
    contrasenia = input("Ingrese su contraseña: ")
    return contrasenia

def verificarContrasenia(contrasenia):
    return contrasenia == CONTRASENIA_CORRECTA

def ejercicio5b():
    intentos = 3
    while intentos > 0:
        contrasenia = pedirContrasenia()
        if verificarContrasenia(contrasenia):
            print("La contraseña es correcta")
            break
        else:
            intentos -= 1
            if intentos == 0:
                print("La contraseña es incorrecta. No te quedan intentos")
            else:    
                print(f"La contraseña es incorrecta. Te quedan {intentos} intentos")

if __name__ == "__main__":
    ejercicio5b()

