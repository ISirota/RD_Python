# генератор числа Фібоначчі
def fib(n):
   if n == 0:
       yield 0
   elif n == 1:
       yield 1
   else :
        a, b = 0, 1
        for nom in range(n):
            a, b = b, a + b
        yield a


n = int(input("Ведіть порядковий номер елемента послідовності Фібоначчі "))

# print(k)
for i in range(n):
    print(next(fib(i)))
