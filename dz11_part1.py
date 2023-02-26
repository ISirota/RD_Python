''' Написати власний декоратор, задачею якого має бути друк назви функції і часу, коли вона була викликана.
Декоратор має працювати для різних функцій однаково.'''

import time
def decor(func):
    '''декоратор виконує друк назви функції і часу, коли вона була викликана.'''
    def wrap(*args, **kwargs):
        print(f'Start Function name < {func.__name__} > start time - {time.time()}')
        return func(*args, **kwargs)
    return wrap

@decor
def erer(*args, **kwargs):
    print('function erer')

@decor
def bugers(a, name):
    print(a, name)

erer()
time.sleep(3)
bugers(34, name='bug')
