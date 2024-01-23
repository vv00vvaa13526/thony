a = 0
b = 0

f1 = open('3agadky.txt', 'r', encoding="utf-8")
str1 = f1.readlines()
f1.close()

f2 = open('otvets.txt', 'r', encoding="utf-8")
str21 = f2.readline(1).strip()
str22 = f2.readline(2).strip()
str23 = f2.readline(3).strip()
str24 = f2.readline(4).strip()
f2.close()

for i in range(0,4):
    print(str1[a])
    a += 1

print("Попробуй угадать хотя бы одну загадку.")
x = input("Твой ответ: ")

if str(x) == str21:
    b = 1
    f1 = open('otvets.txt', 'w', encoding="utf-8")
    f1.write("отгадано\n2\n3\n4")
    f1.close()
if str(x) == str22:
    b = 1
    f1 = open('otvets.txt', 'w', encoding="utf-8")
    f1.write("1\nотгадано\n3\n4")
    f1.close()
if str(x) == str23:
    b = 1
    f1 = open('otvets.txt', 'w', encoding="utf-8")
    f1.write("1\n2\nотгадано\n4")
    f1.close()
if str(x) == str24:
    b = 1
    f1 = open('otvets.txt', 'w', encoding="utf-8")
    f1.write("1\n2\n3\nотгадано")
    f1.close()
if str(x) == "отгадано":
    print("Ах ты читер! Так не пойдёт!")
    b = 2
    
if b == 1:
    print("Ты отгадал!")
    
if b == 0:
    print("Нет такого ответа")
    
if b == 2:
    pass
    
    

