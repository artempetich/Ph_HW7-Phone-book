def show_menu():
    print("\nВыберите пункт меню:")
    menu = ["Показать все контакты", "Открыть файл", "Сохранить файл", "Новый контакт",
            "Изменить контакт", "Удалить контакт", "Найти контакт", "Выйти из программы"]
    for i in range(len(menu)):
        print("\t{}. {}".format(i+1, menu[i]))
    while True:
        try:
            number = int(input("Введите число: "))
            if 1 <= number <= len(menu):
                return number
            else:
                print("Нет такого пункта")
        except:
            print("Введите цифру")


def show_contacts(phone_book: list, flag: str):
    if len(phone_book) > 0:
        for item in phone_book:
            print(f"{item[0]} {item[1]} ({item[2]})")
    elif flag == 'all':
        print('Телефонная книга пуста или не загружена')
    elif flag == 'find' or flag == 'change':
        print('Ничего не найдено')


def load_success():
    print('Телефонная книга загружена успешно')


def save_success():
    print('Телефонная книга записана успешно')


def delete_approve():
    choose = input("Удалить найденные контакты? (1 - да, 2 - нет) ")
    return choose


def delete_success(flag: int):
    if flag == '1':
        print('Контакт удален успешно')
    elif flag == '2':
        print('Отмена удаления')


def new_contact():
    name = input("Введите имя и фамилию контакта: ")
    phone = input("Введите номер телефона: ")
    comment = input("Введите комментарий к контакту: ")
    return name, phone, comment


def find_contact(flag: str):
    if flag == 'find':
        search = input('Введите искомое значение: ')
    elif flag == 'del':
        search = input('Введите контакт для удаления: ')
    elif flag == 'change':
        search = input('Введите контакт для изменения: ')
    return search


def many_contacts():
    print('Найдено больше 1 контакта для изменения. Уточните поиск')


def change_contact():
    print('Введите новые данные контакта. Ничего не вводите, если не нужно изменять данное поле')


def phone_book_changes():
    print('Текущая телефонная книга отличается от исходной')
    return int(input("Сохранить изменения? (1 - да, 2 - нет): "))