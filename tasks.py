from os import listdir, chdir, mkdir
from time import sleep

def createTask(name: str):
    with open("main.txt", "a", encoding="utf-8") as archive:
        archive.write(f"{name}\n")

def createCategory(name: str):  
    try:
        mkdir("categorys")
    except FileExistsError:
        chdir("./categorys")
        if name in listdir():
            print(f"Categoria {name} já existe")
        chdir("./../")
    sleep(5)