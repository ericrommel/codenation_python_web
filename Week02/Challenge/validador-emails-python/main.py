import re

def valid_email(email):
    ''' This function will valid a given email, based on follow requirement:
    # - Deve ter o tipo de formato username@websitename.extension
    # - Group 1: O nome de usuário só pode conter letras, dígitos e os caracteres -, . e _
    # - Group 2: O nome do site só pode ter letras e dígitos
    # - Group 3: O comprimento máximo da extensão é 1, 2, 3 caracteres
    '''

    match = re.search(r'([\w\._-]+)@([\w]+)\.([\w]+)', email)
    if match and email.count('@') == 1:
        if match.group(1) and match.group(2) and match.group(3):
            if len(match.group(3)) <= 3:
                return True

    return False


def filter_email(emails):
    aux = []
    for email in emails:
        if valid_email(email):
            aux.append(email)

    return aux
