import streamlit as st

# st.image("img/file.png")

st.title("📌 ORDER BY", anchor=False)

st.write("A cláusula ```ORDER BY``` é usada para **ordenar os resultados** de uma consulta SQL com base em uma ou mais colunas.")


st.write("Sintaxe:")

code = '''
SELECT coluna1, coluna2, colunaN
FROM tabela
ORDER BY coluna1 [ASC | DESC];
'''
st.code(code, language="sql")


st.divider()


url = "https://mundosql.streamlit.app/select"
st.write("⚠️ Usaremos o mesmo [contexto](%s) do comando ```SELECT```." % url)


st.text("")

st.subheader("💡 Exemplo 1:", anchor=False)

code = '''
SELECT nome, fone, cidade
FROM Clientes
WHERE lim_cred >= 5000
ORDER BY nome;
'''
st.code(code, language="sql")

st.write("🎯 **Resultado:**")

st.markdown("""
|    **nome**    |    **fone**    |   **cidade**   |
|:--------------:|:--------------:|:--------------:|
|João Silva		 |11987654321     |São Paulo       |
|Pedro Santos	 |51943210987	  |Porto Alegre    |
|Rafael Costa	 |21921098765	  |Niterói         |
""")

st.write("📝 A consulta retorna os campos ```nome```, ```fone``` e ```cidade``` de clientes com limite de crédito ≥ 5000, **ordenando** os resultados pelo **nome**, em ordem **crescente** (```ASC```).")


st.divider()


st.write("⚠️ Por **padrão**, a ordenação é feita em **ordem crescente** (```ASC```), ou seja, do menor para o maior ou de A a Z. Para exibir os dados em **ordem decrescente**, é necessário **especificar explicitamente** usando a palavra-chave ```DESC``` na consulta.")


st.divider()




st.subheader("💡 Exemplo 2:", anchor=False)

code = '''
SELECT nome, fone, cidade
FROM Clientes
WHERE lim_cred >= 5000
ORDER BY nome DESC;
'''
st.code(code, language="sql")

st.write("🎯 **Resultado:**")

st.markdown("""
|    **nome**    |    **fone**    |   **cidade**   |
|:--------------:|:--------------:|:--------------:|
|Rafael Costa	 |21921098765	  |Niterói         |
|Pedro Santos	 |51943210987	  |Porto Alegre    |
|João Silva		 |11987654321     |São Paulo       |
""")

st.write("📝 A consulta retorna os campos ```nome```, ```fone``` e ```cidade``` de clientes com limite de crédito ≥ 5000, **ordenando** os resultados pelo **nome**, em ordem **decrescente** (```DESC```).")

st.divider()




st.subheader("💡 Exemplo 3:", anchor=False)

code = '''
SELECT nome, estado, cidade
FROM Clientes
ORDER BY estado ASC, cidade DESC;
'''
st.code(code, language="sql")

st.write("🎯 **Resultado:**")

st.markdown("""
|    **nome**    | **estado**     | **cidade**     |
|:--------------:|:--------------:|:--------------:|
|Carlos Souza	|MG	|Belo Horizonte |
|Ana Pereira	|PR	|Curitiba |
|Maria Oliveira	|RJ	|Rio de Janeiro |
|Rafael Costa	|RJ	|Niterói |
|Pedro Santos	|RS	|Porto Alegre |
|João Silva		|SP	|São Paulo |
|Lucia Ferreira	|SP	|Campinas |
""")

st.write("📝 A consulta retorna os campos ```nome```, ```estado``` e ```cidade``` da tabela **Clientes**, **ordenando** os resultados pelo **estado**, em ordem **crescente** (```ASC```) e pela **cidade**, em ordem **decrescente** (```DESC```).")
