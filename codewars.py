# Flatten and sort an array
# def flatten_and_sort(array):
#     a=[]
#     for i in array:
#         for j in i:
#             a.append(j)
#     return sorted(a)
# def flatten_and_sort(array):
#     return sorted([j for i in array for j in i])
# print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]))

# Deodorant Evaporator
# def evaporator(co, ev, th):
#     count = 0
#     th_2 = co * th * .01
#     while co >= th_2:
#         co=co*(1 - ev * .01)
#         count += 1
#     return count
# print(evaporator(10,10,5))

# Sum of the first nth term of Series
# def series_sum(n):
#     summa = 0
#     i = 1
#     for _ in range(1, n + 1):
#         summa += 1 / (i)
#         i += 3
#     return f'{summa:.2f}'
# def series_sum(n):
#     return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
# print(series_sum(0))

# Simple Encryption #1 - Alternating Split
# def encrypt(enc, n):
#     if n<=0 or enc==[]:
#         return enc
#     j = 1
#     while j <= n:
#         enc = ''.join([y for i, y in list(enumerate(enc)) if i % 2] + [y for i,y in list(enumerate(enc)) if i % 2 == 0])
#         j+=1
#     return enc
# print(encrypt("hskt svr neetn!Ti aai eyitrsig", 4))
#
# def decrypt(dec, n):
#     if n <= 0 or dec == []:
#         return dec
#     lst_tail = []
#     lst_head = []
#     lst_2 = []
#     j = 1
#     while j <= n:
#         for y, i in list(enumerate(dec)):
#             if y >= len(dec)//2:
#                 lst_tail.append(i)
#             elif y < len(dec)//2:
#                 lst_head.append(i)
#         for y, i in list(zip(lst_tail, lst_head)):
#             lst_2.append(y)
#             lst_2.append(i)
#         if len(dec)%2:
#             lst_2+=dec[len(dec)-1]
#         dec = lst_2
#         lst_2 = []
#         lst_tail = []
#         lst_head = []
#         j += 1
#     return ''.join(dec)
# print(decrypt("hsi  etTi sats!", 1))
# def decrypt(s, n):
#     if not s: return s
#     o, l = len(s) // 2, list(s)
#     for _ in range(n):
#         l[1::2], l[::2] = l[:o], l[o:]
#     return ''.join(l)
# def encrypt(s, n):
#     if not s: return s
#     for _ in range(n):
#         s = s[1::2] + s[::2]
#     return s


# text = input('text: ')
# text = text.split()
# text = sorted(set(text), key = text.index)
# print (text)

# Словари
# days = {1:'Mn',
#         2:'Tu',
#         3:'Wen',
#         4:'Tho',
#         5:'Fra',
#         6:'Set',
#         0:'Sun'
#         }
# date = int(input('date----> '))
# n = days.get(date % 7)
# print(f'{n}')

# Classwork 'вернуть чистые строки'
# text = (input('text : ')).split()
# lst = []
# for i in text:
#     lst.append(''.join(list(y for y in i if y.isalnum())))
# print (' '.join(lst))

# Classwork  'вернуть чистые строки' 2 вариант
# import string
# text = input('text=')
# for item in string.punctuation:
#     text = text.replace(item, ' ')
# print(text.split())

# Help the bookseller !
# def stock_list(list_of_art, list_of_cat):
#     lst = []
#     res = []
#     res_2 = []
#     summa = 0
#     for i in list_of_art:
#         lst.append(i.split())
#     lst = [(i[0],int(i[1])) for i in lst]
#     dict_art = dict(lst)
#     for x in list_of_cat:
#         for i,j in dict_art.items():
#             if x==i[0]:
#                 summa+=j
#         res.append(summa)
#         summa = 0
#     for i,j in list(zip(list_of_cat, res)):
#         res_2.append('('+i+':'+str(j)+')')
#     return '-'.join(res_2)
# # вариант codwars
# def stock_list(list_of_art, list_of_cat):
#     if list_of_art and list_of_cat:
#         return " - ".join("({} : {})".format(c, sum([int(i.split(" ")[1]) for i in list_of_art if c==i[0]])) for c in list_of_cat)
#     else:
#         return ""
# print(stock_list(["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"],["A", "B", "C", "D"]))

# Money, Money, Money
# def calculate_years(p, i, t, d):
#     y = 0
#     while p < d:
#         p = p + p * i * (1 - t)
#         y += 1
#     return y
# print(calculate_years(1000,0.05,0.18,1000))

