import os

newFileFlag = False
while True:
    what = int(input("Открыть(1), Создать(2), посмотреть файлы(3): "))
    if what == 1: 
        fileName = input("Введите путь и название файла: ")
        if fileName.endswith(".txt"): 
            try:
                with open(fileName, "r", encoding="UTF-8") as file:
                    content = file.read()
                    print(content)
            except FileNotFoundError:
                print("Файл не найден")
        else: 
            print("вы ввели неправильное название/расширение/путь файла")

    elif what == 2:
        while newFileFlag == False: 
            nameNewFile = input("Введите название файла: ")

            newFile = open(nameNewFile.txt, 'r+', encoding="UTF-8")