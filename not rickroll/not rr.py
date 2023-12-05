import pyautogui
import time
import pyqrcode
import png
import turtle

p = 0

f = open('login.txt', 'r', encoding="utf-8")


f2 = open('password.txt', 'r', encoding="utf-8")


def Sign_up():
    loginSign = pyautogui.prompt(text = "Enter login", title = "QUESTION")
    f1 = open("login.txt", "w", encoding="utf-8")
    f1.write(str(loginSign))
    f1.close()

    passwordSign = pyautogui.prompt(text = "Enter password", title = "QUESTION")
    f2 = open("password.txt", "w", encoding="utf-8")
    f2.write(str(passwordSign))
    f2.close()
    
def Login():
    loginSign = pyautogui.prompt(text = "Enter login", title = "QUESTION")
    f1 = open("login.txt", "r", encoding="utf-8")
    str1 = f1.readline().strip()
    f1.close()
    if str1 == loginSign:
        passwordSign = pyautogui.prompt(text = "Enter password", title = "QUESTION")
        f2 = open("password.txt", "r", encoding="utf-8")
        str2 = f2.readline().strip()
        f2.close()
        if str2 == passwordSign:
            my_qr = pyqrcode.create("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            my_qr.png('not rickrolll.png',scale=6)

            pyautogui.confirm(text = "All infornation in qrcode", title = "SECRET")
        else:
            pyautogui.confirm(text = "Incorrect password", title = "ERROR")
    else:
        pyautogui.confirm(text = "Incorrect login", title = "ERROR")

    
    
    
quest = pyautogui.confirm(text = "Login or Sign up", title = "QUESTION", buttons = ["Login","Sign up"])


if quest == "Sign up":
    Sign_up()
    
if quest == "Login":
    Login()
    
    
    
