from pydantic import BaseModel, Field, EmailStr
from typing import Annotated

class Estudiante(BaseModel):
    legajo: Annotated[int, Field(gt = 0)]
    nombreCompleto: Annotated[str, Field(min_length=5)]
    email: EmailStr
    promedio: Annotated[float, Field(ge=0.0, le=10.0, default=0.0)] # Como deberia hacer el default?

if __name__ == "__main__":
    #e1 = Estudiante(legajo=-1, nombreCompleto="Tobias", email="algunmail@gmail.com", promedio=4.2)

    #e2 = Estudiante(legajo=4, nombreCompleto="Tobi", email="algunmail@gmail.com", promedio=4.2)

    #e3 = Estudiante(legajo=3, nombreCompleto="Tobias", email="algunmailgmail.com", promedio=4.2)

    #e4 = Estudiante(legajo=3, nombreCompleto="Tobias", email="algunmail@gmail.com", promedio=-32.3)

    e5 = Estudiante(legajo=3, nombreCompleto="Tobias", email="algunmail@gmail.com", promedio=4.2)
