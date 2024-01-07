from math import gcd  # module gcd makes simply fraction , for example --- 7/14 == 1/2


class ProperFraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        common_divisor = gcd(numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


if __name__ == '__main__':
    print('Input values of fraction N 1')
    a1, b1 = int(input('numertor: ')), int(input('denominator: '))
    print('Input values of fraction N 2')
    fraction1 = ProperFraction(a1, b1)

    a2, b2 = int(input('numertor: ')), int(input('denominator: '))
    fraction2 = ProperFraction(a2, b2)

    print(f"Fraction 1: {fraction1}")
    print(f"Fraction 2: {fraction2}")

    sum_result = fraction1 + fraction2
    print(f"Sum: {sum_result}")

    diff_result = fraction1 - fraction2
    print(f"Difference: {diff_result}")

    mul_result = fraction1 * fraction2
    print(f"Multiplication: {mul_result}")

