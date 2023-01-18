'''
Написати конструкцію try ... except ... else ... finally, яка буде робити точно те ж,
що і менеджер контексту із попереднього завдання.'''


my_list = {}

try:
    # Код в якому ловимо помилки
    print(10 * '=')
    k = 5 / 4
    #k = 5+'gdf'
    #print(my_list['error'])


except AttributeError:
    print(' Custom exception is occured - AttributeError')
except ArithmeticError:
    print(' Custom exception is occured - ArithmeticError')
except EOFError:
    print(' Custom exception is occured - EOFError')
except NameError:
    print(' Custom exception is occured - NameError')
except LookupError:
    print(' Custom exception is occured - LookupError')
except StopIteration:
    print(' Custom exception is occured - StopIteration')
except OSError:
    print(' Custom exception is occured - OSError')
except TypeError:
    print(' Custom exception is occured - TypeError')
except ValueError:
    print(' Custom exception is occured - ValueError')

# можна і більш глобально -але тоді не вкажемо тип помилки
#except Exception:
#    print ('Error')

else:
    print('No error')

finally:
    print('The end')
    print(10 * '=')