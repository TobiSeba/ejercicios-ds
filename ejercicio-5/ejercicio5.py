def pedirContrasenia():
    contrasenia = input("Ingrese una contraseña que tenga al menos 8 caracteres, una letra mayuscula y una minuscula: ")
    return contrasenia

def verificarContrasenia(contrasenia):
    if len(contrasenia) < 8:
        return False
    if not any(char.isupper() for char in contrasenia):
        return False
    if not any(char.islower() for char in contrasenia):
        return False
    return True

def ejercicio5():
    contrasenia = pedirContrasenia()
    if verificarContrasenia(contrasenia):
        print("La contraseña es valida")
    else:
        print("La contraseña no es valida, debe tener al menos 8 caracteres, una letra mayuscula y una letra minuscula")

if __name__ == "__main__":
    ejercicio5()