CREATE TABLE tabela_empresas (
    Registro_ANS VARCHAR(20),
    CNPJ VARCHAR(20),
    Razao_Social VARCHAR(255),
    Nome_Fantasia VARCHAR(255),
    Modalidade VARCHAR(255),
    Logradouro VARCHAR(255),
    Numero VARCHAR(20),
    Complemento VARCHAR(255),
    Bairro VARCHAR(255),
    Cidade VARCHAR(255),
    UF CHAR(2),
    CEP VARCHAR(10),
    DDD CHAR(2),
    Telefone VARCHAR(15),
    Fax VARCHAR(15),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(255),
    Regiao_de_Comercializacao VARCHAR(255),
    Data_Registro_ANS VARCHAR(10)
);

LOAD DATA INFILE 'C:/Users/igorj/OneDrive/Documentos/Code/Repositorios/Intuitive/3. SQL/Relatorio_cadop.csv'
INTO TABLE tabela_empresas
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(
    Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, 
    Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, 
    Endereco_eletronico, Representante, Cargo_Representante, Regiao_de_Comercializacao, 
    Data_Registro_ANS
);

SELECT * FROM tabela_empresas;