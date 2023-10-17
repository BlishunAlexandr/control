import os
import json

while True:
    what = int(input("Открыть(1), Создать(2), файлы(3), удаление(4), редактирование(5): "))

    if what == 1: 
        fileName = input("Введите Название файла: ")
        try:
            with open(fileName + ".json", "r", encoding="UTF-8") as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("Файл не найден")

    elif what == 2:
        nameNewFile = input("Введите название файла: ")
        newFile = open(nameNewFile + ".json", 'w', encoding="UTF-8")
        text = input("Введите текст: \n")
        newFile.write(text)
        newFile.close()

    elif what == 3:
        files = os.listdir()
        for file in files:
            print(file)

    elif what == 4:
        deleteFile = input("Введите название файла который нужно удалить: ")
        os.remove(deleteFile + ".json")

    elif what == 5:
        editFile = input("Введите название файла, который нужно редактировать: ")
        try:
            with open(editFile + ".json", "r", encoding="UTF-8") as file:
                content = file.read()
                print("Текущий текст в файле:\n", content)
                new_text = input("Введите новый текст: \n")
            with open(editFile + ".json", "w", encoding="UTF-8") as file:
                file.write(new_text)
                print("Текст успешно изменен.")
        except FileNotFoundError:
            print("Файл не найден")