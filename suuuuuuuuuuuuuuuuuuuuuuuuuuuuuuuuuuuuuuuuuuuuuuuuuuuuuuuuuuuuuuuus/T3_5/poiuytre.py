import pyautogui

sp = []

while True:
    quest = pyautogui.confirm(text = "Что сделать?", title = "QUESTION", buttons = ["добавить","удалить","вывести","стоп"])
    if quest == "добавить":
        sp.append(str(pyautogui.prompt(text = "Что добавить? ", title = "QUESTION")))
            
    elif quest == "удалить":
        sp.remove(str(pyautogui.prompt(text = "Что добавить? ", title = "QUESTION")))
            
    elif quest == "вывести":
        print(sp)
        
    elif quest == "стоп":
        break
