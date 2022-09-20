# Вводятся две строки, a и b, и возвращать количество раз,
# когда в обеих строках под одинаковыми индексами стоит одна и та же пара букв.

first = input("введите текст: ").lower()
second = input("введите второй текст: ").lower()
first2 = first.replace(" ","")
second2=second.replace(" ","")
c = 0
for i in range(0,len(first2)):
    if len(first2)<=len(second2):
        if first2[i] == second2[i]:
            c += 1
            print(f"Буква {first2[i]} Индекс:{i}", end=" ")
    else:

print("\n", "количество одинаковых пар: ",c)
# else:
#     for i in range(0,len(second2)):
#         if first2[i] == second2[i]:
#             c += 1
#             print("Буква",first2[i]," Индекс:",i," ", end=" ")
#     print("\n", "количество одинаковых пар: ",c)


