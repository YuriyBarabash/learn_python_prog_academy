class Product:
    def __init__(self, name: str, price: float, product_description: str):
        self.name = name
        self.price = price
        self.product_description = product_description




    def __str__(self):
        return f'{self.name} {self.price} $ per 1 kg, {self.product_description}'

class IncorrectValue(Exception):
    def __init__(self, price, message):
        self.price = price
        self.message = message


class Cart:
    def __init__(self):
        self.products = []
        self.quantities = []

    def add_product(self, product: Product, quantity: int | float = 1):
        if not isinstance(product, Product) or not isinstance(quantity, (int, float)):
            raise TypeError("Invalid type.")
        try:
            if product.price <= 0:
                raise IncorrectValue(product.price, f'{product.name} price must be bigger then 0')
            self.products.append(product)
            self.quantities.append(quantity)
        except IncorrectValue as err:
            print(err)



    def total(self):
        return sum(product.price * quantity for product, quantity in zip(self.products, self.quantities))

    def __str__(self):
        res = str()
        for product, quantity in zip(self.products, self.quantities):
            res += f'{product.name} - {product.price} x {quantity} = {product.price * quantity} UAH\n'
        res += f'Total: {self.total()} UAH'
        return res

product_1 = Product('Tomatos', -1.22, 'red-pink,made in Montenegro')
product_2 = Product('Potatos', 0.86, 'small, homemade, type: kornishon')
product_3 = Product('Pork', 4.25, 'frash, local, best quality')
cart = Cart()
cart.add_product(product_1,  3)
cart.add_product(product_2,  5)
cart.add_product(product_3,  4)
print(cart)