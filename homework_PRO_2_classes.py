class Product:
    def __init__(self, name: str, price: float, product_description: str):
        self.name = name
        self.price = price
        self.product_description = product_description

    def __str__(self):
        return f'{self.name} {self.price} $ per 1 kg, {self.product_description}'

product_1 = Product('Tomatos', 1.36, 'red-pink,made in Montenegro')
product_2 = Product('Potatos', 0.86, 'small, homemade, type: kornishon')
product_3 = Product('Pork', 4.25, 'frash, local, best quality')

class Card:
    def __init__(self):
        self.products = {}

    def add_product(self, product, price: float, qry: int):
        if product not in self.products:
            self.products[product] = price*qry

    def __str__(self):
        return f'{self.products}  total bill {sum(self.products.values())}$'

card = Card()
card.add_product(product_1.name, product_1.price, 3)
card.add_product(product_2.name, product_2.price, 5)
card.add_product(product_3.name, product_3.price, 4)
print(card)
