# Вводятся две строки, a и b, и возвращать количество раз,
# когда в обеих строках под одинаковыми индексами стоит одна и та же пара букв.

first = input("введите текст: ")
second = input("введите второй текст: ")
c=0
for i in range(0,len(first)):
    if len(first) <= len(second):
        if first[i] == second[i]:
            c+=1
            print(first[i], end=" ")
print("\n", c)
