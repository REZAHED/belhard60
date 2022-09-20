# Вводится число N, вывести первые N чисел последовательности Фибоначи

number = int(input("введите число: "))
fibo = [0, 1]
for i in range(0, number-2):
    fibo.append(fibo[i] + fibo[i+1])
print(fibo)
