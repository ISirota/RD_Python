# 2. Написати декоратор, який буде записувати в файл назву функції, яку він декорує, і писати час її виклику.

import time


def decor(func):
    # декоратор виконує друк назви функції і часу, коли вона була викликана.
    def wrap(*args, **kwargs):
        rezult = func(*args, **kwargs)
        with open('log_decor.log', 'a+') as file:
            file.write(f'Function name < {func.__name__} > start time - {time.asctime()}')
            file.write('\n')
        return rezult

    return wrap


@decor
def erer():
    print('function erer')


@decor
def bugers(a, name):
    # function bugers
    print(a, name)


erer()
time.sleep(3)
bugers(34, name='bug')
