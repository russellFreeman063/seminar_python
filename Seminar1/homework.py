# Задача 2: Найдите сумму цифр трехзначного числа.

# num = int(input("Введите число: "))
# sum = num % 10
# while num > 0:
#     num //= 10
#     sum += num % 10
# print(sum)


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# s = int(input("Введите количество журавликов: "))
# print((s//6), ((s//6)*4), (s//6))


# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# num = int(input("Введите номер билета: "))
# num1 = num % 10 + (num // 10) % 10 + (num // 100) % 10
# num2 = (num // 1000) % 10 + (num // 10000) % 10 + (num // 100000) % 10
# print(num1 == num2)


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# n = int(input("Введите x размер шоколадки: "))
# m = int(input("Введите y размер шоколадки: "))
# k = int(input("Введите количество долек: "))
# if k < m * n and (k % m == 0 or k % n == 0):
#     print("yes")
# else: 
#     print("no")




