import os

todolist = ["arrumar a casa", "ajeitar site do canil"]

def userCli():
    os.system("cls") or None
    i = 0
    if len(todolist) == 0:
        print("Nenhuma tarefa no momento.")
    else:
        while i < len(todolist):
            print(f"{[i+1]} | {todolist[i]}")
            i += 1
    userInput()

def userInput():
    userOpt = int(input("\n1 - Adicionar tarefa | 2 - Remover tarefa | 3 - Sair\n>> "))

    match userOpt:
        case 1:
            addToList = input("Digite o nome da tarefa\n>> ")
            todolist.append(addToList)
            userCli()
        case 2:
            if len(todolist) == 0:
                userCli()
            else:
                removeFromList = int(input("Digite o número da tarefa a ser excluida.\n>> "))
                todolist.pop(removeFromList-1)
                userCli()
        case 3:
            print("Até logo")

userCli()