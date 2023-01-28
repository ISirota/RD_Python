'''
Написати конструкцію try ... except ... else ... finally, яка буде робити точно те ж,
що і менеджер контексту із попереднього завдання.'''


my_list = {}

try:
    # Код в якому ловимо помилки
    print(10 * '=')
    k = 5 / 4
    #k = 5+'gdf'
    #print(my_list[gf])

except Exception as e:
    print(f'{e}')
else:
    print('No error')

finally:
    print(10 * '=')

