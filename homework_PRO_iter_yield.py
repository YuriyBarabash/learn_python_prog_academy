# Task 1
class Cart:

    def __init__(self, items=[]):
        self.items = items

    def __iadd__(self, other):
        if isinstance(other, Cart):
            self.items += other.items
            return self
        else:
            raise ValueError("Allowed to merge only with another instance of the Cart class")

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration


cart1 = Cart(items=["apple", "pear"])
cart2 = Cart(items=["milk", "bread"])
cart3 = Cart(items=['tomatos', 'pork'])
cart4 = Cart(items=['potatos', 'milk', 'bread'])

for item in cart4:
    print(f'{item}')


# Task 2
class DishIterator:

    def __init__(self, names, prices):
        self.names = names
        self.prices = prices
        self.index = 0

    def __next__(self):
        if self.index >= len(self.names):
            raise StopIteration()
        name = self.names[self.index]
        price = self.prices[self.index]
        self.index += 1
        return name, price


class Dish:

    def __init__(self):
        self.names = []
        self.prices = []

    def add(self, name, price):
        self.names.append(name)
        self.prices.append(price)

    def __iter__(self):
        return DishIterator(self.names, self.prices)

    def __getitem__(self, item):
        if isinstance(item, int) and item > len(self.names) - 1:
            raise IndexError(f'Index of product name out of range, max = {len(self.names)-1}')

        if isinstance(item, int):
            return self.names[item], self.prices[item]

        if isinstance(item, slice):
            res_names = self.names[item]
            res_prices = self.prices[item]
            return list(zip(res_names, res_prices))

    def __len__(self):
        return len(self.names)


def main():
    dish = Dish()
    dish.add('Tartar Monte', 24.00)
    dish.add('Fish Veg', 22.00)
    dish.add('Salad with cherry tomatoes and onions', 20.00)
    dish.add('Melt the steak on the grill', 27.00)
    dish.add('Fiorentina T-BON steak', 12.00)
    dish.add('Veal schnitzel', 18.00)
    dish.add('Homemade sweat pies', 4.00)
    dish.add('Baklava', 4.50)

    for name, price in dish:
        print(f'{name}: {price}')

    print(len(dish))

    #print(dish[5])
    for i,j in dish[::2]:
        print(f'{i}----{j}$')

if __name__ == '__main__':
    main()

# Task 3 geometric progression
def g_progression(n, i):
    temp = n
    while True:
        yield temp
        temp *= i

generate = g_progression(4, 2)
for _ in range(10):
    print(next(generate))

# Task 4 own_range
def own_range(start, stop, step=1):
    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    elif step < 0:
        while current > stop:
            yield current
            current -= abs(step)

for i in own_range(1, 20, 2):
    print(i)

# Task 5
def generate_primes(limit):
    primes = []
    num = 2
    while num < limit:
        is_prime = all(num % i != 0 for i in primes)
        if is_prime:
            primes.append(num)
            yield num
        num += 1


limit = 18
prime_generator = generate_primes(limit)

res = ' '.join(map(str, (prime for prime in prime_generator)))
print(res)

# Task 6
n = int(input('n= '))
lst = [i**3 for i in range(2, n+1)]
print(lst)

#Task 7
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci_generator()
res = ' '.join(map(str, (next(fib_gen) for _ in range(10))))
print(res)


#Task 8
from datetime import timedelta, date

def generate_dates(start, end):
    current_date = start
    while current_date <= end:
        yield current_date
        current_date += timedelta(days=7)


start = date(2024, 1, 1)
end = date(2024, 12, 31)
weeks = 0
for generated_date in generate_dates(start, end):
    print(generated_date)
    weeks +=1
print(f'{weeks} weeks in current period ')
