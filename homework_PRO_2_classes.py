# Task 1

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


class Cart:
    def __init__(self):
        self.products = []
        self.quantities = []

    def add_product(self, product: Product, quantity: int | float = 1):
        if not isinstance(product, Product) or not isinstance(quantity, (int, float)):
            raise TypeError("Invalid type.")
        self.products.append(product)
        self.quantities.append(quantity)

    def total(self):
        return sum(product.price * quantity for product, quantity in zip(self.products, self.quantities))

    def __str__(self):
        res = str()
        for product, quantity in zip(self.products, self.quantities):
            res += f'{product.name} - {product.price} x {quantity} = {product.price * quantity} UAH\n'
        res += f'Total: {self.total()} UAH'
        return res


card = Cart()
card.add_product(product_1,  3)
card.add_product(product_2,  5)
card.add_product(product_3,  4)
print(card)

# Task 2


class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f'{self.name.ljust(50,chr(45))}{self.price} $ ({self.description})'


class MenuCategory:
    def __init__(self, name):
        self.name = name
        self.dishes = []

    def add_dish(self, dish: Dish):
        if not isinstance(dish, Dish):
            raise ValueError("Not a dish")

        if dish not in self.dishes:
            self.dishes.append(dish)

    def __str__(self):
        return f'{self.name}:\n' + '\n'.join(map(str, self.dishes))


dish_1 = Dish('Tartar Monte', 'prosciutto, marinated leg of lamb, crust, homemade cheese', 24.00)
dish_2 = Dish('Fish Veg', 'ostopus salad, fish file, tuna tartar', 22.00)
dish_3 = Dish('Salad with cherry tomatoes and onions', 'freeze salad, cherry, onion, cheese', 20.00)
dish_4 = Dish('Melt the steak on the grill', 'Sliced steak, Grana padano, rocket, pine nuts', 27.00)
dish_5 = Dish('Fiorentina T-BON steak', 'price of request', 12.00)
dish_6 = Dish('Veal schnitzel', 'veal, lemon juice, butter, capers, rice', 18.00)
dish_7 = Dish('Homemade sweat pies', 'apple or cherry', 4.00)
dish_8 = Dish('Baklava', 'turkish desert', 4.50)

category_1 = MenuCategory('Cold appetizers')
category_1.add_dish(dish_1)
category_1.add_dish(dish_2)
category_1.add_dish(dish_3)
category_2 = MenuCategory('Meat Specialties')
category_2.add_dish(dish_4)
category_2.add_dish(dish_6)
category_2.add_dish(dish_5)
category_3 = MenuCategory('Deserts')
category_3.add_dish(dish_7)
category_3.add_dish(dish_8)


def main():
    print(f'{category_1}\n\n{category_2}\n\n{category_3}')


if __name__ == '__main__':
    main()





