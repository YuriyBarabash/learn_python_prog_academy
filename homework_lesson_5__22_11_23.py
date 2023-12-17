# # Task 1 Подсчитать "b"
# text = input('text: ')
# n = text.count('b')
# print(f'b : {n}' )

# Task 3
# text = input('text : ')
# print(sum(map(ord,text)))

# # Task 2 Имя
# name = str(input('Name: '))
# if name.isalpha() and name.istitle() and name[1:].islower() and len(name)>1:
#     print(name)
# else:
#     print(False)
#
# # Task 4 Число Pi
# import math
# for i in range(2,11):
#     print(f'{math.pi:.{i}f}')
#
# # Task 5 Самое длинное слово
# text = input('text : ')
# text = text.split()
# text = sorted(text, key = len, reverse = True)
# print(text[0])

#Task 5 Самое длинное слово 2 вар
# text = input('text : ')
# text = text.split()
# text = max(text, key = len)
# print(text)

# # Task 6 если символы не повторяются
# strng = str(input('text: '))
# res = ''.join(sorted(set(strng), key = strng.index))
# print (res)
#
# Task 6 для любых символов
# strng = input('text: ')
# temp = ''
# n = 1
# for i in strng:
#     if (temp + i) * (len(strng)//n) in strng:
#         res = temp + i
#         break
#     else:
#         temp += i
#     n += 1
# print(res)
#
# # Task 7
# text = '<div class="b-popup__title">Быстрая регистрация</div> <div class="b-popup__title">Опция пополнения</div>'\
# '<div class="b-popup__title">Режим работы</div> <div class="b-popup__title">Завершение сеанса</div>'\
# '<div class="b-popup__title">контакты</div>'
# text = text.split('/div>')
# res = []
# for  i in text:
#     temp = ''.join(i.split('>', maxsplit=1)[1:])
#     temp = (temp.rsplit('<', maxsplit=1)[:-1])
#     res += temp
# print(' '.join(res))
# 2 вариант
# while '<' in text:
#     text = text.replace(text[text.find('<'):text.find('>')+1],'')
# print(text)