# Two Sum
# def two_sum(num, target):
#     summa = 0
#     for i_c, i in enumerate(num):
#         for x_c, x in enumerate(num):
#             summa = i + x
#             if summa == target and i_c != x_c:
#                 return (i_c, x_c)
#
# print(two_sum([2 ,2, 3], 4))

# Classwork Lesson 7
# text_1 = input('text_1:').split()
# text_2 = input('text_2:').split()
# print(set(text_1).intersection(set(text_2)))

# def largest_pair_sum(numbers):
#     a = max(numbers)
#     numbers.remove(a)
#     print(numbers)
#     b = max(numbers)
#     return a+b
#
# print(largest_pair_sum([10,14,2,23,19]))

# def meeting(s):
#     lst = []
#     res = []
#     s = s.upper()
#     s = s.split(';')
#     for i in s:
#         lst.append(i.split(':'))
#     for i in lst:
#         res.append('('+i[1]+', '+i[0]+')')
#     res = sorted(res)
#     return ''.join(res)
#
# print(meeting("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn;Alex:Kor"))

import time
import timeit


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        stop = time.perf_counter()
        return f'{res}-----{stop - start:.8f} sec'

    return wrapper


# @measure_time
# def sum_pairs_1(ints, s):
#     lst = []
#     count = 1
#     ints_2 = ints.copy()
#     for x, y in enumerate(ints):
#         for i, j in enumerate(ints_2):
#             if y + j == s and x != i:
#                 lst.append(i)
#                 break
#         #if len(lst) > 0:
#             #break
#         count += 1
#         ints = ints[count:]
#     if lst == []:
#         return None
#     print (lst)
#     lst = list(sorted(set(lst), key=lst.index))
#     ind_min = min(lst[len(lst)//2:])
#     return [ints_2[ind_min], s - ints_2[ind_min]]
#
# @measure_time
# def sum_pairs(lst, s):
#     cache = set()
#     for i in lst:
#         if s - i in cache:
#             return [s - i, i]
#         cache.add(i)
#
#
# print(sum_pairs_1([10, 5, 2, 3, 7, 5, 10, 5, 2, 3, 7, 10, 5, 2, 3, 7],        10))
# print(sum_pairs([10, 5, 2, 3, 7, 5, 10, 5, 2, 3, 7, 10, 5, 2, 3, 7],        10))

# @measure_time
# def solve(s):
#     summa = []
#     n = 0
#     for i in s:
#         if i in 'aeiou':
#             s = s.replace(i, ' ')
#     s = s.split()
#     for i in s:
#         for j in i:
#             n += (ord(j)-96)
#         summa.append(n)
#         n = 0
#     return max(summa)
#
#
# import re
# @measure_time
# def solve_1(s):
#     return max(sum(ord(c)-96 for c in subs) for subs in re.split('[aeiou]+', s))
#
#
# print(solve("mischtschenkoanasdfasdhfewihfpiehrpfwergwehrghwegwefvqwdojfqejrfjqjfoajdfojadojqjdfoqjfoqof"))
# print(solve_1("mischtschenkoanasdfasdhfewihfpiehrpfwergwehrghwegwefvqwdojfqejrfjqjfoajdfojadojqjdfoqjfoqof"))


# @measure_time
# def check_exam(arr1,arr2):
#     n = 0
#     for i in zip(arr1, arr2):
#         if i[0]==i[1]:
#             n+=4
#         elif i[1] == '':
#             continue
#         elif i[0]!=i[1]:
#             n-=1
#     if n>=0:
#         return n
#     return 0

# @measure_time
# def check_exam_1(arr1, arr2):
#     return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))
#
# print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))
# print(check_exam_1(["a", "a", "b", "b"], ["a", "c", "b", "d"]))

# @measure_time
# def rev_rot(strng, sz):
#     if sz <= 0 or strng == '' or sz > len(strng):
#         return ''
#     lst = []
#     n = len(strng)//sz
#     a = 0
#     b = sz
#     for _ in range(n):
#         sub = strng[a:b]
#         if sum([int(i)**3 for i in sub]) % 2 == 0:
#             lst.append(sub[::-1])
#         else:
#             lst.append(sub[1:]+sub[0])
#         a = b
#         b += sz
#     lst = lst[:n]
#     return ''.join(lst)
#
# print(rev_rot("563000655734469485", 4))
#
# str = '''def rev_rot(strng, sz):
#     if sz <= 0 or strng == '' or sz > len(strng):
#         return ''
#     lst = []
#     n = len(strng) // sz
#     a = 0
#     b = sz
#     for _ in range(n):
#         sub = strng[a:b]
#         if sum([int(i) ** 3 for i in sub]) % 2 == 0:
#             lst.append(sub[::-1])
#         else:
#             lst.append(sub[1:] + sub[0])
#         a = b
#         b += sz
#     lst = lst[:n]
#     return ''.join(lst)
#
# print(rev_rot("563000655734469485", 4))'''
# print(f'{timeit.timeit(str, number=1):.8f}')
#
# def func(s):
#     result = sum(int(x)**3 for x in s)
#     if result % 2 == 0:
#         return s[::-1]
#     else:
#         return s[1:] + s[0]
# @measure_time
# def revrot(s, sz):
#     if not sz:
#         return ''
#     print(list(zip(*[iter(list(s))] * sz)))
#     return ''.join(func(''.join(x)) for x in zip(*[iter(list(s))]*sz))
#
# print(revrot("563000655734469485", 4))

