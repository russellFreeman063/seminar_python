import view
import model
import text

def search_modul():
    word = view.input_data(text.input_search_word)
    result = model.search(word)
    view.show_contact(result, text.empty_search(word))
    return result
    
def start():
    main_phone_book = model.PhoneBook()
    while True:
        user_select = view.show_menu()
        match user_select:
            case 1:
                main_phone_book.open_file()
                view.print_msg(text.load_successful)
            case 2:
                main_phone_book.save_file()
                view.print_msg(text.save_successful)
            case 3:
                view.show_contact(main_phone_book, text.empty_book)
            case 4:
                contact = view.input_new_contact(text.fields_new_contact)
                main_phone_book.input_contact(contact)
                view.print_msg(text.new_contact_successful(contact[0]))
            case 5:
                search_modul()
            case 6:
                if search_modul():
                    uid = view.input_number(text.input_rename_uid)
                    rename = view.input_new_contact(text.fields_rename_contact)
                    main_phone_book.change_contact(uid, rename)
                    view.print_msg(text.rename_successful(name))
            case 7:
                if search_modul():
                    uid = view.input_number(text.input_del_uid)
                    name = main_phone_book.delete_contact(uid)
                    view.print_msg(text.contact_deleted(name))
            case 8:
                if main_phone_book.phone_book != main_phone_book.original_phone_book:
                    answer = view.input_data(text.save_changes)
                    if answer == 'y':
                        main_phone_book.save_file()
                        view.print_msg(text.save_successful)
                view.print_msg(text.good_bay)
                break