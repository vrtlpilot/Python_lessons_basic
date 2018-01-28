# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

i = 0
fruits = ["яблоко", "банан", "киви", "арбуз"]
for fruit in fruits:
    i = i + 1
    print('{}. {:>6}'.format(i, fruit))

# Подсказка: воспользоваться методом .format()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
list1 = ['4', 'dfsdf', 'kh43']
list2 = ['456', 'dfsdf']

for item in list2:
    if item in list1:
        list1.remove(item)
print(list1)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
list1 = (23, 555555, 80, 23, 5, 9, 345)
list2 = []
for item in list1:
    if item % 2 == 0:
        list2.append(item/4)
    else:
        list2.append(item*2)

print(list2)
