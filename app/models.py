from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, field_validator


class Genre(str, Enum):
    ROCK = "Rock"
    POP = "Pop"
    RAP = "Rap"
    JAZZ = "Jazz"
    CLASSIQUE = "Classique"
    ELECTRO = "Electro"
    REGGAE = "Reggae"


class AlbumCreate(BaseModel):
    titre: str = Field(min_length=1)
    artiste: str
    genre: Genre
    annee: int = Field(ge=1900, le=datetime.now().year)
    note: float = Field(ge=0, le=10)

    @field_validator("titre")
    @classmethod
    def titre_ne_doit_pas_etre_vide(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Le titre ne peut pas être vide")
        return value


class AlbumResponse(AlbumCreate):
    id: int


class Token(BaseModel):
    access_token: str
    token_type: str
