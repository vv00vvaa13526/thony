import pyautogui

z = 0


pyautogui.confirm(text = "Я Дед Мороз и мне нужен список твоих подарков.", title = "НЕ ВОПРОС")

for i in range(0,3):
    f = open('spsk_pdrkv.txt', 'a', encoding="utf-8")
    x = pyautogui.prompt(text = "Что ты хочешь?", title = "ВОПРОС", default = "пиши сюда")
    f.write(x+"\n")
    f.close
    z += 1
    if z < 3:
        pyautogui.confirm(text = "Хочешь что-то ешё?", title = "НЕ ВОПРОС", buttons = ["Да","Да"])
    else:
        pyautogui.confirm(text = "Хочешь что-то ешё?", title = "НЕ ВОПРОС", buttons = ["Нет","Нет"])
