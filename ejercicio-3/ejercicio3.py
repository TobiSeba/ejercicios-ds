
def ejercicio3():
    costoEstimadoPasaje = input("Ingrese el costo estimado del pasaje: ")
    costoAlojamientoXNoche = input("Ingrese el costo estimado del alojamiento por noche: ")
    cantidadNoches = input("Ingrese la cantidad de noches que durara el viaje: ")
    dineroDisponible = input("Ingrese la cantidad de dinero disponible: ")
    costoTotalViaje = (float(costoEstimadoPasaje) + (float(costoAlojamientoXNoche) * int(cantidadNoches)))

    if costoTotalViaje <= float(dineroDisponible):
        esSuficiente = True
    else:
        esSuficiente = False

    print(f"El costo estimado del pasaje es: ${costoEstimadoPasaje}")
    print(f"El costo de alojamiento por noche es: ${costoAlojamientoXNoche}")
    print(f"La cantidad de noches que durara el viaje es: {cantidadNoches}")
    print(f"El costo total del viaje es: ${costoTotalViaje}")
    print(f"El dinero disponible es: ${dineroDisponible}")
    print(f"El dinero disponible es suficiente para pagar el viaje: {esSuficiente}")

if __name__ == "__main__":
    ejercicio3()