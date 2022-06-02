from unicodedata import name
from uuid import UUID
from fastapi import FastAPI
from models import Provider
from typing import List
from urls import url_provider_expedia, url_provider_jumbo
import requests

app = FastAPI()

db: List[Provider] = [
    Provider(
        provider_id="1",
        name='Expedia', 
        code='EXP', 
        url=url_provider_expedia
    ),
    Provider(
        provider_id="2",
        name='Jumbo', 
        code='JMB', 
        url=url_provider_jumbo
    )
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
async def fetch_avail():
    provider_exp = await fetch_provider_exp()
    provider_jmb = await fetch_provider_jmb()

    for k,v in provider_exp.items():
        for y in v:
            y['provider'] = Provider.provider_id
            print(y)
        #print(k,v)

    print('----')
    #for k, v in provider_jmb.items():
    #    print(k, v)

    #print('JMB')
    #print(provider_jmb)
    #print('----')

    
    #print('EXP')
    #print(provider_exp)
    #print('----')

    #db: List[Options] = [
    #    Options(
    #        provider_id="1",
    #        name='Expedia', 
    #        code='EXP', 
    #        url=url_provider_expedia
    #    )
    #]



    #result = provider_jmb.update(provider_exp)
    #print('--------')
    #print(provider_jmb)
    #for avails in provider_jmb:
    #    print(provider_jmb['avails'])

    #print('--------')
    ##print(results)
    #for k,v in results.items():
    #    print(k, v)
    ##print(results['rates'])
    #print('--------')

    r = requests.get(url_provider_jumbo)
    return r.json()



