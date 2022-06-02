from uuid import UUID
from ast import Str
from typing import List
from pydantic import BaseModel, HttpUrl


class Provider(BaseModel):
    proveider_id: UUID
    name: str
    code: str
    url: HttpUrl

class Options(BaseModel):
    options_id: UUID
    hotel: int
    nights: int
    final_price: int
    provider: int

class Hotel(BaseModel):
    hotel_id: UUID
    options: List[Options]


class Available(BaseModel):
    available_id: UUID
    hotel: List[Hotel]