class User:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        super().__setattr__(first_name, last_name)

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    def __setattr__(self, name, value):
        if name in ('first_name', 'last_name'):
            raise AttributeError("Cannot directly set 'first_name' or 'last_name'")
        super().__setattr__(name, value)

    def __getattr__(self, name):
        raise AttributeError(f"'User' object has no attribute '{name}'")


user = User("Yuriy", "Barabash")
print(f'{user.first_name} {user.last_name}')

try:
    user.first_name = "Alex"
except AttributeError as err:
    print(err)

try:
    user.date_of_birth
except AttributeError as err:
    print(err)
