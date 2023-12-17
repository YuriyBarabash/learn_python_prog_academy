def expenses_by_categories(file_name: str):
    categories = {}
    with open(file_name) as file:
        for line in file:
            _, *_, money, category = line.split()
            money = float(money.replace('$', ''))
            if category in categories:
                categories[category] += money
            else:
                categories[category] = money
    return categories


def expenses_by_users(file_name: str):
    users = {}
    with open(file_name) as file:
        for line in file:
            _, *name, money, _ = line.split()
            money = float(money.replace('$', ''))
            name = ' '.join(name)
            if name in users:
                users[name] += money
            else:
                users[name] = money
    return users


def expenses_by_user(file_name: str, user_name: str):
    user_expenses = {}
    with open(file_name) as file:
        for line in file:
            _, *name, money, category = line.split()
            name = ' '.join(name)
            if name.lower() != user_name.lower():
                continue
            money = float(money.replace('$', ''))
            if category in user_expenses:
                user_expenses[category] += money
            else:
                user_expenses[category] = money
    return user_expenses


def main():
    res = expenses_by_categories('hw_10_test.txt')
    res = '\n'.join(map(lambda key: f'{key.ljust(20,chr(45))}{res[key]:.2f}', res))
    print(res)

    res = expenses_by_users('hw_10_test.txt')
    res = '\n'.join(map(lambda key: f'{key.ljust(20,chr(45))}{res[key]:.2f}', res))
    print(res)

    res = expenses_by_user('hw_10_test.txt', input('user name >>'))
    res = '\n'.join(map(lambda key: f'{key.ljust(20,chr(45))}{res[key]:.2f}', res))
    print(res)



if __name__ == '__main__':
    main()
