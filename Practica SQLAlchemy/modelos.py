from sqlalchemy import create_engine, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime
from typing import List, Optional


engine = create_engine("sqlite:///ejerciciosSQLAlchemy.db", echo=False)

class Base(DeclarativeBase):
    pass

class Profesor(Base):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(40))
    email: Mapped[str] = mapped_column(String(60))
    fechaIngreso: Mapped[datetime] = mapped_column(DateTime)

    departamentoId: Mapped[Optional[int]] = mapped_column(ForeignKey("departamentos.id"))
    departamento: Mapped[Optional["Departamento"]] = relationship(back_populates="profesores")

    cursos: Mapped[List["Curso"]] = relationship(back_populates="profesor")


class Departamento(Base):
    __tablename__ = "departamentos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(40))
    profesores: Mapped[List["Profesor"]] = relationship(back_populates="departamento")


class Curso(Base):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(40))
    creditos: Mapped[int] = mapped_column(Integer)

    profesorId: Mapped[Optional[int]] = mapped_column(ForeignKey("profesores.id"))
    profesor: Mapped[Optional["Profesor"]] = relationship(back_populates="cursos")

    clases: Mapped[List["Clase"]] = relationship(back_populates="curso")

    inscripciones: Mapped[List["Inscripcion"]] = relationship(back_populates="curso")
    estudiantes: Mapped[List["Estudiante"]] = relationship(secondary="inscripciones", back_populates="cursos", viewonly=True)

class Clase(Base):
    __tablename__ = "clases"

    id: Mapped[int] = mapped_column(primary_key=True)
    tema: Mapped[str] = mapped_column(String(60))
    duracionMinutos: Mapped[int] = mapped_column(Integer)

    cursoId: Mapped[int] = mapped_column(ForeignKey("cursos.id"))
    curso: Mapped["Curso"] = relationship(back_populates="clases")

class Estudiante(Base):
    __tablename__ = "estudiantes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(40))
    legajo: Mapped[int] = mapped_column(Integer)

    inscripciones: Mapped[List["Inscripcion"]] = relationship(back_populates="estudiante")
    cursos: Mapped[List["Curso"]] = relationship(secondary="inscripciones", back_populates="estudiantes", viewonly = True)

class Inscripcion(Base):
    __tablename__ = "inscripciones"

    estudianteId: Mapped[int] = mapped_column(ForeignKey("estudiantes.id"), primary_key=True)
    cursoId: Mapped[int] = mapped_column(ForeignKey("cursos.id"), primary_key=True)

    fechaInscripcion: Mapped[datetime] = mapped_column(DateTime)
    calificacionFinal: Mapped[Optional[int]] = mapped_column(Integer)

    estudiante: Mapped["Estudiante"] = relationship(back_populates="inscripciones")
    curso: Mapped["Curso"] = relationship(back_populates="inscripciones")


"""

"""