# Вводятся две строки, a и b, и возвращать количество раз,
# когда в обеих строках под одинаковыми индексами стоит одна и та же пара букв.

first = input("введите текст: ").lower().replace(" ","")
second = input("введите второй текст: ").lower().replace(" ","")
c = 0
len_ = 0
for i in range(0, min(len(first),len(second))):
  if first[i] == second[i]:
    c += 1
    print(f"Буква {first[i]} Индекс:{i}", end=" ")
print("\n", "количество :",c)



