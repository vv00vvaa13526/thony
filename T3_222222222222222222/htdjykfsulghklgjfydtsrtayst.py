import os
import pyautogui
import keyboard

f1 = open('1.txt', 'r', encoding="utf-8")
str1 = f1.readline().strip()
f1.close()

f2 = open('2.txt', 'r', encoding="utf-8")
str2 = f2.readline().strip()
f2.close()

f3 = open('3.txt', 'r', encoding="utf-8")
str3 = f3.readline().strip()
f3.close()

f4 = open('4.txt', 'r', encoding="utf-8")
str4 = f4.readline().strip()
f4.close()
        
if str1 or str2 or str3 or str4 == "тревожно":
    os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    