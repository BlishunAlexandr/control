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
        editFileName = input("Введите название файла, который нужно редактировать: ")
        try:
            with open(editFileName + ".json", "r", encoding="UTF-8") as file:
                content = file.read()
                print("Текущий текст в файле:\n", content)
                choice = input("Хотите изменить (1) весь текст или (2) часть текста: ")
                if choice == "1":
                    new_text = input("Введите новый текст: \n")
                elif choice == "2":
                    start = int(input("Введите начальную позицию: "))
                    end = int(input("Введите конечную позицию: "))
                    new_text = input("Введите новый текст для замены: ")
                    content = content[:start] + new_text + content[end:]
                else:
                    print("Некорректный выбор.")
                    continue
            with open(editFileName + ".json", "w", encoding="UTF-8") as file:
                file.write(content)
                print("Текст успешно изменен.")
        except FileNotFoundError:
            print("Файл не найден")