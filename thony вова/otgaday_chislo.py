import random

numPeople = 0

numRandom = 0

while True:
    numRandom = random.randint(1,100)
    print("Угадай задуманное число от 1 до 100")
    numPeople = int(input("Число вводить здесь "))
    
    elif numPeople < numRandom:
        print("Ты не угадал. Число было",str(numRandom)+". Ты промахнулся на",str(numRandom - numPeople))
        
    elif numPeople > numRandom:
        print("Ты не угадал. Число было",str(numRandom)+". Ты промахнулся на",str(numPeople - numRandom))
        
    elif numPeople == numRandom:
        print("ТЫ УГАДАЛ!!! Число было",str(numRandom))
        