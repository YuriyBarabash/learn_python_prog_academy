x = int(input('Только отрицательное число: '))
print(f'Отрицательное ? {min(x,0) or False}')   # Task1
print(f'меньше 20 {x<20}')                     # Task2
print(f'Не равно нулю {x!=0}')                 # Task3
print(f'нечетное число: {bool(x%2)}')           # Task4
x, y, z = int(input('x----> ')), int(input('y----> ')), int(input('z----> '))  # Task5
print(f'max----> {max(x,y,z)}')
# Task1 (special with if)
a = str(input('Есть ли у Вас водительское удостоверение(yes/no) '))
if a == 'yes':
    print('Вы можете управлять автомобилем')
else:
    print('Вы не можете управлять автомобилем')
# Task1 (without if)
a = str(input('Есть ли у Вас водительское удостоверение(yes/no) '))
b = 'не'
print(f'Вы {len(a)>2 or b} можете управлять автомобилем')
# Task2(special)
a = int(input('Укажите Ваш возраст пожалуйста '))
if 0 < a < 18:
    print('Вы не соответствуете критериям для получения водительского удостоверения')
else:
    print('Вы можете получить водительское удостоверение')
# Task3(special)
x = int(input('Введите целое число '))
if x >= 0 and x % 2 == 0:
    print('Число является положительным и четным')
else:
    print('Число не соответствует критериям')
# Task4(special)
x = int(input('Введите целое число '))
if x % 3 == 0 and x % 5 != 0:
    print('Число подходит')
else:
    print('Число не подходит')





