f = open('nachalo.txt', 'r', encoding="utf-8")
str(nachalo_list) = f.readlines()
f.close()

f1 = open('konec.txt', 'r', encoding="utf-8")
str(konec_list) = f1.readlines()
f1.close()

a = nachalo_list[0] + konec_list[0]
a1 = nachalo_list[1] + konec_list[1]
a2 = nachalo_list[2] + konec_list[2]
a3 = nachalo_list[3] + konec_list[3]
a4 = nachalo_list[4] + konec_list[4]

f2 = open('itogo.txt', 'w', encoding="utf-8")
f2.write(a)
f2.write(a1)
f2.write(a2)
f2.write(a3)
f2.write(a4)
f2.close()
