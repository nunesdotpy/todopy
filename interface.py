from os import system, listdir
from time import sleep
import tasks

# importando as tasks salvas
todolist = tasks.todolist
newTasks = []
completedTasks = []


def userCli():
    system("clear") or None
    i = 0
    if len(todolist) == 0:
        print("Nenhuma tarefa no momento.")
    else:
        if todolist[i] in completedTasks:
            return    
        else:
            for task in todolist:
                print(f"[{i+1}] | {task}")
                i += 1
    if len(completedTasks) == 0:
        print("\n--\n\nNenhuma tarefa completa no momento.")
    else:
        for completedTask in completedTasks:
            print(f"[{i+1}] | {completedTask}")
    userInput()

def userInput():
    userOpt = int(input("\n1 - Adicionar tarefa | 2 - Remover tarefa | 3 - Sair\n>> "))

    match userOpt:
        case 1:
            addToList = input("Digite o nome da tarefa\n>> ")
            tasks.createTask(addToList)
            todolist.append(f"\n{addToList}")
            userCli()
        case 2:
            if len(todolist) == 0:
                userCli()
            else:
                removeFromList = int(input("Digite o número da tarefa a ser excluida.\n>> "))
                todolist.pop(removeFromList-1)
                tasks.removeTask(removeFromList-1)
                userCli()
                print(f"{todolist[removeFromList-1]}")
        case 3:
            print("Até logo")

userCli()