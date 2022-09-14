import random

# if num==1:
# lst=[i for i in range(1,10)]
# print(lst)
# else:
lst2 = []
for i in range(1, 9):

    numb = random.randint(1, 9)

    if numb not in lst2:
        lst2.append(numb)

    while len(lst2) < 9:
        if numb not in lst2:
            # for i in range(1,10):
            #   if i  in lst2:
            #    i+=1
            #  else:
            lst2.append(numb)
        else:
            numb = random.randint(1, 9)

print(lst2)



lst3 = []
for i in range(1, 9):

    numb = random.randint(1, 9)

    if numb  != lst2[0]:
        while len(lst3) < 9 and numb not in lst3:
            lst3.append(numb)
    else:
        while len(lst3) < 9:
         if numb not in lst3 and numb != lst2[0]:
            # for i in range(1,10):
            #   if i  in lst2:
            #    i+=1
            #  else:
            lst3.append(numb)
         else:
            numb = random.randint(1, 9)

print(lst3)



# lst4 = []
# for i in range(1, 9):
#
#     numb = random.randint(1, 9)
#
#     if numb not in lst4:
#         lst4.append(numb)
#
#     while len(lst4) < 9:
#         if numb not in lst4:
#             # for i in range(1,10):
#             #   if i  in lst2:
#             #    i+=1
#             #  else:
#             lst4.append(numb)
#         else:
#             numb = random.randint(1, 9)
#
# print(lst4)