import streamlit as st

st.title("SELECT")

# st.write("O comando ```SELECT ... FROM``` no SQL é usado para consultar dados de uma tabela.")


st.write("Para que servem os comandos SQL? Um dos usos mais comuns é a seleção de dados em uma tabela dentro de um banco de dados. Para isso, duas palavras-chave são essenciais: SELECT (selecionar) e FROM (de), indicando quais colunas desejamos recuperar e de qual tabela.")

st.write("Sintaxe básica:")

code = '''
SELECT coluna1, coluna2
FROM tabela;
'''
st.code(code, language="sql")

st.write("Para ilustrar o exemplo apresentado, considere a seguinte tabela:")


st.write("Tabela **Alunos**")

st.markdown("""
| **RA** |  **Nome** | **Idade** |
|:------:|:---------:|-----------|
|   001  |   Maria   |     25    |
|   002  |    José   |     30    |
|   003  |    Ana    |     27    |
|   004  |    João   |     23    |
|   005  | Francisco |     25    |
""")


code = '''
SELECT *
FROM Alunos;
'''
st.code(code, language="sql")

st.write("Retornar todos os dados da tabela Alunos, exibindo todas as colunas e registros.")


code = '''
SELECT Nome, Idade
FROM Alunos;
'''
st.code(code, language="sql")

st.write("Retornar apenas as colunas **nome** e **idade** da tabela **Alunos**, exibindo os dados dessas colunas para todos os registros.")





