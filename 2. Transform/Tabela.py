import tabula
import pandas as pd
import os
import zipfile
import acesso

# Caminho do arquivo PDF
path = os.getcwd()
parent = os.path.dirname(path)

scripts_folder = os.path.dirname(os.path.realpath(__file__))
pdf_path = os.path.join(path, "1. Scraping", acesso.file_name)

lista_tabelas = tabula.read_pdf(pdf_path, pages="3-181", lattice=True)

df_final = lista_tabelas[0]

for tabela in lista_tabelas[1:]:
    df_final = pd.concat([df_final, tabela.iloc[1:]], ignore_index=True)
    
df_final.dropna(how="all", inplace=True)

df_final = df_final.apply(lambda x: x.astype(str).str.replace(r"\s+", " ", regex=True).str.strip())

df_final.rename(columns={'OD': 'Seg. Odontológica', 'AMB': 'Seg. Ambulatorial'}, inplace=True)

df_final.replace({
    'OD': 'Seg. Odontológica',
    'AMB': 'Seg. Ambulatorial',
}, inplace=True)

print(df_final)

csv_path = os.path.join(scripts_folder, "dados_extraidos.csv")
excel_path = os.path.join(scripts_folder, "dados_extraidos.xlsx")
zip_path = os.path.join(scripts_folder, "Teste_Igor_Bomfim.zip")

df_final.to_csv(csv_path, index=False, encoding="utf-8", quotechar='"', sep=";", lineterminator='\n')
df_final.to_excel(excel_path, index=False, engine='openpyxl')

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(csv_path, os.path.basename(csv_path))
    zipf.write(excel_path, os.path.basename(excel_path))
print(f"Arquivos compactados em {zip_path}")