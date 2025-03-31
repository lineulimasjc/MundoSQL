import streamlit as st

# st.image("img/file.png")

st.title("📌 SUM", anchor=False)

st.write("O comando ```SUM``` é usado para calcular a **soma** de todos os valores em uma coluna numérica.")

st.write("Sintaxe:")

code = '''
SELECT SUM(coluna)
FROM tabela;
'''
st.code(code, language="sql")


st.divider()


url = "https://mundosql.streamlit.app/select"
st.write("⚠️ Usaremos o mesmo [contexto](%s) do comando ```SELECT```." % url)


st.text("")

st.subheader("💡 Exemplo:", anchor=False)

code = '''
SELECT SUM(lim_cred)
FROM Clientes;
'''
st.code(code, language="sql")

st.write("🎯 **Resultado:**")

st.markdown("""
| **SUM(lim_cred)** |
|-------------------|
|      35150        |
""")

st.write("📝 O comando ```SUM``` calcula a soma de todos os valores em uma coluna numérica.")