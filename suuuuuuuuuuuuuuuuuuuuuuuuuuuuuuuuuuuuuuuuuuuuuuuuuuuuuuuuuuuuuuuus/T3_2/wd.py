import pyautogui

sp = ['a','b','c','d','e']


for x in range(len(sp)):
    quest = pyautogui.confirm(text = "Что сделать с элементом "+sp[x], title = "QUESTION", buttons = ["удалить","заменить","оставить"])
    if quest == "удалить":
        sp.pop(x)
        
        
    elif quest == "заменить":
        sp[x] = pyautogui.prompt(text = "На что заменить? ", title = "QUESTION")
        
        
    elif quest == "оставить":
        continue
    x-=1
print(sp)