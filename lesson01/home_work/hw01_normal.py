
__author__ = 'Пантелеев А.А.'

# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4

number = int(input('Введите число: '))
while True:
    if 0 < number < 10:
        break
    number = int(input('Введите число больше 0, но меньше 10: '))
print(number ** 2)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
a = a + b
b = a - b
a = a - b
print('A = ', a)
print('B = ', b)

