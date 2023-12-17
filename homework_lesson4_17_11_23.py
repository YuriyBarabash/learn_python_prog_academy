# # Task1 Cчастливый билет
# lst = []
# for i in range(1, 5):
#     n = int(input(f'namber {i} ---> '))
#     lst.append(n)
# print(sum(lst[:2]) == sum(lst[2:]))
#
# # Task2 Полиндром
# lst = []
# for i in range(1, 7):
#    n = int(input(f'namber {i} ---> '))
#    lst.append(n)
# print(lst == lst[::-1])
#
# # Task3 координаты в окружности
# R = 4
# x, y = int(input('x----> ')), int(input('y----> '))
# print(abs(x) <= (R ** 2 - y ** 2)**.5 and abs(y) <= (R ** 2 - x ** 2)**.5)

# # Task4 кратное 7
# for i in range(1,101):
#     if i % 7 == 0:
#         print(i, end=' ')
#
# Task5 сумма нечетных чисел
# print([i for i in range(1,100,2)])
# print(sum(range(1,100,2)))
#
# # Task6 вывод чисел с шагом 5
# i = 1
# STEP = 5
# while i <= 200:
#     print(i, end = ' ')
#     if i % STEP == 0:
#         print('')
#     i += 1
#
# # Task7 факториал
# n = int(input('n----> '))
# f = 1
# for i in range(2, n+1):
#     f *= i
# print(f'f----> {f}')
#
# # Task8 Таблица умножения
# n = 5
# for i in range(1, 11):
#     print(f'{i} x {n} = {i * n}')
#
# # Task9 Прямоугольник
# h, w = int(input('h----> ')), int(input('w----> '))
# print('*' * w)
# for _ in range(h-2):
#     print('*','' * w, '*')
# print('*' * w)
#
# # Task10 Количество нечетных чисел
# lst = [0, 5, 2, 4, 7, 1, 3, 19]
# count = 0
# for i in lst:
#     if i % 2:
#         count += 1
# print(f'value of odds {count}')
#
# Task11
# import random
# lst = []
# for _ in range(4):
#     lst.append(random.randint(1, 100))
# lst.extend([i*2 for i in lst])
# print(lst)
#
# # Task12 среднемесячная зарплата
# import random
# lst = []
# MOUNTHS = 12
# for _ in range(MOUNTHS):
#     lst.append(random.randint(10000, 20000))
# print(lst)
# print(f'{sum(lst)/len(lst):.2f}')
#
# # Task13 Матрица
# arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# summa = 0
# for i in range(0, len(arr)):
#     print(arr[i])
#     summa += sum(arr[i])
#     print(summa)
# print(f'sum = {summa}')
#
# # Task14 Зеркало
# def lst(a):
#     a_rew = a[::-1]
#     return a, a_rew
# print(lst([1,2,2,2,3,4,5,6,7,9]))
#
# # Task15 простые числа
# a, b, c = [], [], []
# for i in range(1, 101):
#     b.append(i)
#     for j in range(2, i):
#        if i % j == 0:
#            a.append(i)
#            break
# for i in b:
#     if i not in a:
#         c.append(i)
# print(c)
#
# Task16
# n = int(input('please odd n-----> '))
# if n % 2:
#     s = 0
#     for i in range(n, 0, -2):
#         print(' '*s, '*'*i, ' '*s, i)
#         s += 1
#     s -= 2
#     for i in range(3, n+1, 2):
#         print(' '*s, '*'*i, ' '*s, i)
#         s -= 1
# else:
#     print(bool(n % 2))
#
# Classwork
# text = str(input('text = '))
#     while '  ' in text:
#         text = text.replace('  ', '')

# x = [
#     '1 Bob Simson 19.58$ decorations',
#     '2 Mary 66.7$ food',
#     '3 Mary 98.91$ toys',
#     '4 Aleksa 72.29$ drinks',
# ]
# summa = 0
# for i in x:
#     summa+=float((i.split()[-2]).replace('$',''))
#
# print(summa)



