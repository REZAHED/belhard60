# 2. Вводится цисло, вывести таблицу умножения от 1 до 10 на это число
number = int(input("введите число: "))
for i in range(1,11):
    number2 = number * i
    print(number2)
