class Account:
    def __init__(self, own_balance):
        self.__setattr__('__balance', own_balance)

    @property
    def balance(self):
        return self.__balance

    def __setattr__(self, name, value):
        if name == '__balance':
            super().__setattr__(name, value)
        else:
            raise AttributeError("Cannot directly modify attributes. Use another methods.")

    def __getattr__(self, name):
        raise AttributeError(f"Current object has no attribute '{name}'")


my_account = Account(own_balance=1000)
print("Own Balance:", my_account.__balance)


try:
    my_account.balance = 1500
except AttributeError as e:
    print(e)

try:
    print(my_account.withdrow)
except AttributeError as e:
    print(e)





