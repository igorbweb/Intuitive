import requests
from bs4 import BeautifulSoup
import os
import re
import zipfile

url_base = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'
site_base = 'https://www.gov.br'

scripts_folder = os.path.dirname(os.path.realpath(__file__))

zip_path = os.path.join(scripts_folder, "anexos.zip")

response = requests.get(url_base)

arquivos = []

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    anexos = soup.find_all("a", string=re.compile("Anexo"))  

    for anexo in anexos:
        file_url = anexo.get("href")

        if file_url.lower().endswith(".pdf"):
            file_name = os.path.basename(file_url)
            file_path = os.path.join(scripts_folder, file_name)

            file_response = requests.get(file_url, stream=True)
            if file_response.status_code == 200:
                with open(file_path, "wb") as file:
                    for chunk in file_response.iter_content(chunk_size=8192):
                        file.write(chunk)
                    arquivos.append(file_path)
                    print(f"Download concluído: {file_name}")
            else:
                    print(f"Falha no Download: {file_name}")
                    print(f"{file_url}")
else:
    print(f'Erro ao acessar {url_base}, status code: {response.status_code}')


if arquivos:
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for pdf in arquivos:
            zipf.write(pdf, arcname=os.path.basename(pdf))

    print(f"Arquivos compactados em {zip_path}")

else:
    print("Nenhum PDF baixado")