1. Scraping:

Este script automatiza o processo de extração e download de anexos no formato PDF disponíveis na página da Agência Nacional de Saúde Suplementar (ANS) sobre atualização do Rol de Procedimentos.

Acessa a página oficial da ANS e faz uma requisição HTTP para obter o conteúdo;
Analisa o HTML utilizando a biblioteca BeautifulSoup para localizar links de anexos nomeados com "Anexo";
Filtra e baixa apenas arquivos PDF, salvando-os no diretório do script;
Compacta os arquivos baixados em um ZIP, se houver downloads bem-sucedidos;
Exibe mensagens de status, indicando downloads concluídos ou possíveis falhas.

Tecnologias Utilizadas
Python 3;
Requests (requisição HTTP);
BeautifulSoup (extração de dados HTML);
Zipfile

Certifique-se de ter o Python instalado e execute:
pip install -r requirements.txt

---------------------------------------------------------------------------

2. Transform:

Este script automatiza a extração de tabelas de um documento PDF utilizando Tabula, processa os dados e os exporta para formatos estruturados (CSV e Excel). Ao final, os arquivos são compactados em um ZIP, conforme solicitado.

Lê um arquivo PDF contendo tabelas a partir do diretório de scraping;
Extrai tabelas das páginas 3 a 181 utilizando a técnica de detecção por grid (lattice);
Concatena todas as tabelas extraídas em um único DataFrame;
Limpa e normaliza os dados, removendo valores nulos, espaços extras e renomeando colunas específicas;
Salva os dados tratados em formatos CSV e Excel;
Compacta os arquivos extraídos em um arquivo ZIP.

Python 3
Tabula (extração de tabelas de PDFs)
Pandas
Zipfile

Certifique-se de ter o Python instalado e execute:
pip install -r requirements.txt

*Obs.: Para esse script é necessário ter o Java instalado para o funcionamento da lib Tabula, caso ainda não possua certifique-se de fazer o Download da versão mais recente: https://www.java.com/pt-BR/download/

---------------------------------------------------------------------------

3. SQL:

Este conjunto de scripts SQL cria e popula tabelas relacionadas a dados de operadoras de planos de saúde e suas movimentações contábeis.

Criação de Tabelas
tabela_empresas: Contém informações cadastrais das operadoras de planos de saúde, incluindo CNPJ, nome, endereço, representante e região de comercialização.
2023 e 2024: Armazenam dados contábeis das operadoras, como código de conta, descrição e valores de saldo inicial e final.
Os dados são carregados a partir dos arquivos CSV especificados

MySQL

Certifique-se de ter um banco de dados MySQL configurado.
Execute os scripts SQL para criar as tabelas.
Utilize os comandos LOAD DATA INFILE para importar os arquivos CSV.
Confirme a importação utilizando consultas SELECT.

---------------------------------------------------------------------------

4. API:

Esta API foi desenvolvida com FastAPI para fornecer uma interface simples e eficiente para consulta de operadoras de planos de saúde cadastradas na Agência Nacional de Saúde Suplementar (ANS).

Recursos da API
Consulta geral: Retorna todos os registros disponíveis.
Busca por filtros específicos: Registro ANS, CNPJ, cidade, estado (UF) e modalidade.
Busca avançada: Permite a combinação de múltiplos filtros para uma pesquisa refinada.
Resposta estruturada em JSON.
CORS habilitado para permitir acesso de qualquer origem.

FastAPI (framework para desenvolvimento da API).
JSON (armazenamento dos dados).
CORS Middleware (permite chamadas de diferentes origens).

Instale as dependências:
pip install fastapi uvicorn

Execute a API:
uvicorn main:app --reload

Acesse a documentação interativa:
http://127.0.0.1:8000/docs

---------------------------------------------------------------------------

5. VUE:

Além da API em FastAPI, este projeto inclui uma interface web desenvolvida com Vue.js para facilitar a consulta das operadoras de saúde cadastradas na ANS.

Formulário para pesquisa com múltiplos filtros: Registro ANS, CNPJ, Cidade, UF e Modalidade.
Exibição de resultados em cartões responsivos.
Integração direta com a API para consumo dos dados.
Feedback visual para o usuário em caso de erro ou carregamento de dados.


Vue.js 3
Axios (Consumo da API)
TailwindCSS

Instalar Dependências

Caso ainda não tenha, instale o Vue CLI:
npm install -g @vue/cli

Depois, dentro do diretório do projeto, instale as dependências:
npm install

Configurar a URL da API
Crie um arquivo .env na raiz do projeto frontend e adicione:

VITE_API_URL=http://{SEU_LOCALHOST}/
Isso garante que a aplicação se comunique com a API localmente.


Para iniciar o servidor de desenvolvimento:
npm run dev

O frontend estará disponível em http://{SEU_LOCALHOST}/
