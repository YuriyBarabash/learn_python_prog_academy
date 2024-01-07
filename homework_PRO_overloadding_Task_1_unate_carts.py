class Cart:

    def __init__(self, items=[]):
        self.items = items

    def __iadd__(self, other):
        if isinstance(other, Cart):
            self.items += other.items
            return self
        else:
            raise ValueError("Allowed to merge only with another instance of the Cart class")


cart1 = Cart(items=["apple", "pear"])
cart2 = Cart(items=["milk", "bread"])
cart3 = Cart(items=['tomatos', 'pork'])
cart4 = Cart(items=['potatos', 'milk', 'bread'])

cart1 += cart2
cart2 += cart3
cart3 += cart4

print(cart1.items)
print(cart2.items)
print(cart3.items)

