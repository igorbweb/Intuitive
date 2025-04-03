from fastapi import FastAPI, Query
import pandas as pd
from typing import List
import os

app = FastAPI()

path = os.getcwd()

CSV_PATH = os.path.join(path, "3. SQL", "Relatorio_cadop.csv")

if os.path.exists(CSV_PATH):
    df = pd.read_csv(CSV_PATH, delimiter=";", dtype=str)
else:
    df = pd.DataFrame()

@app.get("/")
def home():
    return "Interactive Care"

@app.get("/operadoras/")
async def buscar_operadoras(q: str = Query(..., min_length=3)):
    """Busca operadoras pelo Nome Fantasia, Razão Social ou CNPJ."""
    if df.empty:
        return {"error": "Nenhum dado carregado"}

    resultados = df[df.apply(lambda row: row.astype(str).str.contains(q, case=False, na=False).any(), axis=1)]
    return resultados.to_dict(orient="records")