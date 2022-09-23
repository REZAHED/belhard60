# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные
import random
from random import randint
number = []


def rand(number:list):          # создать рандомный список
    number.clear()
    for i in range(0, 10):
        number.append(random.randint(0, 100))
    return number

def odd():
    print(f"первоначвльный рандомный список :{rand(number)}")
    number2 =[]
    number2 = list(filter(lambda x:x%2==0 ,(number)))

    for i in range(0,len(number)):
        if number[i]%2:
            number2.append(number[i])
    return number2

print("\t"*4,f"отсортированный:{odd()}")