from pydantic import EmailStr
from sqlmodel import SQLModel, Field

class UsuarioCreate(SQLModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8)

class UsuarioRead(SQLModel):
    id: int
    username: str
    email: str

class Token(SQLModel):
    access_token: str
    token_type: str
