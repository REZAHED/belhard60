# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза
number = [1, 2 , 5 , 6 , 8 , 4 , 7, 15, 12]
for i in range(0,len(number)-1):
    for j in range(0,len(number)-i-1):
        number[j],number[j+1] = number[j+1],number[j]
print(number)