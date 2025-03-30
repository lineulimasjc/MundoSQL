import streamlit as st

st.image("img/select2.png")

st.title("📌 SELECT", anchor=False)

st.write("O comando ```SELECT ... FROM ...``` no SQL é usado para consultar dados de uma tabela.")

st.write("Duas palavras-chave são essenciais: ```SELECT``` (selecionar) e ```FROM``` (de), indicando quais **colunas** desejamos recuperar e de qual **tabela**.")

st.write("Sintaxe básica:")

code = '''
SELECT coluna1, coluna2, colunaN
FROM tabela;
'''
st.code(code, language="sql")


st.divider()


st.subheader("📖 Contexto", anchor=False)

st.write("Para ilustrar o exemplo apresentado, considere a seguinte tabela:")

st.write("Tabela **Alunos**")

st.markdown("""
| **RA** |  **Nome** | **Idade** |
|:------:|:---------:|-----------|
|   1    |   Maria   |     25    |
|   2    |    José   |     30    |
|   3    |    Ana    |     27    |
|   4    |    João   |     23    |
|   5    | Francisco |     25    |
""")

st.text("")

st.write("🗂️ **Script SQL** para criação do ambiente:")

code = '''
CREATE TABLE Alunos (
  ra      INT,
  nome    CHAR(30),
  idade   INT
)

INSERT INTO Alunos VALUES
  (1, "Maria", 25),
  (2, "José", 30),
  (3, "Ana", 27),
  (4, "João", 23),
  (5, "Francisco", 25)
'''
st.code(code, language="sql")


st.divider()

st.subheader("💡 Exemplo 1:")

code = '''
SELECT *
FROM Alunos;
'''
st.code(code, language="sql")

st.write("🎯 **Resultado:**")

st.markdown("""
| **ra** |  **nome** | **idade** |
|:------:|:---------:|-----------|
|   1    |   Maria   |     25    |
|   2    |    José   |     30    |
|   3    |    Ana    |     27    |
|   4    |    João   |     23    |
|   5    | Francisco |     25    |
""")


st.write("📝 Retorna todos os dados da tabela Alunos, exibindo todas as **colunas** e **linhas**.")

st.divider()

st.write("⚠️ **Diferença de nomenclatura:**")

st.write("**Linha** → Termo mais comum no dia a dia.")

st.write("**Registro** → Muito usado no contexto de sistemas e aplicações.")

st.write("**Tupla** → Termo mais técnico, vindo da teoria dos bancos de dados relacionais.")

st.write("Então, na prática, dizer que **linha = registro = tupla** está correto! 🚀")

st.divider()

st.subheader("💡 Exemplo 2:")

code = '''
SELECT nome, idade
FROM Alunos;
'''
st.code(code, language="sql")

st.write("🎯 **Resultado:**")

st.markdown("""
|  **nome** | **idade** |
|:---------:|-----------|
|   Maria   |     25    |
|    José   |     30    |
|    Ana    |     27    |
|    João   |     23    |
| Francisco |     25    |
""")

st.write("📝 Retorna apenas as colunas **nome** e **idade** da tabela **Alunos**, exibindo os dados dessas colunas para todos os registros.")
