# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int
number = int(input("введите число: "))
lst = []


def binar(number : int) -> bin:
    decim = 0
    while number:
        lst.append(number % 2)
        number //= 2

    for i in range(len(lst)-1, -1, -1):
        print(lst[i], end="")
    print()

    for i in range(0, len(lst)):
        if lst[i] != 0:
            decim += 2 ** i
    print(decim)


binar(number)



