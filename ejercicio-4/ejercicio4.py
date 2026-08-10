def pedirTemperatura():
    while True:
        try:
            grados = float(input("Ingrese la temperatura: "))
            return grados
        except ValueError:
            print("ERROR: Por favor ingrese un valor numerico")
            continue

def pedirEscala():
    while True:
        escala = input("Ingrese la escala de temperatura (C para Celsius, F para Fahrenheit): ").upper()
        if escala == "C" or escala == "F":
            return escala
        else:
            print("ERROR: Por favor ingrese una escala valida (C o F)")

def convertirACelsius(grados):
    return (grados - 32) * 5/9

def convertirAFahrenheit(grados):
    return (grados * 9/5) + 32

def ejercicio4():
    temperatura = pedirTemperatura()
    escala = pedirEscala()
    if escala == "C":
        temperaturaFinal = convertirAFahrenheit(temperatura)
        print(f"La temperatura original en Celcius es: {temperatura}°C")
        print(f"La temperatura en Fahrenheit es: {temperaturaFinal}°F")
    else:
        temperaturaFinal = convertirACelsius(temperatura)
        print(f"La temperatura original en Fahrenheit es: {temperatura}°F")
        print(f"La temperatura en Celsius es: {temperaturaFinal}°C")

if __name__ == "__main__":
    ejercicio4()