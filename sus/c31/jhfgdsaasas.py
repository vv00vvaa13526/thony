import pyautogui

a = ['1','2']
b = ['3','4']

c = ['a','b']

quest1 = pyautogui.confirm(text = "Из какой группы вывесть текст из фаила?", title = "QUESTION", buttons = [str(c[0]),str(c[1])])

if quest1 == str(c[0]):
    quest2 = pyautogui.confirm(text = "Из какого файла вывести текст?", title = "QUESTION", buttons = [str(a[0]),str(a[1])])
    
    if quest2 == str(a[0]):
        f1 = open(str(a[0])+'.txt', 'r', encoding="utf-8")
        str1 = f1.readline().strip()
        f1.close()
        print(str(str1))
        
    elif quest2 == str(a[1]):
        f2 = open(str(a[1])+'.txt', 'r', encoding="utf-8")
        str2 = f2.readline().strip()
        f2.close()
        print(str(str2))
    
elif quest1 == str(c[1]):
    quest3 = pyautogui.confirm(text = "Из какого файла вывести текст?", title = "QUESTION", buttons = [str(b[0]),str(b[1])])
    
    if quest3 == str(b[0]):
        f3 = open(str(b[0])+'.txt', 'r', encoding="utf-8")
        str3 = f3.readline().strip()
        f3.close()
        print(str(str3))
        
    elif quest3 == str(b[1]):
        f4 = open(str(b[1])+'.txt', 'r', encoding="utf-8")
        str4 = f4.readline().strip()
        f4.close()
        print(str(str4))
    