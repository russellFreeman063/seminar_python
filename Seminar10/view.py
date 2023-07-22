import text
from model import PhoneBook

def show_menu() -> int:
    for i, item in enumerate(text.main_menu):
        if i:
            print('\t' + f'{i}. {item}')
        else:
            print(item)
    select_option = input('Выберете пункт меню: ')
    while True:
        if select_option.isdigit() and 0 < int(select_option) < len(text.main_menu) - 1:
            return int(select_option)
        select_option = input(text.main_menu_input_error)
        
def show_contact(book: PhoneBook, msg: str):
    if book:
        max_n, max_p, max_c = book.calculation_max_field()
        print('\n' + '=' * (7+max_p+max_c+max_n))
        for uid, contact in book.phone_book.items():
            print(f'{uid: >3}. {contact.to_show(max_n, max_p, max_c)}')
        print('=' * (7+max_p+max_c+max_n) + '\n')
    else:
        print_msg(msg)
    
def print_msg(msg: str):
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n')
        
def input_new_contact(input_list: list[str]):
    new_contact = []
    for item in input_list:
        new_contact.append(input(item))
    return new_contact

def input_data(msg: str) -> str:
    return input(msg)

def input_number(msg: str) -> int:
    while True:
        number = input(msg)
        if number.isdigit():
            return int(number)
        
