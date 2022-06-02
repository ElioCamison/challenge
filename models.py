from ast import Str
from pydantic import BaseModel, HttpUrl


class Provider(BaseModel):
    name: str
    code: str
    url: HttpUrl


class Avail(BaseModel):
    id: int
    name = 'Jane Doe'