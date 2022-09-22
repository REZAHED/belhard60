# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int
number = int(input("введите число: "))
lst = []


def binar(numb : int) -> bin:
    text = ""
    lst.clear()
    while numb:
        lst.append(numb % 2)
        numb //= 2
    for i in range(len(lst)-1,-1,-1):
        text += str(lst[i])
    return text


def decimal(lst:list) -> int:
    decim = 0

    for i in range(len(lst)-1,-1,-1):

        if lst[i] != 0:
            decim += 2 ** i
    return decim


print(f"число {number} в двоечной системе равно {binar(number)}")
print(f"число {binar(number)} в двоечной системе равно {decimal((lst))}")

