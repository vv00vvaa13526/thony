import pyautogui
import time

qest = pyautogui.confirm(text = "какая температура?", title = "ВОПРОС", buttons = ["< 10°","10° - 30°","> 30°"])

f = open('orangereya.txt', 'r', encoding="utf-8")
text = f.read().strip()
f = open('orangereya.txt', 'a', encoding="utf-8")

if qest == "< 10°":
    f.write("Слишком низкая температура!")
