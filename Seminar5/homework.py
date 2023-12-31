# Задача 26:  Напишите программу, которая на вход принимает 
# два числа A и B, и возводит число А в целую степень B с помощью рекурсии.


def pow(num_a, num_b):
    if (num_b == 1): return num_a
    return num_a * pow(num_a, num_b - 1)

print(pow(int(input("Введите число: ")), int(input("Введите степень: "))))


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух 
# целых неотрицательных чисел. Из всех арифметических операций допускаются 
# только +1 и -1. Также нельзя использовать циклы.


def sum(num_a, num_b):
    if (num_b == 0): return num_a
    return sum(num_a + 1, num_b - 1)

print(sum(int(input("Введите первое число: ")), int(input("Введите второе число: "))))