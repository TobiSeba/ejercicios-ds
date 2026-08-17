from sqlalchemy import select, func
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from modelos import engine, Base, Profesor, Departamento, Curso, Clase, Estudiante, Inscripcion
from datetime import datetime

Base.metadata.create_all(engine)

def ejercicio1():
    with Session(engine) as session:
        profe1 = Profesor(nombre="Pepito Flowers", email="pepitoflowers@gmail.com", fechaIngreso=datetime.now())
        session.add(profe1)
        session.commit()
    
        profe2 = Profesor(nombre="Antonio Rivaldo", email="antoniorivaldo@gmail.com", fechaIngreso=datetime.now())
        session.add(profe2)
        session.commit()
    
        stmt = select(Profesor)     
        for p in session.scalars(stmt):
            print(f"Profesor ID: {p.id} | Nombre: {p.nombre} | Email: {p.email} | Fecha de ingreso: {p.fechaIngreso}")

def ejercicio2y3():
    with Session(engine) as session:
        profe1 = Profesor(nombre="Pepito Flowers", email="pepitoflowers@gmail.com", fechaIngreso=datetime.now())
        profe2 = Profesor(nombre="Antonio Rivaldo", email="antoniorivaldo@gmail.com", fechaIngreso=datetime.now())
        profe3 = Profesor(nombre="Jose Martinez", email="jmartinez@gmail.com", fechaIngreso=datetime.now())
        session.add(profe1)
        session.add(profe2)
        session.add(profe3)
        session.commit()
    
        departamento1 = Departamento(nombre="Departamento de Informatica")
        departamento1.profesores = [profe1, profe2, profe3]
        session.add(departamento1)
        session.commit()
    
        stmt = select(Profesor)
        print("Profesores:")
        for p in session.scalars(stmt):
            if p.departamento:
                nombreDepartamento = p.departamento.nombre
            else:
                nombreDepartamento = "Ninguno"
            print(f"ID: {p.id} | Nombre: {p.nombre} | Email: {p.email} | Fecha de ingreso: {p.fechaIngreso} | Departamento: {nombreDepartamento}")
    
        stmt2 = select(Departamento)
        print("Departamentos:")
        for d in session.scalars(stmt2):
            nombresProfes = []
            for p in d.profesores:
                nombresProfes.append(p.nombre)
            print(f"ID: {d.id} | Nombre: {d.nombre} | Profesores: {nombresProfes}")

def ejercicio4():
    with Session(engine) as session:
        profe1 = Profesor(nombre="Pepito Flowers", email="pepitoflowers@gmail.com", fechaIngreso=datetime.now())
        session.add(profe1)
        session.commit()

        curso1 = Curso(titulo="Curso 1", creditos=5)
        curso2 = Curso(titulo="Curso 2", creditos=2)

        curso1.profesor = profe1
        curso2.profesor = profe1
        session.add(curso1)
        session.add(curso2)
        session.commit()

        stmt = select(Curso)
        print("Cursos:")
        for c in session.scalars(stmt):
            print(f"Titulo: {c.titulo} | Creditos: {c.creditos} | Profesor: {c.profesor.nombre}")


def ejercicio5():
    with Session(engine) as session:
        curso1 = Curso(titulo="Curso 1", creditos=5)
        session.add(curso1)
        session.commit()

        clase1 = Clase(tema="Tema 1", duracionMinutos=5)
        clase2 = Clase(tema="Tema 2", duracionMinutos=50)
        curso1.clases = [clase1, clase2]
        session.add(clase1)
        session.add(clase2)
        session.commit()
        
        stmt = select(Curso).where(Curso.titulo == "Curso 1")
        curso = session.scalars(stmt).first()
        print(f"Clases del curso: {curso.titulo}")
        for clase in curso.clases:
            print(f"Tema: {clase.tema} | Duracion en minutos: {clase.duracionMinutos}")


def ejercicio6y7():
    with Session(engine) as session:
        e1 = Estudiante(nombre="Tobias Sabbione", legajo = 1000)
        e2 = Estudiante(nombre="Jose Messi", legajo = 1001)

        curso1 = Curso(titulo="Curso 1", creditos=5)
        curso2 = Curso(titulo="Curso 2", creditos=5)

        ins1 = Inscripcion(fechaInscripcion=datetime.now())
        ins2 = Inscripcion(fechaInscripcion=datetime.now())
        ins3 = Inscripcion(fechaInscripcion=datetime.now())
        ins4 = Inscripcion(fechaInscripcion=datetime.now())
        
        ins1.estudiante = e1
        ins1.curso = curso1
        ins2.estudiante = e1
        ins2.curso = curso2

        ins3.estudiante = e2
        ins3.curso = curso1
        ins4.estudiante = e2
        ins4.curso = curso2
        
        session.add_all([ins1, ins2, ins3, ins4])
        session.commit()

        stmt = select(Inscripcion)
        print("Inscripciones:")
        for i in session.scalars(stmt):
            print(f"Estudiante: {i.estudiante.nombre} | Curso: {i.curso.titulo} | Fecha de inscripcion: {i.fechaInscripcion} | Calificacion final: {i.calificacionFinal}")

