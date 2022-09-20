# 3. Вводится число, посчитать факториал этого числа
number = int(input("введите число: "))
faktorial = 1
for i in range(2,number+1):
    faktorial *= i
print(faktorial)
