import random

# if num==1:
# lst=[i for i in range(1,10)]
# print(lst)
# else:
lst2 = []
lst3 = []
lst4 = []
while len(lst2) < 3:
    for i in range(3):

        numb = random.randint(1, 9)

        if numb not in lst2:
            lst2.append(numb)

while len(lst3) < 3:
    for i in range(3):

        numb2 = random.randint(1, 9)

        if numb2 not in lst2 and numb2 not in lst3:
            lst3.append(numb2)


while len(lst4) < 3:
    for i in range(3):

        numb3 = random.randint(1, 9)

        if numb3 not in lst2 and numb3 not in lst3 and numb3 not in lst4:
            lst4.append(numb3)

            # if numb not in lst2 :
#  for i in range(1,4):
#   if i  in lst2:
#    i+=1
#  else:
#     lst2.append(numb)
#    else:
#      numb=random.randint(1,9)

print(lst2)
print(lst3)
print(lst4)

# if num ==9 :
# num2 = 1
# else:
# num2 = num+3
# print(num2)


#
# lst3=[i for i in range(num2,10)]
# print(lst3)


# while len(lst3)<9:
#  for i in range(1,10):
#   if i  in lst3:
#    i+=1
#   else:
#    lst3.append(i)
#
# print(lst3)
#