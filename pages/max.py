import streamlit as st

# st.image("img/file.png")

st.title("📌 MAX", anchor=False)

st.write("O comando ```MAX``` é usado para retornar o **maior** valor de uma coluna em um conjunto de registros.")

st.write("Sintaxe:")

code = '''
SELECT MAX(nome_da_coluna)
FROM nome_da_tabela;
'''
st.code(code, language="sql")


st.divider()


url = "https://mundosql.streamlit.app/select"
st.write("⚠️ Usaremos o mesmo [contexto](%s) do comando ```SELECT```." % url)


st.text("")

st.subheader("💡 Exemplo:", anchor=False)

code = '''
SELECT MAX(lim_cred)
FROM Clientes;
'''
st.code(code, language="sql")

st.write("🎯 **Resultado:**")

st.markdown("""
| **MAX(lim_cred)** |
|-------------------|
|       8500        |
""")

st.write("📝 O comando ```MAX``` retorna o **maior** valor de uma coluna em um conjunto de registros.")