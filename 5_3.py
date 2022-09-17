# Вывести четные числа от 2 до N по 5 в строку
number_n = int(input("введите число: "))
c = 0
for i in range(2, number_n+1):
    if not i % 2 and c < 5:
        print(i, end=" ")
        c += 1
    elif c == 5:
        print()
        c = 0




