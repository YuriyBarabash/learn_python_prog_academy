# Task 1
import re

def credit_card(card_number):
    if re.match(r'^(\d{4}-){3}(\d{4})$', card_number):
        return True
    return False

