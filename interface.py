from os import system, listdir, chdir, mkdir
import tasks

todolist = []

# Ler as categorias, caso não existe, exibir que não existe.
def categorys():
    if "categorys" in listdir():
        chdir("./categorys")
        if len(listdir()) == 0:
            print("\n--\n\nNenhuma categória existente no momento.")
        else:
            for category in listdir():
                print(f"\n--\n\n{category}")
    else:
        print("\n--\n\nNenhuma categória existente no momento.")
    chdir("./../")

# Principal interface do usuário.
def userCli():
    system("clear") or None
    i = 0
    if len(todolist) == 0:
        print("Nenhuma tarefa existente no momento.")
    else:
        while i < len(todolist):
            print(f"{[i+1]} | {todolist[i]}")
            i += 1
    # Mostrar as categorias.
    categorys()
    # Mostrar as opções de input para usuário.
    userInput()

def userInput():
    userOpt = int(input("\n1 - Adicionar tarefa | 2 - Remover tarefa | 3 - Acessar categoria | 4 - Criar nova categoria | 5 - Sair\n>> "))
    match userOpt:
        case 1:
            addToList = input("Digite o nome da tarefa\n>> ")
            tasks.createTask(addToList)
            userCli()
        case 2:
            if len(todolist) == 0:
                userCli()
            else:
                removeFromList = int(input("Digite o número da tarefa a ser excluida.\n>> "))
                todolist.pop(removeFromList-1)
                userCli()
        case 3:
            print("Não disponível no momento")
            userCli()
        case 4:
            newCategory = input("Digite o nome da categoria\n>> ")
            tasks.createCategory(newCategory)
            userCli()
        case 5:
            print("Até logo")

userCli()