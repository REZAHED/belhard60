number = int(input("введите число:  "))
n_factorial = 1
k_factorial = 1
lst1 = []
lst2 = []
c = 0
while c <= number:
    for i in range(2, c + 1):
        n_factorial *= i

    for i in range(0, c + 1):
        k_factorial *= i
        if k_factorial == 0:
            k_factorial = 1
        lst1.append(k_factorial)

    lst2 = lst1[::-1]

    for i in range(0, c + 1):
        print(int(n_factorial // (lst1[i] * lst2[i])), end=" ")
    print()

    # print(c)
    c += 1
    n_factorial = 1
    k_factorial = 1
    lst1.clear()

