# Дан список чисел, отсортировать его по возрастанию без использования sort и sorted
number = [2, 2, 6, 4, 8, 1, 5, 16, 3, 9, 12, 7 , 45, 13, 76, 4]
number_lst = []
for i in range(0,len(number)):
    number_lst.append(min(number))
    number.pop(number.index(min(number)))
print(number_lst)



