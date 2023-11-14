import pyautogui
import time
import keyboard
def ctrlv():
    pyautogui.moveTo(1279, 289)
    pyautogui.doubleClick()
    
def ctrla1():
    pyautogui.moveTo(1176, 170)
    pyautogui.doubleClick()
    
def ctrla2():
    pyautogui.moveTo(1276, 70)
    pyautogui.doubleClick()

def ctrla3():
    pyautogui.moveTo(1376, 170)
    pyautogui.doubleClick()

y = int(pyautogui.confirm(text = "1 2 или 3 папка?", title = "ВОПРОС", buttons = ["1","2","3"]))

pyautogui.hotkey('win', 'd')

time.sleep(1)

if y == 1:
    ctrla1()
if y == 2:
    ctrla2()
if y == 3:
    ctrla3()
    
time.sleep(1)

pyautogui.hotkey('ctrl', 'a')
time.sleep(1)

pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

pyautogui.hotkey('alt', 'f4')
time.sleep(1)

pyautogui.moveTo(1276, 270)
pyautogui.doubleClick()

pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

pyautogui.hotkey('alt', 'f4')