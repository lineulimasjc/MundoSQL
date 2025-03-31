import streamlit as st

# st.image("img/file.png")

st.title("📌 AVG", anchor=False)

st.write("O comando ```AVG``` é usado para calcular a **média** dos valores em uma coluna numérica.")

st.write("Sintaxe:")

code = '''
SELECT AVG(nome_da_coluna)
FROM nome_da_tabela;
'''
st.code(code, language="sql")


st.divider()


url = "https://mundosql.streamlit.app/select"
st.write("⚠️ Usaremos o mesmo [contexto](%s) do comando ```SELECT```." % url)


st.text("")

st.subheader("💡 Exemplo:", anchor=False)

code = '''
SELECT AVG(lim_cred)
FROM Clientes;
'''
st.code(code, language="sql")

st.write("🎯 **Resultado:**")

st.markdown("""
| **AVG(lim_cred)** |
|-------------------|
|       1400        |
""")

st.write("📝 O comando ```AVG``` calcula a **média** dos valores em uma coluna numérica.")
