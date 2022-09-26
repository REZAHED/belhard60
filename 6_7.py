# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

number = [2, 4, 6, 7]
for i in range(0, len(number)):
    if i == len(number)-1:
        summ = number[0] + number[i-1]
    else:
        summ = number[i - 1] + number[i + 1]
    print(summ)
