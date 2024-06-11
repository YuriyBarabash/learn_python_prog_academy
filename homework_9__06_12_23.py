
def categories_of_goods(data: list) -> list:
    lst_of_goods = []
    for i in data:
        lst_of_goods.append(i[-1])
    return list(set(lst_of_goods))

def total_sum_of_category(good: str, g_prices: list) -> float:
    total = 0
    for i, j in g_prices:
        if good == i:
            total += float(j[:-1])
    return round(total, 2)

def names(data: list) -> list:
    """
    This function returns list of names of customers
    :param data: list of
    :return: list(set(lst_of_names))
    """
    lst_of_names = []
    for i in data:
        if len(i) == 5:
            lst_of_names.append(i[1]+' '+i[2])
        elif len(i) == 4:
            lst_of_names.append(i[1])
    return list(set(lst_of_names))

def money_of_every(name: str, lst: list) -> float:
    """

    """
    money = 0
    name = name.split(' ')
    for i, j in lst:
        if name[0] == i:
            money += float(j[:-1])
    return round(money, 2)

def numbers_of_goods(name: str, lst) -> int:
    count = 0
    name = name.split(' ')
    for i, j in lst:
        if name[0] == i:
            count += 1
    return count

def main():
    with open('hw_10_test.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')[:-1]
        data = [i.split() for i in data]
    category = categories_of_goods(data)                                       # Task 1
    lst = [i[:-3:-1] for i in data]
    for i in category:
        total = total_sum_of_category(i, lst)
        print(f'{i.ljust(20,chr(45))}{total}$\n', file=open('report.txt', 'a'))
        print(f'{i.ljust(20,chr(45))}{total}$')
    name = names(data)                                                          # Task 2
    lst_2 = [(i[1], i[-2]) for i in data]
    for i in name:
        money = money_of_every(i, lst_2)
        print(f'{i.ljust(20,chr(45))}{money}$\n', file=open('report.txt', 'a'))
        print(f'{i.ljust(20,chr(45))}{money}$')
    n = input('enter name (Bob Simpson, Maria Simpson, Aleksa, Jack, Mary) ')   # Task 3
    money_one = money_of_every(n, lst_2)
    number = numbers_of_goods(n, lst_2)
    print(f'{n}------{money_one}$----for {number} goods')

if __name__ == '__main__':
    main()



