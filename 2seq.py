
my_elements = input('Введите элементы списка через запятую:')
if my_elements.find(',') > 0:
    x = ","
elif my_elements.find(';') > 0:
    x = ";"
elif my_elements.find('/') > 0:
    x = "/"
first_list = my_elements.split(x)

second_list = []
for i in range(len(first_list)):
    if first_list.count(first_list[i]) == 1:
       second_list.append(int(first_list[i]))
print(second_list)