import streamlit as st

# st.image("img/file.png")

st.title("📌 WHERE", anchor=False)

st.write("O comando ```WHERE``` é usado para **filtrar** registros com base em uma **condição específica**. Ele permite selecionar apenas as linhas que atendem a critérios definidos.")


st.write("Sintaxe:")

code = '''
SELECT coluna1, coluna2, colunaN
FROM tabela
WHERE condição;
'''
st.code(code, language="sql")


st.divider()


url = "https://mundosql.streamlit.app/select"
st.write("⚠️ Usaremos o mesmo [contexto](%s) do comando ```SELECT```." % url)


st.text("")

st.subheader("💡 Exemplo 1:", anchor=False)

code = '''
SELECT nome, cidade
FROM Clientes
WHERE estado = 'SP';
'''
st.code(code, language="sql")

st.write("🎯 **Resultado:**")

st.markdown("""
|    **nome**    | **cidade**     |
|:--------------:|----------------|
|   João Silva   |    São Paulo   |
| Lucia Ferreira |    Campinas    |
""")

st.write("📝 O comando ```WHERE``` filtra os registros com base na condição informada.")


st.divider()


st.title("Operadores de Compração", anchor=False)

st.write("Os operadores de comparação em SQL são usados para comparar valores em condições ```WHERE```, ```HAVING```, ```JOIN``` e outras cláusulas.")



st.markdown("""
| **Operador** |   **Descrição**  |   **Exemplo**  |
|:------------:|:----------------:|:----------------:|
|   ```=```    |      igual a     | ```WHERE status = 1``` |
|   ```!=``` ou ```<>```   |   diferente de   | ```WHERE cidade <> 'São Paulo'``` |
|    ```>```   |     maior que    | ```WHERE lim_cred > 3500``` |
|   ```>=```   | maior ou igual a | ```WHERE lim_cred >= 3500``` |
|    ```<```   |     menor que    | ```WHERE lim_cred < 3500``` |
|   ```<=```   | menor ou igual a | ```WHERE lim_cred <= 3500'``` |
""")


st.divider()


st.subheader("💡 Exemplo 2:", anchor=False)

code = '''
SELECT *
FROM Clientes
WHERE lim_cred >= 5000;
'''
st.code(code, language="sql")

st.write("🎯 **Resultado:**")

st.markdown("""
| **id** |    **nome**    | **fone**    | **cidade**     | **estado** | **lim_cred** | **status** |
|:------:|:--------------:|-------------|----------------|------------|--------------|------------|
|    1   |   João Silva   | 11987654321 |    São Paulo   |     SP     |         8500 |      1     |
|    5   |  Pedro Santos  | 51943210987 |  Porto Alegre  |     RS     |         6500 |      1     |
|    7   |  Rafael Costa  | 21921098765 |     Niterói    |     RJ     |         8500 |      0     |
""")

st.write("📝 Essa consulta retorna todos os dados da tabela **Clientes**, filtrando apenas os registros onde o **limite de crédito** é **maior ou igual a 5000**.")