# def title_case(title, minor_words=''):
#     strng = []
#     for i in title.lower().split():
#         if i in minor_words.lower().split():
#             strng.append(i.lower())
#         else:
#             strng.append(i.title())
#     return ' '.join(strng).
#
# print(title_case('a clash of KINGS', 'a an the of'))
import math
# def power_of_two(x):
#     print(math.log2(x))
#     if x == 0: return False
#     elif math.log2(x) % 1 == 0:
#         return True
#     return False
#
# print(power_of_two(38685626227668133590597628))


# def delete_nth(order, max_e):
#     order = order[::-1]
#     for j in order:
#         if order.count(j) >= max_e:
#             order.remove(j)
#     return order[::-1]
#
# print(delete_nth([2, 6, 43, 5, 39, 5, 39, 43, 43, 43, 43, 39, 6, 5, 5, 43, 39, 5, 5, 5, 43, 2, 6, 6, 2, 5, 39, 39, 6, 39, 39], 3))

# def name_shuffler(str_):
#     return ' '.join(reversed(str_.split()))
#
# print(name_shuffler('john McClane'))
# def regex(strng):
#     if len(strng) < 6:
#         return False
#     elif not strng.isupper() and not strng.islower() and not strng.isalnum():
#         return False
#     return True
# print(regex('4fdg5Fj3'))

# def find_even_index(arr):
#     for i in range(len(arr)):
#         if sum(arr[:i]) == sum(arr[i+1:]):
#             return i
#     return -1
# print(find_even_index([0,0,0,0,0]))


# def to_camel_case(text):
#     res = str()
#     if len(text) > 0:
#         for i in '-_':
#
#             if i in text:
#                 text = text.replace(i, ' ')
#
#         text = text.split()
#
#         for i in text[1:]:
#             res += i.capitalize()
#         return text[0] + res
#
#     return ''
#
# print(to_camel_case(""))

# def count_characters(s):
#     char_count = {}
#     for char in s:
#         char_count[char] = char_count.get(char, 0) + 1
#     return char_count
#
# print(count_characters('abarbara'))

# from datetime import datetime
#
# def checkCoupon(enteredCode, correctCode, currentDate, expirationDate):
#     print(datetime.strptime(currentDate,'%B %d, %Y'))
#     return enteredCode == correctCode and datetime.strptime(currentDate, "%B %d, %Y") <= datetime.strptime(
#         expirationDate, "%B %d, %Y")
#
# print(checkCoupon('123','123','September 5, 2014','October 1, 2014'))

# def create_phone_number(n):
#     n = list(map(str,n))
#     a = ''.join(n[:3])
#     b = ''.join(n[3:6])
#     c = ''.join(n[6:])
#
#     return f'({a}) {b}-{c}'
# print(create_phone_number([1,2,3,4,5,6,7,8,9]))

# def generate_primes():
#     for num in range(1, 101):
#         if is_prime(num):
#             yield num


# def diamond(n):
#     a = 1
#     b = n
#     strng = str()
#     if n % 2 == 0 or n <= 0:
#         return None
#     elif n == 1:
#         return '*\n'
#     else:
#         while a <= n:
#             strng += ' ' * (b // 2) + '*' * a + '\n'
#             a += 2
#             b -= 2
#         a = n - 2
#         b = 1
#         while a >= 1:
#             strng += ' ' * b + '*' * a + '\n'
#
#             a -= 2
#             b += 1
#     return strng
# print(diamond(21))

# def sum_of_intervals(intervals):
#     intervals = sorted(intervals, key=lambda x: x[0])
#     print(intervals)
#     total_length = 0
#     current_interval = list(intervals[0])
#     print(current_interval)
#     for interval in intervals[1:]:
#         if interval[0] <= current_interval[1]:
#             current_interval[1] = max(current_interval[1], interval[1])
#         else:
#             total_length += current_interval[1] - current_interval[0]
#             current_interval = interval
#     total_length += current_interval[1] - current_interval[0]
#     return total_length
#
# print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))

