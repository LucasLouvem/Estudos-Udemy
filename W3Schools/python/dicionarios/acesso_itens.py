# pode acessar os itens de um dicionário usando colchetes ou o método get()
# usando colchetes, se a chave não existir, será gerado um erro KeyError

dicionario = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo'
}
print(dicionario['nome'])  # Acessando o valor da chave 'nome'
# print(dicionario['profissao'])  # Acessando uma chave que não existe
x = dicionario.get('profissao')  # Usando get para acessar uma chave que não existe
print(x)  # Imprime None, pois a chave 'profissao' não existe
y = dicionario.get('profissao', 'Desconhecida')  # Usando get com valor padrão para chave que não existe
print(y)  # Imprime 'Desconhecida', pois a chave 'profissao' não existe e o valor padrão foi retornado

# adicionando ou atualizando itens em um dicionário
dicionario['profissao'] = 'Engenheiro'  # Adicionando um novo item ao dicionário
print(dicionario)  # Imprime o dicionário atualizado com a nova chave 'profissao'
dicionario['idade'] = 31  # Atualizando o valor da chave 'idade'
print(dicionario)  # Imprime o dicionário atualizado com a nova idade

# o metodo keys() retorna uma lista de todas as chaves do dicionário
chaves = dicionario.keys()
print(chaves)  # Imprime as chaves do dicionário
# o método values() retorna uma lista de todos os valores do dicionário
valores = dicionario.values()
print(valores)  # Imprime os valores do dicionário