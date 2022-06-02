from uuid import UUID
from ast import Str
from typing import List
from pydantic import BaseModel, HttpUrl


class Provider(BaseModel):
    provider_id: int
    name: str
    code: str
    url: HttpUrl

class Options(BaseModel):
    options_id: int
    hotel: int
    nights: int
    final_price: int
    provider: int

class Hotel(BaseModel):
    hotel_id: int
    options: List[Options]


class Available(BaseModel):
    available_id: int
    hotel: List[Hotel]