# def decipher_this(s):
#     s_digit = str()
#     s_str = str()
#     res = []
#     s = s.split()
#     for i in s:
#         for j in i:
#             if j.isdigit():
#                 s_digit += j
#             elif j.isalpha():
#                 s_str +=j
#         if len(s_str)>2:
#             s_str_2 = s_str[-1]
#             s_str_end = s_str[0]
#             res.append(chr(int(s_digit)) + s_str_2 + s_str[1:-1] + s_str_end)
#         elif 0<len(s_str)<=2:
#             res.append(chr(int(s_digit)) + s_str[::-1])
#         elif len(s_str) == 0:
#             res.append(chr(int(s_digit)))
#         s_digit = str()
#         s_str = str()
#
#     return ' '.join(res)
#
# print(decipher_this("84 109ero 104e 115wa 116eh 108sse 104e 115eokp"))


# def strip_comments(text, comment_markers):
#     lines = text.split('\n')
#     print(lines)
#     for i in range(len(lines)):
#         for marker in comment_markers:
#             index = lines[i].find(marker)
#             print(index)
#             if index != -1:
#                 lines[i] = lines[i][:index].rstrip()
#
#         else:
#             lines[i] = lines[i].rstrip()
#
#     result = '\n'.join(lines)
#     return result
#
# print(strip_comments('\tbananas\n. - lemons\nlemons @ @ pears strawberries -\nlemons\n-', ["'", '!', '^', '-', ',', '.', '#', '@', '=']))

# def valid_braces(s):
#     stack = []
#     mapping = {')': '(', ']': '[', '}': '{'}
#
#     for char in s:
#         if char in mapping.values():
#             stack.append(char)
#         elif char in mapping.keys():
#             if not stack or stack.pop() != mapping[char]:
#                 return False
#         else:
#             return False
#
#     return not stack
#
# print(("()("))

# def next_bigger(n):
#     digits = list(str(n))
#     i = len(digits) - 2
#     while i >= 0 and digits[i] >= digits[i + 1]:
#         i -= 1
#     if i == -1:
#         return -1
#     j = len(digits) - 1
#     while digits[j] <= digits[i]:
#         j -= 1
#     digits[i], digits[j] = digits[j], digits[i]
#     digits[i + 1:] = reversed(digits[i + 1:])
#     result = int(''.join(digits))
#     return result
#
# print(next_bigger(2017))

# def to_jaden_case(string):
#     string = string.split()
#     print (string)
#     print
#     return ' '.join([i.capitalize() for i in string])
#
# print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

# from datetime import datetime
#
#
# def check_coupon(enteredCode, correctCode, currentDate, expirationDate):
#     if enteredCode == correctCode and is_coupon_valid(currentDate, expirationDate):
#         return True
#     else:
#         return False
#
#
# def is_coupon_valid(currentDate, expirationDate):
#     current_date_obj = datetime.strptime(currentDate, "%B %d, %Y")
#     expiration_date_obj = datetime.strptime(expirationDate, "%B %d, %Y")
#     print(current_date_obj, expiration_date_obj)
#     if current_date_obj <= expiration_date_obj:
#         return True
#     else:
#         return False
#
# print(check_coupon('123','123','September 5, 2014','October 1, 2014'))

# def find_uniq(arr):
#     arr.sort(key=lambda x: x.upper())
#     print(arr)
#     arr1 = [set(i.upper()) for i in arr]
#     print(arr1)
#     return arr[0] if arr1.count(arr1[0]) == 1 and str(arr1[0]) != 'set()' else arr[-1]
#
# print(find_uniq(['bcd','cbd','dbac','bacd','dbca','cabd','cdab', 'foo']))

# def sort_gift_code(code):
#     res = [i for i in code]
#     res.sort()
#     return res
#
#
# print(sort_gift_code('sdasbsa'))

# def encode(st):
#     for i in st:
#         if i == 'a':
#             st = st.replace(i, '1')
#         if i == 'e':
#             st = st.replace(i, '2')
#         if i == 'i':
#             st = st.replace(i, '3')
#         if i == 'o':
#             st = st.replace(i, '4')
#         if i == 'u':
#             st = st.replace(i, '5')
#     return st
#
# print(encode('hello'))

# def encrypt_this(text: str) -> str:
#     """
#     Encrypt this!
#     :param text: str
#     :return: str
#     """
#
#     if len(text) == 0:
#         return ''
#     text = text.split(' ')
#     res = [(str(ord(i[0]))+i[1:][::-1]) for i in text]
#     return ' '.join(res)
#
# print(encrypt_this('A wise old owl lived in an oak'))

