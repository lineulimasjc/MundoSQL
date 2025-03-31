import streamlit as st

# st.image("img/select2.png")

st.title("📌 DISTINCT", anchor=False)

st.write("O comando SQL ```DISTINCT``` é usado para remover valores duplicados de um conjunto de resultados. Ele retorna apenas os valores únicos de uma ou mais colunas especificadas.")

st.write("Sintaxe:")

code = '''
SELECT DISTINCT(coluna1)
FROM tabela;
'''
st.code(code, language="sql")


st.divider()


url = "https://mundosql.streamlit.app/select"
st.write("Usaremos o mesmo [contexto](%s) do comando ```SELECT```." % url)

