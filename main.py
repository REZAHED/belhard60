# number = input("введите число: ")

def foo(number):
    while len(number) > 1:
        s=0
        for i in number:
            s+= int(i)
        number = str(s)
    return int(number)
print(foo("759"))


