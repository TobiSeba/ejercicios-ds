from pydantic import BaseModel, Field, EmailStr, ValidationError
from typing import Annotated, Optional, Union, Literal

TIPO = Literal["Sensor", "Actuador", "Gateway"]

class Dispositivo(BaseModel):
    idDispositivo: Union[int, str]
    tipo: TIPO

if __name__ == "__main__":
    d1 = Dispositivo(idDispositivo=100, tipo="Sensor")
    print(d1.idDispositivo)
    d1.idDispositivo = "Cien"
    print(d1.idDispositivo)

    print()

    try:
        d2 = Dispositivo(idDispositivo=3.2, tipo="Actuador")
    except ValidationError as e:
        print(e)

    print()

    try:
        d3 = Dispositivo(idDispositivo=2, tipo="alguno")
    except ValidationError as e:
        print(e)
