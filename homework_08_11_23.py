#Task 1
name= input('please enter your name ')
print (f'Hello,{name}')

#Task2
print ('Please input five numbers',end='\n')
num1 = int(input ('1-st number '))
num2 = int(input ('2-nd number '))
num3 = int(input ('3-d number ' ))
num4 = int(input ('4-th number '))
num5 = int(input ('5-th number '))
print (f'max number is {max(num1, num2, num3, num4, num5)}')
print (f'min number is {min(num1, num2, num3, num4, num5)}')
print (f'middle value of numbers is {(num1+num2+num3+num4+num5)/5}')

#Task3
x = float(input('x-----> '))
y = float(input('y-----> '))
print(f'addition: x+y= {x+y}')
print(f'subtraction: x-y= {x-y}')
print(f'multiplication: x*y= {x*y}')
print(f'division: x/y= {round(x/y, 2)}')

#Task4
r = float(input('radius-----> '))
print(f'length of circle-----> {round(2*3.14*r, 2)}')
print(f'diameter-----> {round(2*r,2)}')
print(f'square of circle-----> {round(2*3.14*r**2, 2)}')

#Task5
p = int(input('Пожалуйста введите сумму вклада (euro) '))
n = int(input('Пожалуйста введите количество лет сбережения депозита '))
a = round(p*pow(1.1, n), 2)
print(f'Сумма вашего депозита через {n} лет составит {a} евро')

#Task6
s=int(input('Please enter amount for exchange ($) '))
print(f'your amount in grn equals (rate of currency 1$=36.01 grn to 08.11.23) {round(s*36.01, 2)} grn')

#Task7
n=int(input('Please enter three-digit number '))
print(f'{n//100}')
print(f'{n%100//10}')
print(f'{n%10}')


