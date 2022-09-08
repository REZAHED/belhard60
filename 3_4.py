# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных
first_number = input("Введите первое число: ")
second_number = input("Введите второе число: ")
third_number = input("Введите третье число: ")
text = first_number.startswith("-") + second_number.startswith("-") + third_number.startswith("-")
text_2 = first_number.count("0") + second_number.count("0") + third_number.count("0")
print("количество положительных чисел:", 3 - int(text) - int(text_2), "\nколичество отрицательных чисел:", text)
print("количество число 0: ", text_2)




