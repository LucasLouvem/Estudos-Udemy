import os

os.makedirs("projeto_temporario", exist_ok=True)
if not os.path.exists("projeto_temporario/tarefas.txt"):
    with open("projeto_temporario/tarefas.txt", "w") as file:
        pass

path = os.path.join("projeto_temporario", "tarefas.txt")

def adicionar_tarefa(nome, descricao):
    with open(path, "r") as file:
        
        maior_id = 0

        with open(path, "a") as f:
            for linha in f:
                if linha.strip():
                    tarefa_atual = eval(linha.strip())
                    id_atual = tarefa_atual.get("id", 0)
                    if id_atual > maior_id:
                        maior_id = id_atual
        novo_id = maior_id + 1
        nova_tarefa = {
            "id": novo_id,
            "nome": nome,
            "descricao": descricao,
            "concluido": False
        }
        file.write(str(nova_tarefa) + "\n")

def apagar_tarefa(id_tarefa):
    with open(path, "r") as file:
        tarefas = file.readlines()
    with open(path, "w") as file:
        for tarefa in tarefas:
            tarefa_dict = eval(tarefa.strip())
            if int(id_tarefa) != tarefa_dict.get("id"):
                file.write(tarefa)
            else:
                print(f"Tarefa com ID '{id_tarefa}' apagada com sucesso!")

def concluir_tarefa(id_tarefa):
    with open(path, "r") as file:
        tarefas = file.readlines()
    with open(path, "w") as file:
        for tarefa in tarefas:
            if id_tarefa in tarefa:
                tarefa_dict = eval(tarefa.strip())
                tarefa_dict["concluido"] = True
                file.write(str(tarefa_dict) + "\n")
                print(f"Tarefa com ID '{id_tarefa}' marcada como concluída!")
            else:
                file.write(tarefa)

def listar_tarefas():
    with open(path, "r") as file:
        tarefas = file.readlines()
        for tarefa in tarefas:
            print(tarefa.strip())

def main():
    while True:
        print("Gerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Apagar Tarefa")
        print("3. Listar Tarefas")
        print("4. Concluir Tarefa")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome_tarefa = input("Digite o nome da tarefa: ")
            descricao_tarefa = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(nome_tarefa, descricao_tarefa)
            print("Tarefa adicionada com sucesso!")
        elif escolha == "2":
            print("Tarefas disponíveis:")
            listar_tarefas()
            id_tarefa = input("Digite o ID da tarefa a ser apagada: ")
            apagar_tarefa(id_tarefa)
        elif escolha == "3":
            listar_tarefas()
        elif escolha == "4":
            print("Tarefas disponíveis:")
            listar_tarefas()
            id_tarefa = input("Digite o ID da tarefa a ser concluída: ")
            concluir_tarefa(id_tarefa)
        elif escolha == "5":
            print("Saindo do gerenciador de tarefas.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()