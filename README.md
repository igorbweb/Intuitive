# Guia de Implementação do Projeto

## Scraping

Este script automatiza o processo de extração e download de anexos em PDF disponíveis na página oficial da Agência Nacional de Saúde Suplementar (ANS) sobre a atualização do Rol de Procedimentos.

### Funcionalidades:
- *Requisição HTTP* para acessar o conteúdo da página oficial da ANS.
- *Análise HTML* com BeautifulSoup para localizar links de anexos nomeados como "Anexo".
- *Download de arquivos PDF*: Filtra e baixa apenas os arquivos em formato PDF.
- *Compactação em ZIP*: Caso haja downloads bem-sucedidos, os arquivos são compactados em um único arquivo ZIP.
- *Mensagens de status*: Indica o progresso e eventuais falhas durante o processo de download.

### Tecnologias Utilizadas:
- Python 3
- Requests (para requisição HTTP)
- BeautifulSoup (para extração de dados HTML)
- Zipfile (para compactação de arquivos)

### Instalação:
Certifique-se de ter o Python instalado. Em seguida, instale as dependências:
bash
pip install -r requirements.txt


---

## Transform

Este script automatiza a extração de tabelas de um documento PDF utilizando a biblioteca Tabula, processa os dados e os exporta para formatos estruturados (CSV e Excel).

### Funcionalidades:
- *Leitura de PDF*: Lê o arquivo PDF contendo tabelas extraídas no processo de scraping.
- *Extração de tabelas*: Utiliza a técnica de detecção por grid (lattice) para extrair tabelas das páginas 3 a 181.
- *Limpeza e normalização*: Remove valores nulos, espaços extras e renomeia colunas específicas.
- *Exportação*: Salva os dados tratados em formatos CSV e Excel.
- *Compactação em ZIP*: Os arquivos exportados são compactados em um arquivo ZIP.

### Tecnologias Utilizadas:
- Python 3
- Tabula (extração de tabelas de PDFs)
- Pandas (manipulação de dados)
- Zipfile (compactação de arquivos)

### Instalação:
Certifique-se de ter o Python instalado. Em seguida, instale as dependências:
bash
pip install -r requirements.txt


*Observação: A biblioteca **Tabula* depende do *Java*. Caso ainda não tenha o Java instalado, faça o download da versão mais recente [aqui](https://www.java.com/pt-BR/download/).

---

## SQL

Este conjunto de scripts SQL cria e popula tabelas relacionadas a dados de operadoras de planos de saúde e suas movimentações contábeis.

### Funcionalidades:
- *Criação de Tabelas*:
  - tabela_empresas: Contém informações cadastrais das operadoras de planos de saúde, como CNPJ, nome, endereço, representante e região de comercialização.
  - 2023 e 2024: Armazenam dados contábeis das operadoras, como código de conta, descrição e valores de saldo inicial e final.
- *Importação de Dados*: Os dados são carregados a partir de arquivos CSV específicos.

### Tecnologias Utilizadas:
- MySQL

### Instalação:
- Certifique-se de ter um banco de dados MySQL configurado.
- Execute os scripts SQL para criar as tabelas.
- Use o comando LOAD DATA INFILE para importar os arquivos CSV.
- Confirme a importação utilizando consultas SELECT.

---

## API

Esta API foi desenvolvida com *FastAPI* para fornecer uma interface simples e eficiente para consulta de operadoras de planos de saúde cadastradas na ANS.

### Funcionalidades:
- *Consulta Geral*: Retorna todos os registros disponíveis.
- *Busca por Filtros*: Filtros para consulta por Registro ANS, CNPJ, cidade, estado (UF) e modalidade.
- *Busca Avançada*: Permite a combinação de múltiplos filtros para uma pesquisa refinada.
- *Resposta em JSON*: Os dados são retornados de forma estruturada.
- *CORS*: Habilitado para permitir acesso de qualquer origem.

### Tecnologias Utilizadas:
- FastAPI (framework para desenvolvimento da API)
- JSON (armazenamento dos dados)
- CORS Middleware (permite chamadas de diferentes origens)

### Instalação:
Instale as dependências:
bash
pip install fastapi uvicorn


### Execução:
Inicie o servidor da API com o comando:
bash
uvicorn main:app --reload


Acesse a documentação interativa da API em:
[http://{SEU_LOCALHOST}/docs](http://{SEU_LOCALHOST}/docs)

---

## Frontend - Vue.js

O frontend deste projeto é uma interface web desenvolvida com *Vue.js*, permitindo consulta interativa às operadoras de saúde cadastradas na ANS.

### Funcionalidades:
- *Formulário de Pesquisa*: Permite pesquisa com múltiplos filtros, como Registro ANS, CNPJ, cidade, UF e modalidade.
- *Exibição de Resultados*: Exibe os resultados da pesquisa em cartões responsivos.
- *Integração com a API*: Consome dados diretamente da API FastAPI.
- *Feedback Visual*: Mostra mensagens de erro ou status durante o carregamento dos dados.

### Tecnologias Utilizadas:
- Vue.js 3
- Axios (para consumo da API)
- TailwindCSS (para estilização)

### Instalação:
- Caso ainda não tenha, instale o Vue CLI:
  bash
  npm install -g @vue/cli
  
- Em seguida, instale as dependências do projeto:
  bash
  npm install

  
### Configuração:
Crie um arquivo .env na raiz do projeto e adicione a URL da API:
plaintext
VITE_API_URL=http://{SEU_LOCALHOST}/


### Execução:
Inicie o servidor de desenvolvimento:
bash
npm run dev


O frontend estará disponível em:  
[http://{SEU_LOCALHOST}/](http://{SEU_LOCALHOST}/)


![image](https://github.com/user-attachments/assets/b04b5c68-ae43-43a6-84eb-537444d4a880)
