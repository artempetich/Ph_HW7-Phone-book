phone_book = []
path = 'base.txt'


def get_phone_book():
    global phone_book
    return phone_book


def set_phone_book(PB: list):
    global phone_book
    phone_book = PB


def update_phone_book(contact: list):
    global phone_book
    phone_book.append(contact)


def open_file():
    phone_book = []
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            phone_book.append(line.strip().split(';'))
    return phone_book


def save_file():
    global phone_book
    global path
    data = []
    for line in phone_book:
        data.append(';'.join(line))
    with open(path, 'w', encoding='UTF-8') as file:
        data = file.write('\n'.join(data))


def search_contact(search: str):
    global phone_book
    search_result = []
    for contact in phone_book:
        for field in contact:
            if search in field:
                search_result.append(contact)
                break
    return search_result


def delete_contact(delete_contact: list, choose: str):
    global phone_book
    if choose == '1':
        for line in delete_contact:
            if line in phone_book:
                phone_book.remove(line)


def change_contact(contact: list, contact_changed: list):
    global phone_book
    for i in range(len(phone_book)):
        if phone_book[i] == contact[0]:
            for j in range(len(phone_book[i])):
                if contact_changed[j] != "":
                    phone_book[i][j] = contact_changed[j]


def change_check(phone_book_file: list):
    global phone_book
    if phone_book_file != phone_book and len(phone_book) > 0:
        return "yes"
    else:
        return 'no'