from biblioteca.modelos.libro import Libro

def realizarPrestamo(libro):
    if libro.disponible:
        libro.disponible = False
        return f"Se ha realizado el prestamo del libro {libro.titulo} correctamente"
    else:
        return f"El libro {libro.titulo} no esta disponible"

def realizarDevolucion(libro):
    if libro.disponible:
        return f"El libro {libro.titulo} no puede ser devuelto ya que esta disponible"
    else:
        libro.disponible = True
        return f"Se ha devuelto el libro {libro.titulo} correctamente"

def consultarDisponibilidad(libro):
    if libro.disponible:
        return f"Estado del libro {libro.titulo}: Disponible"
    else:
        return f"Estado del libro {libro.titulo}: No disponible"