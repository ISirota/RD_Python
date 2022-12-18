# домашнє завдання 1 до заняття № 5 .

txt = input (' Введіть текст:  ')
for char in txt:
    print(char, type(char))
    if char.isdigit():
        print(' Ви ввели число.')
        if int(char)%2 == 0 :
            print (' І це число парне. ')
        else:
            print (' І це число не парне. ')
    elif char.isalpha():
        if char.isupper():
            print(' Ви ввели велику літеру - ',char)
        else:
            print(' Ви ввели малу літеру - ',char)
    else:
        print(' Ви ввели символ - "', char,'"')
