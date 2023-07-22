main_menu = ['Главное меню',
             'Открыть файл',
             'Сохранить файл',
             'Показать контакт',
             'Добавить контакт',
             'Найти контакт',
             'Изменть контакт',
             'Удалить контакт',
             'Выход',]

main_menu_input_error = f'Ошибка ввода! Введите число от 1 до {len(main_menu)-1}: '

empty_book = 'Телефонная книга пуста или не открыта'
load_successful = 'Телефонная книга успешно загружена'
save_successful = 'Телефонная книга успешно сохранена'

fields_new_contact = ['Введите имя контакта: ', 'Введите телефон: ', 'Введите комментарий: ']

def new_contact_successful(name: str) -> str:
    return f'Контакт {name} успешно добавлен!'



input_search_word = 'Что будем искать: '


def empty_search(word: str) -> str: 
    return f'Контакты содержащие "{word}" не найдены'


input_del_uid = 'Введите Id контакта, который хотите удалить: '


def contact_deleted(name: str) -> str:
    return f'Контакт {name} успешно удален'


fields_rename_contact = ['Введите новое имя контакта (или Enter - без изменений): ', 
                         'Введите новый телефон (или Enter - без изменений): ',
                         'Введите новый комментарий (или Enter - без изменений): ']
input_rename_uid = 'Введите Id контакта, который хотите изменить: '


def rename_successful(name: str) -> str:
    return f'Контакт {name} успешно изменен'

save_changes = 'Сохранить изменения перед выходом? (y/n)'
good_bay = 'Досвидание, до новых встреч'