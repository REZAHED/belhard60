a = int(input("1 : "))
b = int(input(" 2: "))
c=0
for i in range(1,(a*b)+1):
    print(i, end=' ')
    c+=1
    if c==6:
        print()
        print("\t" * 6)

