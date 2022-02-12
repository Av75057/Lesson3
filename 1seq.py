
num_elements = input('Введите количество элементов:')
if num_elements.isdigit():
    mylist = []
    for i in range(int(num_elements)):
        mylist.append(int(input(f'Введите {i+1} элемент: ')))
    mylist.sort()
    print(mylist)
else:
    print('Некорректный ввод, попробуйте снова')
