# # Task 1 Проверка уникальности текста
# text = input('text:').split()
# print(len(set(text)) == len(text))
#
# # Task 2 Вернет количество уникальных элементов
# def count_lst(lst: list | tuple) -> int:
#     count = 0
#     for i in lst:
#         if lst.count(i) == 1:
#             count += 1
#     return count
#
# # Task 3 Проверит словарь на уникальность значений
# def unique_dict(uni: dict) -> bool:
#     """
#     Checks the dictionary for unique values
#     :param uni: dict
#     :return: boolean
#     """
#     return len(set(uni.values())) == len(uni.values())
#
#
# print(unique_dict({'one': 1, 'two': 2, 'three': 3, 'four': 4}))
# print(unique_dict.__doc__)
#
# # Task 4
# f_1, f_2 = input('user1/2/3/4: '), input('user1/2/3/4: ')
# f_1 = ''.join(i for i in f_1 if i.isalnum())
# f_2 = ''.join(i for i in f_2 if i.isalnum())
# friendships = {
#      "user1": {"user2", "user3", "user4"},
#      "user2": {"user1", "user3"},
#      "user3": {"user1", "user2", "user4"},
#      "user4": {"user1", "user3"}
# }
# if f_1 != f_2:
#      print(''.join(friendships.get(f_1) & friendships.get(f_2)))
# else: 'error!'
#
# # Task 5 Самое длинное слово в двух строках
# text_1, text_2 = input('text_1: '), input('text_2: ')
# a = set((text_1).split()) & set((text_2).split())
# if a == set():
#     print('haven`t similar words')
# else:
#     print(max(a, key=len))
#
# # ФУНКЦИИ
#
# # Task 1
# def func(a: int, b: int, strng: str) -> str:
#     """
#     makes concatenation of parameters
#     :param a: int
#     :param b: int
#     :param strng: str
#     :return: str
#     """
#     return strng + str(a + b)
#
# # Task 2
# def rectangle(w: int, h: int) -> str:
#     return f"{'*' * w}\n" + f"*{' ' * (w - 2)}*\n" * (h - 2) + f"{'*' * w}\n"
#
# # Task 3
# def search(lst: list | tuple, a: int) -> int:
#   if a in lst:
#       return lst.index(a)
#   else:
#       return -1
#
# # Task 4
# import string
# def count_of_words(strng: str) -> int:
#     for item in string.punctuation:
#          strng = strng.replace(item, ' ')
#     return len((strng.split()))
#
# # Task 5
# def convert_to_words(a: float) -> str:
#     unit = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     dec = [0, 1, 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
#     a = str(a)
#     a_cent = int(a[-2] + a[-1])
#     if len(a)<=5:
#         d = a[:-3]
#         def cent(c: int):
#             if a_cent < 10:
#                 cents = f'{unit[int(a[-1])]}'
#             if a_cent == 10:
#                 cents = 'ten'
#             elif a_cent == 11:
#                 cents = 'eleven'
#             elif a_cent == 12:
#                 cents = 'twelve'
#             elif 10<a_cent<20:
#                 cents = f'{dec[int(a[-1])][:-2]}teen'
#             elif a_cent>20:
#                 cents = f'{dec[int(a[-2])]} {unit[int(a[-1])]}'
#             return cents
#         def dollars(d: str):
#             if len(a) == 4:
#                 dollar = f'{unit[int(d[0])]}'
#             elif len(a) == 5:
#                 if int(d) == 10:
#                     dollar = 'ten'
#                 elif int(d) == 11:
#                     dollar = 'eleven'
#                 elif int(d) == 12:
#                     dollar = 'twelve'
#                 elif 10 < int(d) < 20:
#                     dollar = f'{dec[int(d[-1])][:-2]}teen'
#                 elif int(d) >= 20:
#                     dollar = f'{dec[int(d[-2])]} {unit[int(d[-1])]}'
#                 return dollar
#         return f'{dollars(d)} dollars {cent(a_cent)} cents'
#     else:
#         return f'number bigger then 99.99'
# Task 5 c помощью модуля
# from num2words import num2words
# def convert_to_word(a):
#        a=str(a).split('.')
#        return f'{num2words(a[0], to="cardinal")} dollars {num2words(a[1], to="cardinal")} cents'
# print(convert_to_word(132.24))

# Classwork lesson 8
# def func(*args,op='+',**kwargs):
#     mul=1
#     print(args)
#     print(op)
#     print(kwargs)
#     if op == '+':
#         return sum(args)
#     elif op == '*':
#         for i in kwargs.values():
#             mul*=i
#         return mul
# print(func(1,2,3,4,5,6,op="*",b=2,d=3,f=5))


