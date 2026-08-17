from pydantic import BaseModel, Field, EmailStr, ValidationError
from typing import Annotated, Optional

CoordenadaGPS = Annotated[float, Field(ge=-90.0, le=90.0)]

class Ubicacion(BaseModel):
    longitud: CoordenadaGPS
    latitud: CoordenadaGPS
    etiqueta: Optional[str] = None

if __name__ == "__main__":
    u1 = Ubicacion(longitud = -90.0, latitud = 90.0)
    print("Ubicacion 1:")
    print(f"Longitud: {u1.longitud} | Latitud: {u1.latitud} | Etiqueta: {u1.etiqueta}")
    u1.etiqueta = "Algun lugar"
    print("\nUbicacion 1:")
    print(f"Longitud: {u1.longitud} | Latitud: {u1.latitud} | Etiqueta: {u1.etiqueta}")

    print()
    try:
        u2 = Ubicacion(longitud = 92.3, latitud = 23, etiqueta= "Otro lugar")
    except ValidationError as e:
        print(e)

    print()
    try:
        u3 = Ubicacion(longitud = 44.3, latitud = 92.3, etiqueta= "Otro lugar")
    except ValidationError as e:
        print(e)