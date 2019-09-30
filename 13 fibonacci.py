# function to produce fibonacci sequence out of a sequence of numbers
# the fibonacci sequence is when the next number in a list is a sum of two previous numbers
# ex. 1+1=2, then 1 +2 = 3, then 2 + 3 = 5, then 3 + 5 = 8, etc.


def gen_fib():
    global fib
    list_size = int(input("How many fibonacci numbers would you like to generate?: "))
    i = 1
    if list_size == 0:
        fib = []

    elif list_size == 1:
        fib = [1]

    elif list_size == 2:
        fib = [1, 1]

    elif list_size > 2:
        fib = [1, 1]
        while i < (list_size - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib


print(gen_fib())