# def gps(s: int, x: list) -> int:
#     """
#     Speed Control
#     :param s: int
#     :param x: list
#     :return: int
#     """
#     return int(max(3600*(x[i+1] - x[i])/s for i in range(len(x)-1)))
#
# print (gps(20, [0.0, 0.18, 0.36, 0.54, 0.72, 1.05, 1.26, 1.47, 1.92, 2.16, 2.4, 2.64, 2.88, 3.12, 3.36, 3.6, 3.84]))

# def vowel_indices(word):
#     res = []
#     vowel = 'aeoiu'
#     for i in word:
#         if i in vowel:
#             res.append(word.index(i)+1)
#     return res
#
# print(vowel_indices("apple"))


# import re
# def func1(s):
#     """
#     A function that takes a string as input and finds all the integers in the string.
#
#     Parameters:
#     s (str): The input string to search for integers.
#
#     Returns:
#     list: A list of integers found in the input string.
#     """
#
#     pattern = '\d+'
#     result = re.findall(pattern, s)
#     return result
#
# print(func1('The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog'))

# import re
#
# # 1. re.match()
# pattern = r'hello'
# string = ' world hello'
# if re.match(pattern, string):
#     print("Match found!")
# else:
#     print("No match found.")
#
# # 2. re.search()
# pattern = r'world'
# string = 'hello world'
# match = re.search(pattern, string)
# if match:
#     print("Match found at index:", match.start())
#
# # 3. re.findall()
# pattern = r'\D+'
# string = 'The price is $20 and $50'
# matches = re.findall(pattern, string)
# print("All matches:", matches)
#
# # 4. re.finditer()
# pattern = r'\d+'
# string = 'Hello4 World26'
# iterator = re.finditer(pattern, string)
# for match in iterator:
#     print("Match found:", match.group())
#
# # 5. re.sub()
# pattern = r'\d+'
# string = 'I have 2 apples and 3 oranges'
# new_string = re.sub(pattern, '5', string)
# print("New string:", new_string)
#
# # 6. re.split()
# pattern = r'\D+'
# string = 'Split8 this2 string12'
# parts = re.split(pattern, string)
# print("Split parts:", parts)
#
# # 7. re.compile()
# pattern = re.compile(r'\d+')
# string = 'There are 3 cats and 5 dogs'
# matches = pattern.findall(string)
# print("Compiled pattern matches:", matches)
#
# # 8. re.fullmatch()
# pattern = r'\d+'
# string = '123'
# if re.fullmatch(pattern, string):
#     print("Full match found!")
# else:
#     print("No full match found.")
#
# # 9. re.escape()
# string = 'Escape special characters like . ^ $ * + ? { } [ ] \ | ( )'
# escaped_string = re.escape(string)
# print("Escaped string:", escaped_string)
#
# # 10. re.group()
# pattern = r'(\w+) (\w+)'
# string = 'John Doe'
# match = re.match(pattern, string)
# if match:
#     print("First name:", match.group(1))
#     print("Last name:", match.group(2))

# def new_avg(arr, newavg):
#     a = newavg*(len(arr) + 1) - sum(arr)
#     return a if a > 0 else ValueError
# print (new_avg([14, 30, 5, 7, 9, 11, 16], 90))
import decimal


# def parse_float(string):
#     """
#     A function to parse a string to a float if possible, otherwise return None.
#
#     Parameters:
#     string (str): The input string to be parsed to float.
#
#     Returns:
#     float or None: The parsed float if successful, None otherwise.
#     """
#     if isinstance(string, list):
#         lst = []
#         for i in string:
#             if i.isalpha():
#                 pass
#             elif isinstance(eval(i), float):
#                 lst.append(float(i))
#         return list(map(decimal.Decimal, lst)) if lst else None
#     return eval(string) if not string.isalpha() else None
#
#
# print(parse_float(['28.32', '4', 'ab', '23.78', '3.2']))

# def count_pages(summa: int) -> int:
#     summa_pages = 0
#     n = 1
#     count = 1
#     while summa_pages <= summa:
#         for i in str(n):
#             summa_pages += int(i)
#             n += 1
#             print(summa_pages)
#
#     return n
#
# print(count_pages(1095))

# def prefill(n, v=None):
#     try:
#         # n = int(n)
#         if n < 0:
#             raise ValueError
#         elif not isinstance(n,int):
#             raise TypeError
#
#     except (ValueError, TypeError):
#         return f'{n} is invalid'
#     return [v] * n
#
# print (prefill([11],[3,5,6]))
