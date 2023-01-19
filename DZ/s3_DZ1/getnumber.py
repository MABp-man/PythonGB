
def get_number(ask_user):
    print(ask_user)
    if 'целое' or 'натуральное' and 'число' in ask_user:
        return int(input())
    elif 'любое число' in ask_user:
        return float(input())
    else:
        return input()