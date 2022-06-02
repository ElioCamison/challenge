from unicodedata import name
from fastapi import FastAPI
from models import Provider
from typing import List
from urls import url_provider_expedia, url_provider_jumbo
import requests

app = FastAPI()

db: List[Provider] = [
    Provider(name='Expedia', code='EXP', url=url_provider_expedia),
    Provider(name='Jumbo', code='JMB', url=url_provider_jumbo)
]

@app.get("/api/v1/providers")
def fetch_providers():
    """
        End for get the all proveider
    """
    return db


@app.get("/api/v1/provider-exp")
async def fetch_provider_exp():
    r = requests.get(url_provider_expedia)
    return r.json()


@app.get("/api/v1/provider-jmb")
async def fetch_provider_jmb():
    r = requests.get(url_provider_jumbo)
    return r.json()


@app.get("/api/v1/avail")
async def fetch_provider_jmb():
    results = await fetch_provider_exp()
    print('--------')
    print(results)
    print('--------')

    r = requests.get(url_provider_jumbo)
    return r.json()



