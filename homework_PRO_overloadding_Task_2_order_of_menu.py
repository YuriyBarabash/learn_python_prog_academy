class Menu:
    def __init__(self):
        self.menu_items = {}

    def add_item(self, item_name, price):
        self.menu_items[item_name] = price

class DishNotFound(Exception):
    def __init__(self, dish, massage):
        self.dish = dish
        self.massage = massage
        super().__init__()

    def __str__(self):
        return f'{self.dish} {self.massage}'

class Order:
    def __init__(self):
        self.order_items = {}

    def __iadd__(self, menu_item):
        menu, item_name = menu_item
        if item_name in menu.menu_items:
            if item_name in self.order_items:
                self.order_items[item_name] += 1
            else:
                self.order_items[item_name] = 1
            return self
        else:
            raise DishNotFound(item_name, 'not found in the menu.')


# Example usage
menu = Menu()
menu.add_item('Tartar Monte', 24.00)
menu.add_item('Fish Veg', 22.00)
menu.add_item('Salad with cherry tomatoes and onions', 20.00)
menu.add_item('Melt the steak on the grill', 27.00)
menu.add_item('Fiorentina T-BON steak', 12.00)
menu.add_item('Veal schnitzel',18.00)
menu.add_item('Homemade sweat pies', 4.00)
menu.add_item('Baklava',  4.50)


order = Order()
order += (menu, 'Tartar Monte')
order += (menu, 'Fish Veg')
order += (menu, 'Fish Veg')
order += (menu, 'Baklava')

print(order.order_items) # output : {'Tartar Monte': 1, 'Fish Veg': 2, 'Baklava': 1}