# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных
first_number = input("Введите первое число: ")
second_number = input("Введите второе число: ")
third_number = input("Введите третье число: ")
text = first_number.startswith("-")+second_number.startswith("-")+third_number.startswith("-")
print("количество положительных чисел:", 3-int(text),"\nколичество отрицательных чисел:",text)



