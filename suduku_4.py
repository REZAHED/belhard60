import random


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lst2=[]
lst3 = []
lst4= []
lst_main =[]
lst5 = []
lst6 = []
lst7 = []
lst8 = []
lst9 = []
lst10 = []


a=0
b=0
c=0
d=0
q=0
for i in range(0,3):
    while len(lst2)<3:

        number = random.randrange(0, 9)

        if lst[number] not in lst2:
            lst2.append(lst[number])
    while len(lst3) < 3:
        number = random.randrange(0, 9)

        if lst[number] not in lst3 and lst[number] not in lst2:
            lst3.append(lst[number])
    while len(lst4) < 3:
        number = random.randrange(0, 9)

        if lst[number] not in lst3 and lst[number] not in lst2 and lst[number] not in lst4:
            lst4.append(lst[number])
    while len(lst5) < 3:
        number = random.randrange(0, 9)

        while b <3:

            if (lst[number] not in lst5 and lst[number] != lst4[b] and lst[number] != lst3[b]
            and lst[number] != lst2[b] ):

                lst5.append(lst[number])
                b+=1
            else:
                number = random.randrange(0, 9)

    while len(lst6) < 3:
        number = random.randrange(0, 9)
    #
        while a < 3:

            if (lst[number] not in lst6 and lst[number] != lst5[a] and lst[number] != lst4[a]
            and lst[number] != lst3[a] and lst[number] != lst2[a] and lst[number] not in lst5):
                lst6.append(lst[number])
                a += 1
            else:
                 number = random.randrange(0, 9)
        for i in range(0, 9):
            print(lst[i])
            if lst[i] not in lst6 and lst[i] not in lst5 and lst[i] not in lst7:
                lst7.append(lst[i])

            while len(lst7) < 3:
                print(lst2[i])
                if lst[i] not in lst6 and lst[i] not in lst7 and lst[i] not in lst5:
                   lst7.append(lst[i])
                else:
                    i+=1
    # while len(lst7) < 3:
    #
    #     number = random.randrange(0, 9)
    #
    #     while c < 3:
    #
    #         if (lst[number] not in lst7 and lst[number] not in lst5 and
    #             lst[number] not in lst6 and lst[number] != lst6[c]
    #             and lst[number] != lst5[c] and lst[number] != lst4[c]
    #             and lst[number] != lst3[c] and lst[number] != lst2[c] ):
    #             lst7.append(lst[number])
    #             print(lst7)
    #             c += 1
    #         else:
    #             number = random.randrange(0, 9)
    #             print(number)


    # while len(lst8) < 3:
    #     number = random.randrange(0, 9)
    #
        # while d < 3:
        #
        #     if (lst[number] not in lst8 and lst[number] not in lst7 and lst[number] not in lst5 and
        #             lst[number] not in lst6 and lst[number] != lst7[c] and lst[number] != lst6[c]
        #             and lst[number] != lst5[c] and lst[number] != lst4[c]
        #     and lst[number] != lst3[c] and lst[number] != lst2[c] ):
        #         lst8.append(lst[number])
        #         d += 1
        #     else:
        #          number = random.randint(0,9)



print(lst2)
print(lst3)
print(lst4)
print(lst5)
print(lst6)
print(lst7)
print(lst8)
