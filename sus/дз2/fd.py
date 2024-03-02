import pyautogui
import shutil

f1 = open('a.txt', 'r', encoding="utf-8")
str1 = f1.readline().strip()
f1.close()

quest1 = pyautogui.confirm(text = "Текст файла a: "+str(str1)+"\nПеренести в важное?", title = "QUESTION", buttons = ["Да","Нет"])

if quest1 == "Да":
    shutil.copy('a.txt','важное/a1.txt')
if quest1 == "Нет":
    pass


f2 = open('b.txt', 'r', encoding="utf-8")
str2 = f2.readline().strip()
f2.close()

quest2 = pyautogui.confirm(text = "Текст файла b: "+str(str2)+"\nПеренести в важное?", title = "QUESTION", buttons = ["Да","Нет"])

if quest2 == "Да":
    shutil.copy('b.txt','важное/b1.txt')
if quest2 == "Нет":
    pass


f3 = open('b.txt', 'r', encoding="utf-8")
str3 = f3.readline().strip()
f3.close()

quest3 = pyautogui.confirm(text = "Текст файла c: "+str(str3)+"\nПеренести в важное?", title = "QUESTION", buttons = ["Да","Нет"])

if quest3 == "Да":
    shutil.copy('c.txt','важное/c1.txt')
if quest3 == "Нет":
    pass
