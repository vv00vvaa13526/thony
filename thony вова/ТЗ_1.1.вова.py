import pyautogui
import time

l = 0
p = 0

login = input("Login: ")
password = input("Password: ")


f = open('login.txt', 'r', encoding="utf-8")
str1 = f.readline().strip()
if str1 == login:
    l = 1
else:
    l = 0
f.close()

f2 = open('password.txt', 'r', encoding="utf-8")
str2 = f2.readline().strip()
if str2 == password:
    p = 1
else:
    p = 0
f.close()

if p == 0 and l == 0:
    print("Логин и пароль неверны")
    
if p == 0 and l == 1:
    print("Пароль неверен")
    
if p == 1 and l == 0:
    print("Логин неверен")
    
if p == 1 and l == 1:
    print("Загрузка...")
    time.sleep(3)
    f3 = open('secret.txt', 'r', encoding="utf-8")
    str3 = f3.readline().strip()
    f.close()
    print(str3)
    
    

