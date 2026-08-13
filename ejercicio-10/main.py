from biblioteca.modelos.libro import Libro
import biblioteca.servicios.prestamo as prestamo

if __name__ == "__main__":
    libro = Libro("Hola mundo!", "Computex", "Alguien", True)

    print(prestamo.consultarDisponibilidad(libro))

    print(prestamo.realizarPrestamo(libro))

    print(prestamo.consultarDisponibilidad(libro))

    print(prestamo.realizarPrestamo(libro))

    print(prestamo.realizarDevolucion(libro))

    print(prestamo.realizarDevolucion(libro))
    