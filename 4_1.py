#Заполнить список степенями числа 2 (от 2^1 до 2^n).

number = int(input("введите число: "))
lst = [2**i for i in range(1, number+1)]
print(lst)

