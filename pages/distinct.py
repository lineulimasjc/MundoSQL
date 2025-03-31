import streamlit as st

# st.image("img/file.png")

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
st.write("⚠️ Usaremos o mesmo [contexto](%s) do comando ```SELECT```." % url)


st.text("")

st.subheader("💡 Exemplo:", anchor=False)

code = '''
SELECT DISTINCT(estado)
FROM Clientes;
'''
st.code(code, language="sql")

st.write("🎯 **Resultado:**")

st.markdown("""
| **estado** |
|------------|
|     SP     |
|     RJ     |
|     MG     |
|     PR     |
|     RS     |
""")

st.write("📝 O ```DISTINCT``` remove os valores duplicados da coluna selecionada.")


