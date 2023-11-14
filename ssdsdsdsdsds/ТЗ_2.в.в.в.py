import pyautogui
import time
import keyboard


q = int(input("Что гуглим? 1 или 2? "))


pyautogui.hotkey('win', 'd')
time.sleep(1)

pyautogui.moveTo(759, 1060)
pyautogui.click()
time.sleep(1)

pyautogui.moveTo(1065, 504)
pyautogui.click()

if q == 1:
    keyboard.write("hfpevty kb z?")
    
elif q == 2:
    keyboard.write("Ckfdf hj,jnfv!")
    
pyautogui.press('enter')