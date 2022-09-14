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
    print("full",lst2)
else:
    while len(lst2) < 9:
        for i in range(1, 10):
            if i in lst2:
             i += 1
            else:
                lst2.append(i)

    print("adde",lst2)
    #print(lst2[0])
if num == 7:
    num2 = 1
elif num == 8:

    num2 = 2
elif num ==9:
    num2 = 3
else:
    num2 = num+3

    #print(num2)

lst3 = [i for i in range(num2, 10)]
# print(lst3)
if num2==1:
    print(lst3)
else:
    while len(lst3)<9:
        for i in range(1,10):
            if i in lst3:
                i+=1
            else:
                lst3.append(i)

    print("secound",lst3)



if num == 7 :
    num3 = 1
elif num == 8:
    num3 =2
elif num == 9:
    num3 = 6
else:
    num3=num2+3

    #print(num2)

lst4 = [i for i in range(num3, 10)]
if num3==1:
    print(lst4)
# print(lst3)
# while lst4[0] == lst2[0] or lst2[1] or lst2[3] or lst3[0] or lst3[1] or lst3[3] :
#     lst4[0] =random.randint(1,9)
#     print("find")
#     # lst4[0]+=1
    # if lst4[0] >9:
    #     lst4[0]=1
    # else:

while len(lst4)<9:
    for i in range(1,10):
        if i in lst4:
            i+=1
        else:
            lst4.append(i)

print(lst4)
