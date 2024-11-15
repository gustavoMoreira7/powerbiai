from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
import uvicorn
import classPowerBi as c
import pandas as pd
import os

app = FastAPI()


TOKEN_OPENAI = os.getenv('TOKEN_OPENAI')

@app.get("/")
async def read_root():
    return {"Hello": """
            
        \n\n

        Essa é a API responsavel pela extratificação de dados da empresa Embrapa\n\n
        Não esqueça de verificar todos os EndPoints em nossa documentação...
                    
        \n\n """}

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204) 


@app.get('/askdata/{ask}')
async def ProductionExtract(ask: str):

    df = pd.read_excel("Data/vendedores.xlsx", index_col=False)
    dfString = df.to_string(index=False)

    conection = c.ConectionOnOpenAiExtractInformation(TOKEN_OPENAI,dfString,ask)

    resp = conection.userAsk(ask)

    return {"response": resp}