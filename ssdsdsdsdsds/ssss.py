import pyautogui
import time
import keyboard


q = int(input("Какая папка? 1, 2 или 3? "))


pyautogui.hotkey('win', 'd')
time.sleep(1)

if q == 1:
    pyautogui.moveTo(1186, 170)
    pyautogui.doubleClick()
elif q == 2:
    pyautogui.moveTo(1279, 289)
    pyautogui.doubleClick()
elif q == 3:
    pyautogui.moveTo(1376, 170)
    pyautogui.doubleClick()

print("Спасибо за использование!")





