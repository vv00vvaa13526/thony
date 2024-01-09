import pyautogui
import keyboard
import random


a = 0

f = open('blackspsk.txt', 'r', encoding="utf-8")
str1 = f.readline(1).strip("\n")
str2 = f.readline(3).strip("\n")
str3 = f.readline(5).strip("\n")
f.close() #тут забыл добавить (), close() это функция, так что скобки должны быть всегда

print(str1)
print(str2)
print(str3)

qest = pyautogui.prompt(text = "Ваше имя и фамилия", title = "ВОПРОС", default = "Амогус Сусовиковский")

if str(qest) == str(str1) or str(qest) == str(str2) or str(qest) == str(str3):
    pyautogui.confirm(text = "Вы в BLACKSPSK. Покинте помешение.", title = "НЕ ВОПРОС", buttons = ["ОК","ОК"])

    
else:
    qest1 = pyautogui.prompt(text = "Сколько сейчас времени?", title = "ВОПРОС", default = "8:00")
    f1 = open('whitespsk.txt', 'a', encoding="utf-8")
    a = "\n" + str(qest1) + " " + str(qest)
    f1.write("\n" + str(qest1) + " " + str(qest))
    f1.close() #тут забыл добавить (), close() это функция, так что скобки должны быть всегда
    

