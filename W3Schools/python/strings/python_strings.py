# Strings em Python

print("Olá, mundo!")  # Imprime uma string simples
print('Python é incrível!')  # Imprime outra string usando aspas simples
print('-'*30)

# citação de aspas dentro de strings
print("Ele disse: 'Python é a melhor linguagem de todas!'")  # Usando aspas duplas para permitir aspas simples dentro da string
print('Ela respondeu: "Eu concordo, Python é ótimo!"')  # Usando aspas simples para permitir aspas duplas dentro da string
print('-'*30)

# atribuindo uma string a uma variável
mensagem = "Bem-vindo ao mundo da programação!"
print(mensagem)  # Imprime a mensagem armazenada na variável
print('-'*30)

#multilinhas
texto_multilinha = """Este é um texto
multilinha em Python.
Ele pode conter várias linhas de texto sem a necessidade de usar caracteres de nova linha."""
print(texto_multilinha)
print('-'*30)

# strings são matrizes, cada caractere tem um indice
palavra = "Python"
print(palavra[0])  # Imprime o primeiro caractere 'P'
print(palavra[1])  # Imprime o segundo caractere 'y'
print(palavra[-1])  # Imprime o último caractere 'n'
print(palavra[0:3])  # Imprime os primeiros três caracteres 'Pyt', o índice 3 não é incluído
print(palavra[3:6])  # Imprime os caracteres do quarto ao sexto 'hon', o índice 3 é incluído e o índice 6 não é incluído
print(palavra[:3])  # Imprime os primeiros três caracteres 'Pyt'
print('-'*30)

palavra = "Testando"
# looping através de uma string
for letra in palavra:
    print(letra)  # Imprime cada letra da palavra em uma linha separada
print('-'*30)

# verificando comprimento de uma string
print(len(palavra)) 
print('-'*30)

# verificando se uma substring está presente em uma string
print("ando está em 'Testando':", 'ando' in palavra)
print("Python está em 'Testando':", 'Python' in palavra)
print("Python não está em 'Testando':", 'Python' not in palavra)

txt = "Olá, mundo!"
if "mundo" in txt:
    print("A substring 'mundo' foi encontrada na string.")
else:    
    print("A substring 'mundo' não foi encontrada na string.")

print('-'*30)

