# homework5
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def square_func(a, b):
    c = a**b
    return c
sq = square_func(a = int(input()), b = int(input()))
print(sq)


# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух 
# целых неотрицательных чисел. Из всех арифметических операций 
# допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a,b):
    c = a + b
    return c
summa = sum(a = int(input()), b = int(input()))
print(summa)
