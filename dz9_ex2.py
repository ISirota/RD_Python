# інтератор числа Фібоначчі
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for nom in range(2, n+1):
            a, b = b, a + b
        return b

n = int(input("Ведіть порядковий номер елемента послідовності Фібоначчі "))

print("Елемент послідовності Фібоначчі за порядковим номером ", n, ' = ', fib(n))

