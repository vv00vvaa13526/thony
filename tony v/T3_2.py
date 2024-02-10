a = []
x = 0

for i in range(0,6):
    y = int(input("Какая у Максимилиана оценка? "))
    a.append(y)

sred_ocenka = (int(a[0]) + int(a[1]) + int(a[2]) + int(a[3]) + int(a[4]) + int(a[5])) / 6
print("Средняя оценка Максимилиана: "+str(sred_ocenka))
    
    