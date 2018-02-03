# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    temp = [0, 1]
    for i in range(1, m):
        temp.append(temp[-2] + temp[-1])
    return temp[n:]


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    new_list = list()
    for number in origin_list:
        i = 0
        while i < len(new_list) and number > new_list[i]:
            i += 1
        new_list.insert(i, number)
    return new_list


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def filter_function(x):
    if x > 0:
        return x
    return None


def my_filter(origin_list):
    return_list = []
    for x in origin_list:
        if filter_function(x):
            return_list.append(x)
    return return_list


my_filter([2, 34, 0, -12, 34, -3, 0, 89])

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


