# Дан список чисел, отсортировать его по возрастанию без использования sort и sorted
number = [2, 6, 4, 1, 5, 16, 3, 9, 12, 7]
number_sort = set(number)
number_lst = []
for i, j in enumerate(number_sort):
    number_lst.append(j)
print("Input: ", number)
print("Sorted:",number_lst)
