import pyautogui
import time

qest = int(pyautogui.confirm(text = "изменить(2) или вывести(1) текст?", title = "ВОПРОС", buttons = ["1","2"]))

if qest == 1:
    f = open('file.txt', 'r', encoding="utf-8")
    str1 = f.readline().strip()
    print("Сейчас текст в файле такой:", str1)
    f.close()

elif qest == 2:
    f1 = open('file.txt', 'w', encoding="utf-8")
    str2 = input("Введите новый текст файла: ")
    f1.write(str2)
    f1.close()

