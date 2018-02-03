# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    nd = 10 ** ndigits
    num = number * nd
    if num % nd >= 5:
        num += 1
    return int(num) / nd


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    str_ticket_number = str(ticket_number)
    half_sum_left = 0
    half_sum_right = 0
    half_len = len(str_ticket_number) // 2
    if half_len * 2 == len(str_ticket_number):
        for number in str_ticket_number[:half_len]:
            half_sum_left = half_sum_left + int(number)
        for number in str_ticket_number[half_len:]:
            half_sum_right = half_sum_right + int(number)
        if half_sum_left == half_sum_right:
            return True
    return False


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
