import pyautogui
import keyboard
import random

a = 0
data1 = 0
data2 = 0
data3 = 0
time1 = 0
time2 = 0
vlazhnost = int(random.randint(0,100))
a = 0
f = open('BLA}I{HOCT6.txt', 'r', encoding="utf-8")
str1 = f.readlines()
f.close()

qest = pyautogui.confirm(text = "Показать данные или ввести новые?", title = "ВОПРОС", buttons = ["Показать","Ввести"])

if qest == "Показать":
    for i in range(len(str1)):
        print(str1[a])
        a = a + 1
        
if qest == "Ввести":
    f = open('BLA}I{HOCT6.txt', 'a', encoding="utf-8")
    data1 = int(pyautogui.prompt(text = "Год?", title = "ВОПРОС", default = "0001"))
    data2 = int(pyautogui.prompt(text = "Месяц?", title = "ВОПРОС", default = "06"))
    data3 = int(pyautogui.prompt(text = "День?", title = "ВОПРОС", default = "08"))
    time1 = int(pyautogui.prompt(text = "Который был час?", title = "ВОПРОС", default = "07"))
    time2 = int(pyautogui.prompt(text = "Сколько было минут?", title = "ВОПРОС", default = "03"))
    pyautogui.confirm(text = "Влажность: "+ str(vlazhnost), title = "НЕ ВОПРОС")
    a = "\n" + str(data1) + "-" + str(data2) + "-" + str(data3) + " " + str(time1) + ":" + str(time1) + " " + str(vlazhnost)
    f.write(str(a))
    f.close()


