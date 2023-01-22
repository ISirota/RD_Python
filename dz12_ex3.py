#3. В попередньо написаний кастомний Exception додати запис помилки і час її виникнення у файл.

import time

try:
    # Код в якому ловимо помилки
    # k = 5 / 0
    k = 5+'dfs'
    # print(my_list[gf])

except Exception as e:
    print(f'{e}')
    with open('error.log', 'a') as file:
        file.write(f'{e}' " > start time - ")
        file.write(f'{time.asctime()}')
        file.write('\n')
