from abc import ABC, abstractmethod


class PaymentBase(ABC):
    @abstractmethod
    def create_payment(self, amount):
        pass


class WithCard(PaymentBase):
    def create_payment(self, amount):
        print(f'Payment of {amount} euro via Credit Card')


class BankTransfer(PaymentBase):
    def create_payment(self, amount):
        print(f'Payment of {amount} euro via Bank Transfer')


class GooglePay(PaymentBase):
    def create_payment(self, amount):
        print(f'Payment of {amount} euro via Google Pay')


class PaymentProcessor:
    def __init__(self):
        self.pay_methods = []

    def add_pay_method(self, pay_method):
        self.pay_methods.append(pay_method)

    def process_pay(self, amount, pay_method_index):
        if 0 <= pay_method_index < len(self.pay_methods):
            selected_method = self.pay_methods[pay_method_index]
            selected_method.create_payment(amount)
        else:
            raise IndexError(f'Invalid payment method INDEX , mast be from 0 to {len(self.pay_methods)-1}')


credit_card = WithCard()
bank_transfer = BankTransfer()
google_pay = GooglePay()

payment_processor = PaymentProcessor()
payment_processor.add_pay_method(credit_card)
payment_processor.add_pay_method(bank_transfer)
payment_processor.add_pay_method(google_pay)

payment_processor.process_pay(210, 1)
payment_processor.process_pay(315, 2)
