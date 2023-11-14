import pyautogui
import time
import keyboard
 
x = str(pyautogui.prompt(title = "ВОПРОС",text = "Во сколько стоматолог?"))
y = str(pyautogui.confirm(text = "Завтра или послезавтра?", title = "ВОПРОС", buttons = ["завтра","послезавтра"]))

pyautogui.hotkey('win', 'd')
time.sleep(1)
pyautogui.hotkey("winleft","r")
time.sleep(1)
pyautogui.write("notepad")
time.sleep(1)
pyautogui.press("enter")

keyboard.write("Стоматолог "+y+" в "+x)

pyautogui.hotkey("ctrl","s")

keyboard.write("sssssssssssssssssssss")

pyautogui.press("enter")