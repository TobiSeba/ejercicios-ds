from pydantic import BaseModel, Field, EmailStr, ValidationError
from typing import Annotated

class UsuarioSistema(BaseModel):
    email: EmailStr
    nivelAcceso: Annotated[int, Field(ge = 1, le = 5)]

if __name__ == "__main__":
    try:
        #u1 = UsuarioSistema(email = "algo@gmail.com", nivelAcceso = 6.4)
        u2 = UsuarioSistema(email = "algogmail.com", nivelAcceso = 5)
    except ValidationError as e:
        print(e)
    