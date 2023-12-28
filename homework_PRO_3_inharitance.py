# Task 1 inheritance Discount
class Discount:
    def discount(self):
        return 0

class Regular(Discount):
    def discount(self):
        return 0.01


class Silver(Discount):
    def discount(self):
        return 0.05


class Gold(Discount):
    def discount(self):
        return 0.1


class Product:
    def __init__(self, name: str, price: float, product_description: str):
        self.name = name
        self.price = price
        self.product_description = product_description

    def __str__(self):
        return f'{self.name} - {self.price}'


class Customer:
    def __init__(self, name: str, discount: Discount):
        self.name = name
        self.discount = discount


class Order:
    def __init__(self):
        self.products = []
        self.quantities = []

    def add_product(self, product: Product, quantity: int):
        self.products.append(product)
        self.quantities.append(quantity)

    def total_price(self, customer: Customer = None):
        discount = customer.discount.discount() if customer else 0
        total = 0
        for product, quantity in zip(self.products, self.quantities):
            total += product.price * quantity
        return f'{total * (1 - discount): .2f}'

    def __str__(self):
        return '\n'.join(map(str, self.products))


discounts = {
    'regular': Regular(),
    'silver': Silver(),
    'gold': Gold()
}

if __name__ == '__main__':
    print('Discounts:')
    for discount in discounts:
        print(discount)
    discount = input('your discount: ')
    customer = Customer('Yuriy', discounts[discount])

    product_1 = Product('Tomatos', 1.36, 'red-pink,made in Montenegro')
    product_2 = Product('Potatos', 0.86, 'small, homemade, type: kornishon')
    product_3 = Product('Pork', 4.25, 'frash, local, best quality')

    order = Order()
    order.add_product(product_1, 4)
    order.add_product(product_2, 3)
    order.add_product(product_3, 2)

    print(order.total_price(customer))

