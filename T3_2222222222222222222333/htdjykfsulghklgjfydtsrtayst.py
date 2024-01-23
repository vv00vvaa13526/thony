import os
import pyautogui
import keyboard
import time

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
        
if str(str1) == "trevozhno":
    pyautogui.hotkey('win', 'd')
    os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    time.sleep(1)
    keyboard.write("номер экстренной службы")
    pyautogui.hotkey('Enter')
    
elif str(str2) == "trevozhno":
    pyautogui.hotkey('win', 'd')
    os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    time.sleep(1)
    keyboard.write("номер экстренной службы")
    pyautogui.hotkey('Enter')
    
elif str(str3) == "trevozhno":
    pyautogui.hotkey('win', 'd')
    os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    time.sleep(1)
    keyboard.write("номер экстренной службы")
    pyautogui.hotkey('Enter')
    
elif str(str4) == "trevozhno":
    pyautogui.hotkey('win', 'd')
    os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    time.sleep(1)
    keyboard.write("номер экстренной службы")
    pyautogui.hotkey('Enter')
    
elif str(str1) == "подозрительно":
    pyautogui.hotkey('win', 'd')
    os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    time.sleep(1)
    keyboard.write("номер аварийной службы")
    time.sleep(1)
    pyautogui.hotkey('Enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    keyboard.write("номер сантехника")
    time.sleep(1)
    pyautogui.hotkey('Enter')
    
elif str(str2) == "подозрительно":
    pyautogui.hotkey('win', 'd')
    os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    time.sleep(1)
    keyboard.write("номер аварийной службы")
    time.sleep(1)
    pyautogui.hotkey('Enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    keyboard.write("номер сантехника")
    time.sleep(1)
    pyautogui.hotkey('Enter')
    
elif str(str3) == "подозрительно":
    pyautogui.hotkey('win', 'd')
    os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    time.sleep(1)
    keyboard.write("номер аварийной службы")
    time.sleep(1)
    pyautogui.hotkey('Enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    keyboard.write("номер сантехника")
    time.sleep(1)
    pyautogui.hotkey('Enter')
    
elif str(str4) == "подозрительно":
    pyautogui.hotkey('win', 'd')
    os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    time.sleep(1)
    keyboard.write("номер аварийной службы")
    time.sleep(1)
    pyautogui.hotkey('Enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    keyboard.write("номер сантехника")
    time.sleep(1)
    pyautogui.hotkey('Enter')
    
    