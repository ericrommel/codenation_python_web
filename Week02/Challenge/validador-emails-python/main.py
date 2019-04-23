import re

def valid_email(email):
    ''' This function will valid a given email, based on follow requirement:
    # - Deve ter o tipo de formato username@websitename.extension
    # - Group 1: O nome de usuário só pode conter letras, dígitos e os caracteres -, . e _
    # - Group 2: O nome do site só pode ter letras e dígitos
    # - Group 3: O comprimento máximo da extensão é 1, 2, 3 caracteres
    '''
    return re.search(r'^[\w._-]+@[\w.]+\.[\w]{1,3}$', email)

def filter_email(emails):
    return list(email for email in emails if valid_email(email))  # It is equivalent to "list(filter(valid_email, emails))"
