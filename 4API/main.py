from fastapi import FastAPI, Query, HTTPException
import pandas as pd
from typing import List
import os
import json


app = FastAPI()

JSON_PATH = os.path.join(os.path.dirname(__file__), "Relatorio_cadop.json")

def carregar_dados():
    if not os.path.exists(JSON_PATH):
        raise HTTPException(status_code=404, detail="Arquivo JSON não encontrado")

    with open(JSON_PATH, "r", encoding="utf-8") as file:
        return json.load(file)
    
@app.get("/")
def home():
    dados = carregar_dados()
    
    if not dados:
        raise HTTPException(status_code=404, detail="Nenhum dado encontrado")
    
    return {"total_registros": len(dados), "dados": dados}
    
@app.get("/registro/{registro_ans}")
def get_registro(registro_ans: str):
    dados = carregar_dados()
    
    resultado = [item for item in dados if item["Registro_ANS"].strip() == registro_ans.strip()]
    
    if not resultado:
        raise HTTPException(status_code=404, detail=f"Registro {registro_ans} não encontrado")

    return resultado

@app.get("/cnpj/{cnpj}")
def get_cnpj(cnpj: str):
    dados = carregar_dados()
    
    resultado = [item for item in dados if item["CNPJ"].strip() == cnpj.strip()]
    
    if not resultado:
        raise HTTPException(status_code=404, detail=f"CNPJ {cnpj} não encontrado")

    return resultado

@app.get("/cidade/{cidade}")
def get_cidade(cidade: str):
    dados = carregar_dados()
    
    resultado = [item for item in dados if item["Cidade"].strip().lower() == cidade.strip().lower()]
    
    if not resultado:
        raise HTTPException(status_code=404, detail=f"Nenhuma operadora encontrada na cidade {cidade}")

    return resultado

@app.get("/uf/{uf}")
def get_uf(uf: str):
    dados = carregar_dados()
    
    resultado = [item for item in dados if item["UF"].strip().upper() == uf.strip().upper()]
    
    if not resultado:
        raise HTTPException(status_code=404, detail=f"Nenhuma operadora encontrada no estado {uf}")

    return resultado

@app.get("/modalidade/{modalidade}")
def get_modalidade(modalidade: str):
    dados = carregar_dados()
    
    resultado = [item for item in dados if item["Modalidade"].strip().lower() == modalidade.strip().lower()]
    
    if not resultado:
        raise HTTPException(status_code=404, detail=f"Nenhuma operadora encontrada na modalidade {modalidade}")

    return resultado