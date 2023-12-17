import time
import timeit

# Task 1
#start_1 = time.time()
str_1 = '''
def func(*args):
    """arithmetic progression"""
    for j in range(len(args)-2):
        if args[j+1] - args[j] != args[j+2] - args[j+1]:
            return None
    return args[-1] + args[1] - args[0]


def func_2(*args):
    """geometric progression"""
    for j in range(len(args) - 2):
        if args[j+1]/args[j] != args[j+2]/args[j+1]:
            return None
    return int(args[-1]*args[1]/args[0])


def func_3(x, *args):
    """consistency likes n^x,(n+step)^x..."""
    lst = [round(i**(1/x), 3) for i in args]
    if isinstance(func(*lst), float):
        return int((args[-1]**(1/x) + args[1]**(1/x) - args[0]**(1/x))**x)
    else:
        return None


def func_4(*args):
    """consistency likes n(1), n(2)+1, n(3)+2,..., n(y)+(y-1)"""
    for j in range(len(args) - 2):
        if args[j+1] - args[j] != args[j+2] - args[j+1] - 1:
            return None
    return args[-1]*2 - args[-2] + 1


def func_5(*args):
    """consistency of Fibonacci"""
    for j in range(len(args)-2):
        if args[j+2] != args[j] + args[j+1]:
            return None
    return args[-1] + args[-2]


def func_6(*args):
    """Factorial"""
    for j in range(1, len(args)):
        if args[j] != (j+1)*args[j-1]:
            return None
    return args[-1]*(len(args)+1)


n = '1 2 3 4 5 6 7 8 9 10' #input('string of numbers (min 3 num) : ')
n = list(map(int, n.split()))


def switch(*args):
    a = 0
    if args[1] - args[0] == args[2] - args[1]:
        return func(*args)
    elif args[0] != 0 and args[1] / args[0] == args[2] / args[1]:
        return func_2(*args)
    elif args[1] - args[0] == args[2] - args[1] - 1:
        return func_4(*args)
    elif args[2] == args[0] + args[1]:
        return func_5(*args)
    elif args[1] == 2*args[0]:
        return func_6(*args)
    else:
        for i in range(2, 6):
            if round(args[1]**(1/i), 3) - round(args[0]**(1/i), 3) == round(args[2]**(1/i), 3) - round(args[1]**(1/i), 3):
                a = i
                break
            else:
                a = -1
        return func_3(a, *args)

switch(*n)'''
#print(round((time.time() - start_1), 4))

# Task 1
str_2 = '''def parse_text(text: str) -> list:    
    punctuations = ',:;'
    for char in punctuations:
        text = text.replace(char, ' ')
    return list(map(int, text.split()))

def is_arithmetic(numbers: list) -> bool:    
    if len(numbers) < 3:
        return False
    d = numbers[1] - numbers[0]
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] != d:
            return False
    return True

def is_geometric(numbers: list) -> bool:    
    if len(numbers) < 3:
        return False
    q = numbers[1] // numbers[0]
    for i in range(len(numbers) - 1):
        if numbers[i + 1] // numbers[i] != q:
            return False
    return True

def next_arithmetic_item(numbers: list) -> int | float:   
    if len(numbers) < 3:
        return None
    d = numbers[1] - numbers[0]
    return numbers[-1] + d

def next_geometric_item(numbers: list) -> int | float:   
    if len(numbers) < 3:
        return None
    q = numbers[1] // numbers[0]
    return numbers[-1] * q

def next_sequence_item(numbers: list) -> int | float:    
    if is_arithmetic(numbers):
        return next_arithmetic_item(numbers)
    if is_geometric(numbers):
        return next_geometric_item(numbers)
    return None

def main():    
    text = '1 2 3 4 5 6 7 8 9 10'#input('numbers>>')
    numbers = parse_text(text)
    item = next_sequence_item(numbers)
    print(f'Next item is {item}')

if __name__ == '__main__':
    main()'''
# print (round(timeit.timeit(str_1, number=1000000), 4))
# print (round(timeit.timeit(str_2, number=1000000),4))

# Task 2
#start_time = time.time()
str_3 = '''lst = []
lst_num_1 = []
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        mul = str(i * j)
        if mul[:3] == mul[:2:-1]:
            lst.append(mul)
            lst_num_1.append(i)
            break
for i, j in enumerate(lst):
    if j == max(lst):
        index = i
for i, j in enumerate(lst_num_1):
    if index == i:
        num_1 = j
print(f'{max(lst)}, {num_1} * {int(int(max(lst))/(num_1))}')'''
#print(round((time.time() - start_time), 4))


str_4 = '''def polindrom(*num):
    mul = str(num[0] * num[1])
    if mul[:3] == mul[:2:-1]:
        return int(mul), num[0], num[1]
    return None


#start_time_2 = time.time()
res = []
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        lst = [i,j]
        if isinstance(polindrom(*lst), tuple):
            res.append(polindrom(*lst))
            break
print(max(res))'''
# print(round((time.time() - start_time_2), 4))
#print (round(timeit.timeit(str_3, number=100), 4))
#print (round(timeit.timeit(str_4, number=100),4))
str_5 = '''def is_palindrome(item: int) -> bool:
    item = str(item)
    return item == item[::-1]
    
                    
def max_palindrome(start: int, stop: int) -> int:
    if stop < start:
        start, stop = stop, start
    result = []
    for i in range(start, stop):
        for j in range(start, stop):
            if is_palindrome(i * j):
                result.append((i, j, i * j))

    return max(result, key=lambda item: item[2])


def main():
    print(max_palindrome(100, 1000))


if __name__ == '__main__':
    main()'''
print(round(timeit.timeit(str_5, number=100), 10))


#classwork recurcia
# def my_pow(a,b):
#     if b==0
#         return 1
#     return a*my_pow(a,b-1))



