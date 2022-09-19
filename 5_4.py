number = int(input("введите число:  "))
n_factorial = 1
k_factorial = 1
a=1
b=1
k=0
for i in range(2, number + 1):
    n_factorial *= i

    k_factorial *= i-1

print((n_factorial/n_factorial)* (a**(number-k)*b**k))
print(k_factorial)


# n_k=number
# k=0
# for i in range(0,number):   # для расчета N!
#     if (number - 1 - i)>0:
#         number2 *= (number - 1 - i)
#         n_k *= (number - k - 1)
#         k += 1
#
#
#
#     print(n_k)
    # else:
    #     # print(number2)
    #     # print(n_k)




# for i in range(0,number+1):
#     number2=number*(number-1-i)