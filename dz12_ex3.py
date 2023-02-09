# 3. В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл.

import time


class MyCustomException:
    def __enter__(self):
        # print('start')
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        file = open('error.log', 'a')
        if exc_type is None:
            file.write(f'Not error. Start -  {time.asctime()}\n')
            # print('Not error')
        else:
            file.write(f'error -  {exc_val} . Start -  {time.asctime()}\n')
            # print(f'error -  {exc_val} . type{exc_type}. tb {exc_tb} Start -  {time.asctime()}')
        file.close()
        return True


with MyCustomException():
    # місце перевірки помилок
    # print('start my')
    k = 5 / 0
