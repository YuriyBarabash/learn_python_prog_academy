x = int(input('������ ������������� �����: '))
print(f'������������� ? {min(x,0) or False}')   # Task1
print(f'������ 20 {x<20}')                     # Task2
print(f'�� ����� ���� {x!=0}')                 # Task3
print(f'�������� �����: {bool(x%2)}')           # Task4
x, y, z = int(input('x----> ')), int(input('y----> ')), int(input('z----> '))  # Task5
print(f'max----> {max(x,y,z)}')
# Task1 (special with if)
a = str(input('���� �� � ��� ������������ �������������(yes/no) '))
if a == 'yes':
    print('�� ������ ��������� �����������')
else:
    print('�� �� ������ ��������� �����������')
# Task1 (without if)
a = str(input('���� �� � ��� ������������ �������������(yes/no) '))
b = '��'
print(f'�� {len(a)>2 or b} ������ ��������� �����������')
# Task2(special)
a = int(input('������� ��� ������� ���������� '))
if 0 < a < 18:
    print('�� �� �������������� ��������� ��� ��������� ������������� �������������')
else:
    print('�� ������ �������� ������������ �������������')
# Task3(special)
x = int(input('������� ����� ����� '))
if x >= 0 and x % 2 == 0:
    print('����� �������� ������������� � ������')
else:
    print('����� �� ������������� ���������')
# Task4(special)
x = int(input('������� ����� ����� '))
if x % 3 == 0 and x % 5 != 0:
    print('����� ��������')
else:
    print('����� �� ��������')





