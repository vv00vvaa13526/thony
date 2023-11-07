num = int(input("Введите число              ПОЛОЖИТЕЛЬНОЕ!!!! "))

x = 0

a = [0]*num
    
if num == 0:
    print("Фактариал",1)
    
if num < 0:
    print("ПОЛОЖИТЕЛЬНОЕ!!!!!")
    
if num > 0:
    num1 = num -1
    for i in range(num-1, 0, -1):
        num *= i
    print("Фактариал", num)
        
        
        
        
    
    