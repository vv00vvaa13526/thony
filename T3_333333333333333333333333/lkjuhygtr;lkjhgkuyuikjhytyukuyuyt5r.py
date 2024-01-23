qest = input("В какой фаил записать (покупки - 1, идеи - 2, задачи - 3)? ")
qest1 = input("Что записать? ")
x = str(qest) + ".txt"
x1 = "- " + str(qest1)
f1 = open(str(x), 'a', encoding="utf-8")
f1.write(str(x1))
f1.close()