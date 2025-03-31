import streamlit as st

# st.image("img/file.png")

st.title("📌 MIN", anchor=False)

st.write("O comando ```MIN``` é usado para retornar o **menor** valor de uma coluna em um conjunto de registros.")

st.write("Sintaxe:")

code = '''
SELECT MIN(nome_da_coluna)
FROM nome_da_tabela;
'''
st.code(code, language="sql")


st.divider()


url = "https://mundosql.streamlit.app/select"
st.write("⚠️ Usaremos o mesmo [contexto](%s) do comando ```SELECT```." % url)


st.text("")

st.subheader("💡 Exemplo:", anchor=False)

code = '''
SELECT MIN(lim_cred)
FROM Clientes;
'''
st.code(code, language="sql")

st.write("🎯 **Resultado:**")

st.markdown("""
| **MIN(lim_cred)** |
|-------------------|
|       1400        |
""")

st.write("📝 O comando ```MIN``` retorna o **menor** valor de uma coluna em um conjunto de registros.")