import random

a = [0]*10

for i in range(len(a)):
    a[i] = random.randint(0,100)

min = int(0)

for i in range(len(a)):
    print(a[i])

for i in range(len(a)):
    if (min < a[i]) :
        min = a[i]
        
print(min)