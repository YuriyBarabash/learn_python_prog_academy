# # Task 1 Словарь {слово:количество вхождений}
# strng = (input('text: ')).split()
# text = {i:strng.count(i) for i in strng}
# print(text)
#
# # Task 2 Словарь русско-английский
from translate import Translator as tr
en = tr(from_lang='Russian', to_lang='English')
print('Введите пять слов для перевода(ru-en)')
word_rus = [input(f'слово {i} ') for i in range (1,6)]
word_en = [en.translate(i) for i in word_rus]
d ={i:j for i,j in list(zip(word_rus,word_en))}
print(d,end='/n', file=open('vocabul.txt','a'))
for i,j in d.items():
    print(f'{i.ljust(10,chr(45))}{5*chr(45)}-> {j}')

# # Task 3 Телефонная книга
# phonebook = dict(Александр_СТО='+30672353481', Ольга_английский='+30631254632', Мария_менеджер='+30695641113',\
#                  Паша='+30731243324', Работа='+30692223335')
# for i,j in phonebook.items():
#     print(f'{i.ljust(20,chr(45))}{10*chr(45)}-> {j}')
# n = int(input('Выберите\n1 - Удалить\n2 - Изменить\n3 - Добавить\n4 - Показать номер\n----->'))
# name = input('Введите имя: ')
# if name in phonebook:
#     if n == 1:
#         del phonebook[name]
#     elif n == 2:
#         number = input('Введите новый номер: ')
#         phonebook[name] = number
#     elif n == 3:
#         number = input('Введите номер телефона: ')
#         phonebook[name] = number
#     elif n == 4:
#         print(f'номер-----> {phonebook[name]}')
# else:
#     print('Error!')
# for i,j in phonebook.items():
#     print(f'{i.ljust(20,chr(45))}{10*chr(45)}-> {j}')

# Task 4
# exchange = {
#             'eur': 39.39,
#             'usd': 36.04,
#             'gbr': 45.33,
#             'pln': 9.02,
#             'czk': 1.61,
#             'grn': 1.00
#              }
# n, current = int(input('value  ')), input('input eur/usd/gbr/pln/czk/grn: ')
# current_out = input('output eur/usd/gbr/pln/czk/grn: ')
# print(f'{n} {current} = {exchange.get(current)*n/exchange[current_out]:.2f} {current_out}')



