# homework5
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def square_func(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    else: 
        c = a**b
        return c

print(square_func(a = int(input()), b = int(input())))



# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух 
# целых неотрицательных чисел. Из всех арифметических операций 
# допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a,b):
    if a < 0 and b < 0:
        return 'Try again'
    else:
        c = a + b
        return c

print(sum(a = int(input()), b = int(input())))
