import re

# Task 1
def check_text(text):
    pattern = r'Rb{3,}r'
    res = re.findall(pattern, text)
    if res:
        return res
    return 'pattern not found'

print (check_text('RbbbrfgdhcnnRbbbbbbbrdgevevwsnbRdefhrRbbbbbbbbbbbr'))

# Task 2
def credit_card(card_number):
    if re.match(r'^(\d{4}-){3}(\d{4})$', card_number):
        return True
    return False

# Task 3
def check_email(email):
    if re.match(r'^[a-zA-Z0-9_]+[-]?[a-zA-Z0-9_]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return True
    return False

# Task 4
def check_login(login):
    if re.match(r'^[a-zA-Z0-9]{2,10}$', login):
        return True

    
