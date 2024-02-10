import random

chislo = int(random.randint(0,10))

x = 1
print("Угадай число от 1 до 10 за три попытки")

for i in range(0,4):
    if x == 4:
        print("!тЫ пРоИгРаЛ!")
        break 
    
    y = int(input(str(x)+" попытка: "))
    
    if y == chislo:
        print("Твоё число равно загаданному \n-}> I Ты ПоБеДиЛ I <{-")
        break 
       
    elif y > chislo:
        print("Твоё число больше загаданного")
        x += 1
        
    elif y < chislo:
        print("Твоё число меньше загаданного")
        x += 1

        
    
    
