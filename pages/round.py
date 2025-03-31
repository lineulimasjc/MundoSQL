import streamlit as st

# st.image("img/file.png")

st.title("📌 ROUND", anchor=False)

st.write("O comando ```ROUND``` é usado para **arredondar** um valor numérico para um número específico de casas decimais.")

st.write("Sintaxe:")

code = '''
SELECT ROUND(valor, numero_de_casas)
FROM tabela;
'''
st.code(code, language="sql")


st.divider()


url = "https://mundosql.streamlit.app/select"
st.write("⚠️ Usaremos o mesmo [contexto](%s) do comando ```SELECT```." % url)


st.text("")

st.subheader("💡 Exemplo:", anchor=False)

code = '''
SELECT ROUND(AVG(lim_cred), 2)
FROM Clientes;
'''
st.code(code, language="sql")

st.write("🎯 **Resultado:**")

st.markdown("""
| **ROUND(AVG(lim_cred), 2)** |
|-----------------------------|
|           5021.43           |
""")

st.write("📝 O comando ```ROUND``` arredonda um valor numérico para um número específico de casas decimais.")
