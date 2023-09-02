
# Le o arquivo "main.txt" onde esta as tarefas, se não existir ele cria
try:
    with open("tasks.txt", "r", encoding="utf-8") as mainlist:
        todolist = mainlist.readlines()
except FileNotFoundError:
    with open("tasks.txt", "w", encoding="utf-8") as archive:
        archive.write("")
        print("Criando arquivos necessários...")
        sleep(1)
    with open("tasks.txt", "r", encoding="utf-8") as mainlist:
        todolist = mainlist.readlines()


# Create a new task
def createTask(taskName: str):
    with open("tasks.txt", "a", encoding="utf-8") as archive:
        archive.write(f"{taskName}\n")

def removeTask(taskNumber: int):
    with open("tasks.txt") as archive:
        line = archive.readlines()
    del line[taskNumber]