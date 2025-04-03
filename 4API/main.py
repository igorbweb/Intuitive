from fastapi import FastAPI, Query, HTTPException
import pandas as pd
from typing import List
import os
import json


app = FastAPI()

JSON_PATH = os.path.join(os.path.dirname(__file__), "Relatorio_cadop.json")
@app.get("/")
def home():
    if not os.path.exists(JSON_PATH):
        raise HTTPException(status_code=404, detail="Arquivo JSON não encontrado")
    
    try:
        df = pd.DataFrame
        df = pd.read_csv(JSON_PATH, delimiter=";", dtype=str)

        df = df.where(pd.notna(df), None)

        if df.empty:
            return {"message": "Nenhum dado encontrado no JSON"}
        
        return df.to_dict(orient="records")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar JSON: {str(e)}")
    
@app.get("/registro/{registro_ans}")
def get_registro(registro_ans: str):
    if not os.path.exists(JSON_PATH):
        raise HTTPException(status_code=404, detail="Arquivo JSON não encontrado")

    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise HTTPException(status_code=500, detail="Formato inválido no JSON")

        registro_ans = registro_ans.strip()
        resultado = [item for item in data if str(item.get("Registro_ANS", "")).strip() == registro_ans]

        if not resultado:
            raise HTTPException(status_code=404, detail=f"Registro {registro_ans} não encontrado")

        return resultado

    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Erro ao carregar o JSON: Formato inválido")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar JSON: {str(e)}")