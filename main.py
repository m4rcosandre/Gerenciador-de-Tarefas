import json
import os

ARQUIVOS_DADOS = "tarefas.json"
tarefas = []


def carregar_tarefas():
    global tarefas

    # verifica se o arquivo existe
    if os.path.exists(ARQUIVOS_DADOS):
        try:
            with open(ARQUIVOS_DADOS, "r") as file:
                tarefas = json.load(file)
            print("Tarefas carregadas com sucesso")
        except Exception as ex:
            print(f"Erro ao carregar dados : {ex}. Iniciando lista vazia")
            tarefas = []

# Função para adicionar tarefa


def nova_tarefa(descricao):
    nova_tarefa = {
        "descricao": descricao,
        "concluida": False
    }
    tarefas.append(nova_tarefa)
    print(f"tarefa {descricao} add com sucesso")


def salvar_tarefas():
    with open(ARQUIVOS_DADOS, "w") as file:
        json.dump(tarefas, file, indent=4)
    print(f"Tarefas salvas em {ARQUIVOS_DADOS}")


def listar_tarefas():
    if not tarefas:
        print("A lista de tarefas está vazia!")
        return
    print("\n --SUAS TAREFAS--")
    for i, t in enumerate(tarefas):
        status = "[x]" if t["concluida"] else "[ ]"
        print(f"{i + 1}. {status} {t['descricao']}")


def concluir_tarefa(indice_str):
    # 1. Tenta converter a entrada para um número inteiro
    try:
        # Subtraímos 1 para transformar o número amigável (1, 2, 3...) no índice real da lista (0, 1, 2...)
        indice = int(indice_str) - 1
    except ValueError:
        print("Erro: Por favor, digite um NÚMERO válido para concluir a tarefa.")
        return

    # 2. Verifica se a lista está vazia
    if not tarefas:
        print("A lista de tarefas está vazia.")
        return

    # 3. Verifica se o índice está dentro dos limites da lista
    # O índice deve ser maior ou igual a 0 E menor que o tamanho da lista (len(tarefas))
    if 0 <= indice < len(tarefas):

        # Se for válido, acessa a tarefa
        tarefa = tarefas[indice]

        # 4. Altera o status para True
        tarefa["concluida"] = True
        print(
            f"Tarefa '{tarefa['descricao']}' marcada como CONCLUÍDA com sucesso!")
    else:
        # Se o índice não existir (ex: a lista tem 3 itens e o usuário digitou 5)
        print(f"Erro: Índice '{indice_str}' inválido. A tarefa não existe.")


def remover_tarefa(indice_str):
    # 1. Tenta converter a entrada do usuário para inteiro e ajusta para o índice da lista
    try:
        indice = int(indice_str) - 1
    except ValueError:
        print("Erro: Por favor, digite um NÚMERO válido para remover a tarefa.")
        return

    # 2. Verifica se o índice está dentro dos limites da lista
    if 0 <= indice < len(tarefas):

        # 3. Usa pop() para remover e obter a tarefa removida
        tarefa_removida = tarefas.pop(indice)

        print(f"Tarefa '{tarefa_removida['descricao']}' removida com sucesso!")
    else:
        print(
            f"Erro: Índice '{indice_str}' inválido. A tarefa não existe para ser removida.")


def menu():
    while True:
        print("\n---- Gerenciador de Tarefas ---")
        print("1. Add tarefas")
        print("2. Listar Tarefas")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("5. Sair e Salvar")

        escolha = input('Digite a descrição da sua tarefa: ')

        if escolha == "1":
            descricao = input('Digite a sua tarefa aqui.')
            nova_tarefa(descricao)
        elif escolha == "2":
            listar_tarefas()
        elif escolha == "3":
            # Primeiro, listamos as tarefas para o usuário ver os números
            listar_tarefas()

            if tarefas:  # Só pede input se houver tarefas
                indice_para_concluir = input(
                    "Digite o NÚMERO da tarefa para CONCLUIR: ")
                concluir_tarefa(indice_para_concluir)
        elif escolha == "4":
            listar_tarefas()
            if tarefas:
                indice_para_remover = input(
                    "Digite o NÚMERO da tarefa para REMOVER: ")
                remover_tarefa(indice_para_remover)
        elif escolha == "5":
            salvar_tarefas()
            print("Muito obrigado! Saindo.")
            break
        else:
            print("Opção inválida! Tente novamente.")


# Isso garante que a função comece quando o script é executado
if __name__ == "__main__":
    carregar_tarefas()
    menu()
