# домашнє завдання до заняття № 7.
'''1. Створити телефонну книгу, яка матиме наступні команди:
stats: кількість записів
add: додати запис
delete <name>: видалити запис за іменем (ключем)
list: список всіх імен в книзі
show <name>: детальна інформація по імені
Записи не мають повторюватися, заборонено перезаписувати записи, тільки видаляти і додавати заново. '''

telefon_book = {}

while True:
    command_input  = input (' Введіть команду (stats, add, delete, list, show):  ')
    if command_input == 'stats':
        print ('Кількість записів' , len(telefon_books))
    elif command_input == 'add':
        new_name = input("введіть ім'я нового запису: ")
        if telefon_book.get(new_name) != None:
            print(' Запису під іменем ', new_name , 'у телефонній книзі існує. Ви не можете змінити номер. Рекомендую видалити запис та додати новий.')
        else:
            new_fone = input("введіть номер телефону: ")
            telefon_book[new_name] = new_fone
    elif command_input == 'delete':
        old_name = input("введіть ім'я  запису, що видаляємо : ")
        if telefon_book.get(old_name) == None:
            print(' Запису під іменем ', old_name , 'у телефонній книзі не існує.')
        else:
            telefon_book.pop(old_name)
            print ('видалено запис для ', old_name)
    elif command_input == 'list':
        print (*list(telefon_book.keys()),sep="\n")
    elif command_input == 'show':
        show_name = input("введіть ім'я  запису, який Вас цікавить : ")
        if telefon_book.get(show_name) == None:
            print(' Запису під іменем ', show_name , 'у телефонній книзі не існує.')
        else:
            print ('номер телефону для ' ,show_name, ' - ',telefon_book.get(show_name))
    else:
        print ('  Я не знаю такої команди.')
