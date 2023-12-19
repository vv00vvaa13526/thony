f = open('nachalo.txt', 'r', encoding="utf-8")
shopping_list = f.readlines()
formatted_list = []
f.close()
for item in shopping_list:
    item = item.rstrip('\n')
    formatted_item = item
    formatted_list.append(formatted_item)
    
f1 = open('konec.txt', 'r', encoding="utf-8")
shopping_list1 = f1.readlines()
formatted_list1 = []
f1.close()
for item1 in shopping_list1:
    item1 = item1.rstrip('\n')
    formatted_item1 = item + item1 
    formatted_list1.append(formatted_item1)


f = open('itogo.txt', 'w', encoding="utf-8")
f.write('\n'.join(formatted_list1))
f.close()