def ejercicio8():
    with Session(engine) as session:
        # Creo las instancias
        curso1 = Curso(titulo="Curso 1", creditos=5)
        curso2 = Curso(titulo="Curso 2", creditos=5)
        curso3 = Curso(titulo="Curso 3", creditos=5)

        profe1 = Profesor(nombre="Pepito Flowers", email="pepitoflowers@gmail.com", fechaIngreso=datetime.now())
        e1 = Estudiante(nombre="Tobias Sabbione", legajo = 1000)
        e2 = Estudiante(nombre="Jose Messi", legajo = 1001)

        ins1 = Inscripcion(fechaInscripcion=datetime.now())
        ins2 = Inscripcion(fechaInscripcion=datetime.now())
        ins3 = Inscripcion(fechaInscripcion=datetime.now()) # Estas 3 son del e1

        ins4 = Inscripcion(fechaInscripcion=datetime.now())
        ins5 = Inscripcion(fechaInscripcion=datetime.now()) # Estas 2 son del e2

        # Relleno los valores necesarios para las consultas
        profe1.cursos = [curso1, curso2, curso3]

        ins1.estudiante = e1
        ins2.estudiante = e1
        ins3.estudiante = e1
        ins1.curso = curso1
        ins2.curso = curso2
        ins3.curso = curso3

        ins4.estudiante = e2
        ins5.estudiante = e2
        ins4.curso = curso1
        ins5.curso = curso2
        
        ins1.calificacionFinal = 9
        ins2.calificacionFinal = 7
        ins3.calificacionFinal = 8

        session.add_all([profe1, ins1, ins2, ins3, ins4, ins5])
        session.commit()

        # Primera consulta: Listar todos los cursos que dicta un profesor especifico usando join

        stmt = select(Curso).join(Profesor).where(Profesor.nombre == "Pepito Flowers")
        cursosDelProfe = session.scalars(stmt)
        print(f"Cursos que dicta el profesor: {profe1.nombre}")
        for c in cursosDelProfe:
            print(f"ID: {c.id} | Titulo: {c.titulo} | Creditos: {c.creditos}")

        # Segunda consulta: Obtener el promedio de calificaciones de un estudiante en particular utilizando funciones de agregacion (func.avg)
        stmt2 = select(func.avg(Inscripcion.calificacionFinal)).join(Estudiante).where(Estudiante.nombre == "Tobias Sabbione")
        promedio = session.scalar(stmt2)
        print(f"El promedio de calificaciones de {e1.nombre} es: {promedio}")

        # Tercera consulta: Contar cuantos estudiantes hay inscriptos en cada curso (func.count)
        stmt3 = select(Curso.titulo, func.count(Inscripcion.estudianteId)).join(Inscripcion).group_by(Curso.titulo) # No se si esta bien
        resultados = session.execute(stmt3) # Uso execute porque tiene 2 columnas
        for t, c in resultados:
            print(f"Curso: {t} | Cantidad de inscriptos: {c}")

def matricularAlumno(session, estudiante, curso):
    try:
        ins = Inscripcion(fechaInscripcion=datetime.now())
        ins.estudiante = estudiante
        ins.curso = curso

        session.add(ins)
        session.commit()
        print(f"Se matriculo al estudiante {estudiante.nombre} en el curso {curso.titulo}")
    except IntegrityError:
        session.rollback()
        print(f"ERROR: El estudiante {estudiante.nombre} ya esta matriculado en el curso {curso.titulo}")


def ejercicio9():
    with Session(engine) as session:
        curso1 = Curso(titulo="Curso 1", creditos=5)
        e1 = Estudiante(nombre="Tobias Sabbione", legajo = 1000)

        session.add_all([curso1, e1])
        session.commit()
        print("Matriculando al estudiante por primera vez")
        matricularAlumno(session, e1, curso1)

        print("\nMatriculando al estudiante por segunda vez para forzar excepcion")
        matricularAlumno(session, e1, curso1)

if __name__ == "__main__":
    #ejercicio1()
    #ejercicio2y3()
    #ejercicio4()
    #ejercicio5()
    #ejercicio6y7()
    #ejercicio8()
    ejercicio9()