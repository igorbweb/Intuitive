import tabula
import pandas as pd
import os
import acesso

# Caminho do arquivo PDF
path = os.getcwd()

parent = os.path.dirname(path)
print("Parent directory", parent)
pdf_path = os.path.join(parent, "1. Scraping", acesso.file_name)
print(pdf_path)

# Abre o PDF
# lista_tabelas = tabula.read_pdf(pdf_path, pages="3-181")
# print(len(lista_tabelas))

# for tabela in lista_tabelas:
#     print(tabela)

# Converte para DataFrame
# df = pd.DataFrame(table[1:], columns=table[0])  # Define a primeira linha como cabeçalho

# Exibe o DataFrame
# print(df)
