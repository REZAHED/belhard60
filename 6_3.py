# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]
lst = [1, 2, 3, 4, 5, 6, 7]
number = int(input("Ведите число: "))
lst2=[]
for i in range(len(lst)-number,len(lst)):
    lst2.append(lst[i])
for i in range(0,len(lst)-number):
    lst2.append(lst[i])
print(lst2)
