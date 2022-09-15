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

    print(lst3)
#
#
#
if num2 == 7 :
    num3 = 1
elif num2 == 8:
    num3 =2
elif num2 == 9:
    num3 = 3
else:
    num3=num2+3

    #print(num2)

lst4 = [i for i in range(num3, 10)]
# if num3==1:
     # print(lst4)
# # print(lst3)
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


if num3 == 7 :
    num4 = 2
elif num3 == 8:
    num4 =3
elif num3 == 9:
    num4 = 4
else:
    num4=num3+4


lst5 = [i for i in range(num4, 10)]
# if num3==1:
     # print(lst4)
# # print(lst3)
# while lst4[0] == lst2[0] or lst2[1] or lst2[3] or lst3[0] or lst3[1] or lst3[3] :
#     lst4[0] =random.randint(1,9)
#     print("find")
#     # lst4[0]+=1
    # if lst4[0] >9:
    #     lst4[0]=1
    # else:

while len(lst5)<9:
    for i in range(1,10):
        if i in lst5:
            i+=1
        else:
            lst5.append(i)

print(lst5)





if num4 == 7 :
    num5 = 2
elif num4 == 8:
    num5 =3
elif num4 == 9:
    num5 = 4
elif num4 ==1:
    num5= 4
elif num4 == 10:
    num5 = 4

else:
    num5=num4+4


lst6 = [i for i in range(num5, 10)]

     # print(lst4)
# # print(lst3)
# while lst4[0] == lst2[0] or lst2[1] or lst2[3] or lst3[0] or lst3[1] or lst3[3] :
#     lst4[0] =random.randint(1,9)
#     print("find")
#     # lst4[0]+=1
    # if lst4[0] >9:
    #     lst4[0]=1
    # else:

while len(lst6)<9:
    for i in range(1,10):
        if i in lst6:
            i+=1
        else:
            lst6.append(i)

print(lst6)





if num5 == 7 and num4 == 3:
    num6 = 6
    lst7 = [i for i in range(num6, 10)]
elif num5 == 8:
    num6 =3
elif num5 == 9:
    num6 = 4
elif num5 ==1:
    num6= 4
elif num5 == 10:
    num6 = 4

else:
    num6=num5+3


lst7 = [i for i in range(num6, 10,4)]

     # print(lst4)
# # print(lst3)
# while lst4[0] == lst2[0] or lst2[1] or lst2[3] or lst3[0] or lst3[1] or lst3[3] :
#     lst4[0] =random.randint(1,9)
#     print("find")
#     # lst4[0]+=1
    # if lst4[0] >9:
    #     lst4[0]=1
    # else:

while len(lst7)<9:
    for i in range(1,10):
        if i in lst7:
            i+=1
        else:
            lst7.append(i)

print(lst7)