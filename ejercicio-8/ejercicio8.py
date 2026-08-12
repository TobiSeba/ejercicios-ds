def calcularPrecioFinal(precioBase, porcentajeDescuento=10, esVip=False):
    if precioBase <= 0:
        raise ValueError("ERROR: El valor del precio base debe ser positivo")
    if porcentajeDescuento < 0:
        raise ValueError("ERROR: El porcentaje de descuento no puede ser negativo")

    descuento = precioBase * (porcentajeDescuento / 100)
    precioFinal = precioBase - descuento
    if esVip:
        precioFinal = precioFinal * 0.95
    return precioFinal

if __name__ == "__main__":
    precio = calcularPrecioFinal(10000, 33, False)
    print(precio)

    precio = calcularPrecioFinal(10000, 33, True)
    print(precio)

    #precio = calcularPrecioFinal(-2, 0, False)
    #print(precio)

    precio = calcularPrecioFinal(3134, -3, True)
    print(precio)