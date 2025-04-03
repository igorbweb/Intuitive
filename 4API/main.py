from fastapi import FastAPI, Query, HTTPException
import pandas as pd
from typing import List
import os

app = FastAPI()

CSV_PATH = os.path.join(os.path.dirname(__file__), "Relatorio_cadop.csv")
@app.get("/")
def home():
    try:
        df = pd.read_csv(CSV_PATH, delimiter=";", dtype=str)

        df = df.where(pd.notna(df), None)

        if df.empty:
            return {"message": "Nenhum dado encontrado no CSV"}
        
        return df.to_dict(orient="records")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar CSV: {str(e)}")