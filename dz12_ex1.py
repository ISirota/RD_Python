'''1. Використати файл як базу даних для збереження записів телефонної книги із попередніх завдань.

Ваша телефонна книга, що до цього містилася в dict, має зберігатися у вигляді тексту в JSON форматі.
При закритті програми і повторному відкритті всі попередні дані мають бути доступними.
Підказка: Ви можете використати бібліотеку json, яка допоможе із перетворенням dict в JSON string (при записі в файл) і JSON string в dict (при читанні із файлу). Файл слід оновлювати після кожної успішної операції add або delete.
'''
import json

with open('telbook.json') as dfile:
    telefon_book = json.load(dfile)

#print (telefon_book)

while True:
    command_input = input(' Введіть команду (stats, add, delete, list, show):  ')
    if command_input == 'stats':
        print('Кількість записів', len(telefon_book))
    elif command_input == 'add':
        new_name = input("введіть ім'я нового запису: ")
        if telefon_book.get(new_name) is not None:
            print(' Запису під іменем ', new_name, 'у телефонній книзі існує. ')
            print(' Ви не можете змінити номер. Рекомендую видалити запис та додати новий.')
        else:
            new_fone = input("введіть номер телефону: ")
            telefon_book[new_name] = new_fone
    elif command_input == 'delete':
        old_name = input("введіть ім'я  запису, що видаляємо : ")
        if telefon_book.get(old_name) is None:
            print(' Запису під іменем ', old_name, 'у телефонній книзі не існує.')
        else:
            telefon_book.pop(old_name)
            print('видалено запис для ', old_name)
    elif command_input == 'list':
        print(*list(telefon_book.keys()), sep="\n")
    elif command_input == 'show':
        show_name = input("введіть ім'я  запису, який Вас цікавить : ")
        if telefon_book.get(show_name) is None:
            print(' Запису під іменем ', show_name , 'у телефонній книзі не існує.')
        else:
            print('номер телефону для ', show_name, ' - ', telefon_book.get(show_name))
    else:
        print('  Я не знаю такої команди.')
    #print(telefon_book)
    with open('telbook.json', 'w') as data_file:
        json.dump(telefon_book, data_file, ensure_ascii=False)
