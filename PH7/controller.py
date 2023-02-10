import view
import modules


def start():
    while True:
        choice = view.show_menu()
        match choice:
            case 1:
                phone_book = modules.get_phone_book()
                view.show_contacts(phone_book, 'all')
            case 2:
                if modules.change_check(modules.open_file()) == 'yes':
                    ans = view.phone_book_changes()
                    if ans == 1:
                        modules.save_file()
                        view.save_success()
                modules.set_phone_book(modules.open_file())
                view.load_success()
            case 3:
                modules.save_file()
                view.save_success()
            case 4:
                new = list(view.new_contact())
                modules.update_phone_book(new)
            case 5:
                while True:
                    search = view.find_contact('change')
                    result = modules.search_contact(search)
                    view.show_contacts(result, 'change')
                    if len(result) <= 1:
                        break
                    view.many_contacts()
                view.change_contact()
                contact_result = list(view.new_contact())
                modules.change_contact(result, contact_result)
            case 6:
                aim = view.find_contact('del')
                result = modules.search_contact(aim)
                view.show_contacts(result, 'find')
                choose = view.delete_approve()
                modules.delete_contact(result, choose)
                view.delete_success(choose)
            case 7:
                search = view.find_contact('find')
                result = modules.search_contact(search)
                view.show_contacts(result, 'find')
            case 8:
                if modules.change_check(modules.open_file()) == 'yes':
                    ans = view.phone_book_changes()
                    if ans == 1:
                        modules.save_file()
                        view.save_success()
                break