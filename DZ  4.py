# Вычислить число c заданной точностью d Пример: при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from cmath import pi

# d = int(input('Введите точность числа Пи '))
# print(f'Число Пи с заданной точностью {d} равно {round(pi,d)}')



# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# num = int(input("Введите число: "))
# i = 2 # первое простое число
# lst = []
# old = num
# while i <= num:
#    if num % i == 0:
#        lst.append(i)
#        num //= i
#        i = 2
#    else:
#        i += 1
# print(f"Простые множители числа {old} приведены в списке: {lst}")



# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# from random import randint


# n = int(input(sum))
# list = []
# for i in range(1,n+1):
#    a = randint(-n,n+1)
#     list.append(a)
# print(list)

# newlist = []
# for i in list:
#    if i not in newlist:
#         newlist.append(i)
# print(newlist)


# a= [1,2,2,2,2,3,1,4]

# print(set(a))