# Dicionarios -> armazenam valores em pares chave:valor
# Dicionarios são mutáveis, ou seja, podem ser alterados
# Dicionarios não permitem chaves duplicadas, ou seja, cada chave deve ser única
# Dicionarios são representados por chaves {}
# Apartir de Python 3.7, os dicionários mantêm a ordem de inserção dos itens


dicionario = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo',
    'profissao': 'Engenheiro',
    'profissao': 'Médico'  # Chave duplicada, o valor 'Médico' irá sobrescrever 'Engenheiro'
}

print(dicionario) # Imprime o dicionário completo
print(dicionario['nome'])  # Acessando o valor da chave 'nome'

print(len(dicionario))  # Imprime o número de itens no dicionário (4, pois a chave 'profissao' foi sobrescrita)

#valores podem ser de qualquer tipo, inclusive outros dicionários
dicionario_complexo = {
    'nome': 'Maria',
    'idade': 25,
    'hobbies': ['leitura', 'viagem', 'culinária'],
    'endereco': {
        'rua': 'Rua A',
        'numero': 123,
        'cidade': 'Rio de Janeiro'
    }
}
print('-'*30)
print(dicionario_complexo)  # Imprime o dicionário complexo
print(dicionario_complexo['hobbies'][2])  # Acessando o terceiro hobby
print(dicionario_complexo['endereco']['cidade'])  # Acessando a cidade do endereço
print(type(dicionario_complexo))  # Imprime o tipo do dicionário (dict)

# usnado dict para criar um dicionário
print('-'*30)
dicionario2 = dict(nome='Carlos', idade=40, cidade='Belo Horizonte', profissao='Advogado')
print(dicionario2)  # Imprime o dicionário criado com dict

# existem 4 tipos de dados de coletação em Python: listas, tuplas, conjuntos e dicionários
# listas -> ordenadas, mutáveis e permitem elementos duplicados
# tuplas -> ordenadas, imutáveis e permitem elementos duplicados
# conjuntos -> não ordenados, mutáveis e não permitem elementos duplicados
# dicionários -> não ordenados, mutáveis e não permitem chaves duplicadas