# Classwork property
from datetime import datetime


class Student:
    def __init__(self, first_name, last_name, birth_date):
        self._first_name = first_name
        self._last_name = last_name
        self._birth_date = birth_date

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str) or not value.istitle():
            raise ValueError
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str) or not value.istitle():
            raise ValueError
        self._last_name = value

    @property
    def age(self):
        birth_date = datetime.strptime(self._birth_date, "%d-%m-%Y")
        today = datetime.now()
        age = int(today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day)))
        if not 18 <= age <= 100:
            raise ValueError('Age must be greater than 18 and less then 100')
        age = self._birth_date
        return age


st = Student('Yuriy', 'Barabash', '29-08-2007')

print(st.first_name)

print(st.age)

