import pyautogui
import time


f = open('kohel.txt', 'r', encoding="utf-8")
str1 = f.readline().strip()
print(str1)

qest = int(pyautogui.confirm(text = "оставить(1), прибавить(2) или отнять деньги(3) с кошелька?", title = "ВОПРОС", buttons = ["1","2","3"]))

if qest == 1:
    f.close()
else:
    qest1 = int(input("Сколько? "))
    if qest == 2:
        f1 = open("kohel.txt", "w", encoding="utf-8")
        x = int(str1) + qest1
        f1.write(str(x))
        f1.close()
    if qest == 3:
        f2 = open('kohel.txt', 'w', encoding="utf-8")
        x1 = int(str1) - qest1
        f2.write(str(x1))
        f2.close()

