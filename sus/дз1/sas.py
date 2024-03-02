import pyautogui
from PIL import Image

image1 = Image.open('sus.png')
image2 = Image.open('sas.png')
image3 = Image.open('ususu.png')

image1.show()
quest1 = pyautogui.confirm(text = "Что сделать с картинкой?", title = "QUESTION", buttons = ["Повернуть на 90°","Перевернуть вверх ногами","Оставить и не изменять"])

if quest1 == "Повернуть на 90°":
    new_image1 = image1.rotate(90)
    new_image1.save("new_sus1.png")
    image1.close
    
if quest1 == "Перевернуть вверх ногами":
    new_image1 = image1.rotate(180)
    new_image1.save("new_sus2.png")
    image1.close
    
if quest1 == "Оставить и не изменять":
    pass


image2.show()
quest2 = pyautogui.confirm(text = "Что сделать с картинкой?", title = "QUESTION", buttons = ["Повернуть на 90°","Перевернуть вверх ногами","Оставить и не изменять"])

if quest2 == "Повернуть на 90°":
    new_image2 = image2.rotate(90)
    new_image2.save("new_sas1.png")
    image2.close
    
if quest2 == "Перевернуть вверх ногами":
    new_image2 = image2.rotate(180)
    new_image2.save("new_sas2.png")
    image2.close
    
if quest2 == "Оставить и не изменять":
    pass


image3.show()
quest3 = pyautogui.confirm(text = "Что сделать с картинкой?", title = "QUESTION", buttons = ["Повернуть на 90°","Перевернуть вверх ногами","Оставить и не изменять"])

if quest3 == "Повернуть на 90°":
    new_image3 = image3.rotate(90)
    new_image3.save("new_ususu1.png")
    image3.close
    
if quest3 == "Перевернуть вверх ногами":
    new_image3 = image3.rotate(180)
    new_image3.save("new_ususu2.png")
    image3.close
    
if quest2 == "Оставить и не изменять":
    pass
        



