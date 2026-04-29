# para trabalhar com arquivos usa-se a função open()
# open() retorna um objeto de arquivo, que tem métodos para ler e escrever arquivos.
# "r" -> modo de leitura ( padrão)
# "w" -> modo de escrita
# "a" -> modo de append
# "x" -> modo de criação
# "b" -> modo binário
# "t" -> modo texto

# Exemplo de uso:
import os # -> módulo para manipulação de arquivos e diretórios
path = os.path.dirname(__file__) # -> retorna o diretório do arquivo atual, garantindo que o caminho seja correto independentemente de onde o script seja executado

arquivo = open(path + "/exemplo.txt")
conteudo = arquivo.read()
print(conteudo)
arquivo.close() # -> é importante fechar o arquivo após usá-lo para liberar recursos do sistema

with open(path + "/exemplo.txt") as arquivo:
    for x in arquivo:
        print(x)

# Escrevendo em um arquivo existente

# "a" -> modo de append, adiciona conteúdo ao final do arquivo sem apagar o conteúdo existente
# "w" -> modo de escrita, apaga o conteúdo existente e escreve o novo conteúdo

with open(path + "/exemplo.txt", "a") as arquivo:
    arquivo.write("Adicionando uma nova linha ao arquivo.\n")

with open(path + "/exemplo.txt") as arquivo:
    print(arquivo.read())

with open(path + "/exemplo.txt", "r") as arquivo:
    with open(path + "/copia_exemplo.txt", "w") as copia:
        for linha in arquivo:
            copia.write(linha)

with open(path + "/exemplo.txt", "w") as arquivo:
    arquivo.write("Este é um novo conteúdo, o conteúdo anterior foi apagado.\n")

with open(path + "/exemplo.txt") as arquivo:
    print(arquivo.read())

with open(path + "/copia_exemplo.txt") as copia:
    print(copia.read())