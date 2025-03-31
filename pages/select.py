import streamlit as st

st.image("img/select2.png")

st.title("📌 SELECT", anchor=False)

st.write("O comando ```SELECT ... FROM ...``` no SQL é usado para consultar dados de uma tabela.")

st.write("Duas palavras-chave são essenciais: ```SELECT``` (selecionar) e ```FROM``` (de), indicando quais **colunas** desejamos recuperar e de qual **tabela**.")

st.write("Sintaxe:")

code = '''
SELECT coluna1, coluna2, colunaN
FROM tabela;
'''
st.code(code, language="sql")


st.divider()


st.subheader("📖 Contexto", anchor=False)

st.write("Para ilustrar o exemplo apresentado, considere a seguinte tabela:")

st.write("Tabela **Clientes**")

st.markdown("""
| **id** |    **nome**    | **fone**    | **cidade**     | **estado** | **lim_cred** | **status** |
|:------:|:--------------:|-------------|----------------|------------|--------------|------------|
|    1   |   João Silva   | 11987654321 |    São Paulo   |     SP     |         8500 |      1     |
|    2   | Maria Oliveira | 21976543210 | Rio de Janeiro |     RJ     |         3500 |      1     |
|    3   |  Carlos Souza  | 31965432109 | Belo Horizonte |     MG     |         1400 |      1     |
|    4   |   Ana Pereira  | 41954321098 |    Curitiba    |     PR     |         2000 |      0     |
|    5   |  Pedro Santos  | 51943210987 |  Porto Alegre  |     RS     |         6500 |      1     |
|    6   | Lucia Ferreira | 11932109876 |    Campinas    |     SP     |         4750 |      1     |
|    7   |  Rafael Costa  | 21921098765 |     Niterói    |     RJ     |         8500 |      0     |
""")

st.text("")

st.write("🗂️ **Script SQL** para criação do ambiente:")

code = '''
CREATE TABLE Clientes (
  id		INT,
  nome		CHAR(50),
  fone		CHAR(11),			-- Formato: "11912345678"
  cidade	CHAR(50),
  estado	CHAR(2),			-- Sigla (ex: "SP")
  lim_cred	NUMERIC,
  status 	BOOLEAN				-- Ativo = 1 | Inativo = 0
);

-- Inserindo 7 clientes fictícios
INSERT INTO Clientes (id, nome, fone, cidade, estado, lim_cred, status) VALUES
  (1, 'João Silva', '11987654321', 'São Paulo', 'SP', 8500.00, 1),
  (2, 'Maria Oliveira', '21976543210', 'Rio de Janeiro', 'RJ', 3500.00, 1),
  (3, 'Carlos Souza', '31965432109', 'Belo Horizonte', 'MG', 1400.00, 1),
  (4, 'Ana Pereira', '41954321098', 'Curitiba', 'PR', 2000.00, 0),
  (5, 'Pedro Santos', '51943210987', 'Porto Alegre', 'RS', 6500.00, 1),
  (6, 'Lucia Ferreira', '11932109876', 'Campinas', 'SP', 4750.00, 1),
  (7, 'Rafael Costa', '21921098765', 'Niterói', 'RJ', 8500.00, 0);
'''
st.code(code, language="sql")


st.divider()

st.subheader("💡 Exemplo 1:", anchor=False)

code = '''
SELECT *
FROM Clientes;
'''
st.code(code, language="sql")

st.write("🎯 **Resultado:**")

st.markdown("""
| **id** |    **nome**    | **fone**    | **cidade**     | **estado** | **lim_cred** | **status** |
|:------:|:--------------:|-------------|----------------|------------|--------------|------------|
|    1   |   João Silva   | 11987654321 |    São Paulo   |     SP     |         8500 |      1     |
|    2   | Maria Oliveira | 21976543210 | Rio de Janeiro |     RJ     |         3500 |      1     |
|    3   |  Carlos Souza  | 31965432109 | Belo Horizonte |     MG     |         1400 |      1     |
|    4   |   Ana Pereira  | 41954321098 |    Curitiba    |     PR     |         2000 |      0     |
|    5   |  Pedro Santos  | 51943210987 |  Porto Alegre  |     RS     |         6500 |      1     |
|    6   | Lucia Ferreira | 11932109876 |    Campinas    |     SP     |         4750 |      1     |
|    7   |  Rafael Costa  | 21921098765 |     Niterói    |     RJ     |         8500 |      0     |
""")


st.write("📝 Retorna todos os dados da tabela Clientes, exibindo todas as **colunas** e **linhas**.")

st.divider()

st.write("⚠️ **Diferença de nomenclatura:**")

st.write("**Linha** → Termo mais comum no dia a dia.")

st.write("**Registro** → Muito usado no contexto de sistemas e aplicações.")

st.write("**Tupla** → Termo mais técnico, vindo da teoria dos bancos de dados relacionais.")

st.write("Então, na prática, dizer que **linha = registro = tupla** está correto! 🚀")

st.divider()

st.subheader("💡 Exemplo 2:", anchor=False)

code = '''
SELECT nome, cidade
FROM Clientes;
'''
st.code(code, language="sql")

st.write("🎯 **Resultado:**")

st.markdown("""
|    **nome**    | **cidade**     |
|:--------------:|----------------|
|   João Silva   |    São Paulo   |
| Maria Oliveira | Rio de Janeiro |
|  Carlos Souza  | Belo Horizonte |
|   Ana Pereira  |    Curitiba    |
|  Pedro Santos  |  Porto Alegre  |
| Lucia Ferreira |    Campinas    |
|  Rafael Costa  |     Niterói    |
""")

st.write("📝 Retorna apenas as colunas **nome** e **cidade** da tabela **Clientes**, exibindo os dados dessas colunas para todos os registros.")
