num_elements = input('Введите количество элементов первого списка:')
if num_elements.isdigit():
    mylist = []
    for i in range(int(num_elements)):
        mylist.append(int(input(f'Введите {i+1} элемент: ')))
#    mylist.sort()
    print(mylist)
else:
    print('Некорректный ввод, попробуйте снова')

my_elements = input('Введите элементы второго списка через запятую:')
if my_elements.find(',') > 0:
    x = ","
elif my_elements.find(';') > 0:
    x = ";"
elif my_elements.find('/') > 0:
    x = "/"
second_list = my_elements.split(x)
second_list = list(map(int, second_list))
print(second_list)

a = [i for i in mylist if not i in second_list]
print(a)