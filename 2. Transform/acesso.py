import requests
from bs4 import BeautifulSoup
import os
import re

url_base = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'
site_base = 'https://www.gov.br'

response = requests.get(url_base)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    anexo = soup.find("a", string=re.compile("Anexo I"))  
    file_url = anexo.get("href")

    if file_url.lower().endswith(".pdf"):
        file_name = os.path.basename(file_url)
        file_response = requests.get(file_url, stream=True)