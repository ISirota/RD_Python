'''
Написати кастомний Exception клас, MyCustomException, який має повідомляти "Custom exception is occured".

Написати власний менеджер контексту, задачею якого буде друкувати "==========" – 10 знаків дорівнює
перед виконанням коду та після виконання коду, таким чином виділяючи блок коду символами дорівнює.

У випадку виникнення будь-якої помилки вона має бути надрукована текстом, проте програма не має завершити своєї роботи.'''


class MyCustomException:
    def __enter__(self):
        '''Пише 10 знаків дорівнює'''
        print(10*'=')

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''Перевіряє на виникнення помилки  та пише 10 знаків  дорівнює '''
        if exc_type != None:
            print('Виникла помилка ', exc_type)
        print(10 * '=')
        return True


my_list ={}

with MyCustomException():
    print(my_list['error'])
    print('Custom exception is occured')
