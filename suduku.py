import random

num = random.randint(1, 9)
#print(num)
# if num == 1:
#     lst = [i for i in range(1, 10)]
#     print(lst)
#
# else:
lst2 = [i for i in range(num, 10)]
if len(lst2) == 9:
    print(lst2)
else:
    while len(lst2) < 9:
        for i in range(1, 10):
            if i in lst2:
             i += 1
            else:
                lst2.append(i)

    print(lst2)
    #print(lst2[0])
if num == 9 or num ==8 or num == 7:
    num2 = 3
else:
    num2 = num + 3

    #print(num2)

lst3 = [i for i in range(num2, 10)]
# print(lst3)

while len(lst3)<9:
    for i in range(1,10):
        if i in lst3:
            i+=1
        else:
            lst3.append(i)

print(lst3)
