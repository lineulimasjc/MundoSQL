import streamlit as st

# st.image("img/file.png")

st.title("📌 COUNT", anchor=False)

st.write("O comando ```COUNT``` em SQL é usado para contar o número de registros em uma tabela ou o número de valores não nulos em uma coluna.")

st.write("Sintaxe:")

code = '''
-- Conta todas as linhas da tabela
SELECT COUNT(*)
FROM tabela;

-- Conta apenas os valores não nulos da coluna
SELECT COUNT(coluna)
FROM tabela;
'''
st.code(code, language="sql")


st.divider()


url = "https://mundosql.streamlit.app/select"
st.write("⚠️ Usaremos o mesmo [contexto](%s) do comando ```SELECT```." % url)


st.text("")

st.subheader("💡 Exemplo:", anchor=False)

code = '''
SELECT COUNT(*)
FROM Clientes;
'''
st.code(code, language="sql")

st.write("🎯 **Resultado:**")

st.markdown("""
| **COUNT(*)** |
|--------------|
|       7      |
""")

st.write("📝 O comando ```COUNT``` conta o número de registros da tabela")