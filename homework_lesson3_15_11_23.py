# Task1
N_OF_ENTRANCES=4
N_OF_FLOORS=9
n = int(input('Введите номер квартиры (1-144) ----> '))
if n > 144:
    print('Ошибка! квартиры под таким номером нет в этом доме')
else:
    house = (n-1)//(N_OF_ENTRANCES*N_OF_FLOORS) + 1
    floor = (n-1)//N_OF_ENTRANCES % N_OF_FLOORS + 1
    print(f'Квартира находится на {floor}-ом этаже {house}-го подъезда')
# Task2
y = int(input('Number of year----> '))
if y % 100  and y % 4 == 0 or y % 400 == 0 :
    print(f'366 days in {y} year')
else:
    print(f'365 days in {y} year')
# Task3
a, b, c = int(input('A = ')), int(input('B = ')), int(input('C = '))
if a+b > c and a+c > b and b+c > a:
    print(True)
else:
    print(False)
# Task4
password = str(input('Please enter password (4 digit) '))
if password == '1234':
    print('Доступ дозволено')
else:
    print('Доступ заборонено')
# Task5
price = int(input('Please enter your price '))
if price > 1000:
    print(f'summary (+10%) = {price * 1.1:.2f}')
else:
    print(f'summary (without sale) = {price}')
# Task6
r = int(input('Будь ласка введите оценку обслуговування (1 - 5) '))
marks=[1,2,3,4,5]
answ=['Жахливо', 'Погано', 'Задовольно', 'Добре', 'Відмінно' ]
if r in marks:
    print(f'{answ[r-1]}')
else:
    print('Оценка не входить у діапaзон (1 - 5) !')
# Task 7
w, t = int(input('Введіть Вашу вагу (кг) ')), float(input('Введить Ваш зріст (м) '))
ind_w_b = round(w/(t**2), 1)
if ind_w_b >= 30:
    print('Ожиріння')
elif ind_w_b >= 25:
    print('Надлишкова вага')
elif ind_w_b >= 18.5:
    print('Нормальна вага')
else:
    print('Недостатньо ваги')



