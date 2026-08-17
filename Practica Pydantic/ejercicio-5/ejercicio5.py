from pydantic import BaseModel, Field, HttpUrl, ValidationError
from typing import Annotated, Optional, Union

class PerfilUsuario(BaseModel):
    username: Annotated[str, Field(pattern = r"^[a-z0-9_]{3,20}$")]
    biografia: Optional[Annotated[str, Field(max_length=200)]] = None
    redesSociales: Optional[list[Union[str,HttpUrl]]] = None

if __name__ == "__main__":
    try:
        print("Usuario 1: Error en username")
        u1 = PerfilUsuario(username="TobiasSabbione")
    except ValidationError as e:
        print(e)

    try:
        print("\nUsuario 2: Error en biografia")
        u2 = PerfilUsuario(username="tobiassabbione", biografia="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    except ValidationError as e:
        print(e)

    try:
        print("\nUsuario 3: Instancia correcta")
        u3 = PerfilUsuario(username="tobiassabbione", biografia="Alumno de Desarrollo de Software", redesSociales=["@tobi", "https://github.com/TobiSeba"])
        print(f"Username: {u3.username} | Biografia: {u3.biografia} | Redes Sociales: {u3.redesSociales}")
    except ValidationError as e:
        print(e)