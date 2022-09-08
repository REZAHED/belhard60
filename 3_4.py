# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных
first_number = input("Введите первое число: ")
second_number = input("Введите второе число: ")
third_number = input("Введите третье число: ")
text = first_number.startswith("-") + second_number.startswith("-") + third_number.startswith("-")
first_number1 = float(first_number)
second_number1 = float(second_number)
third_number1 = float(third_number)
sum_0 = int(first_number1 == 0) + int(second_number1 == 0) + int(third_number1 == 0)
print("количество положительных чисел:", 3 - text - sum_0, "\nколичество отрицательных чисел:", text)
print("количество число 0: ", sum_0)





