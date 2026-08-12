temperaturas = [25.4, 52.1, 92.5, -4.9, 5.0, 32.3]

def promedioLista(lista):
    return sum(lista) / len(lista)

def analizar_temperaturas(registros):
    maximo = max(registros)
    minimo = min(registros)
    promedio = promedioLista(registros)
    tuplaTemperaturas = (maximo, minimo, promedio)

    return tuplaTemperaturas

if __name__ == "__main__":
    temperaturaMaxima, temperaturaMinima, promedioTemperatura = analizar_temperaturas(temperaturas)
    print(f"Lista original de temperaturas: {temperaturas}")
    print(f"Temperatura maxima: {temperaturaMaxima}°")
    print(f"Temperatura minima: {temperaturaMinima}°")
    print(f"Promedio de temperatura: {promedioTemperatura}°")