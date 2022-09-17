# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе число

first_number = float(input("введите первое число:  "))
operation = input("выберите действие : (+  -  *  /  ^) ")
while True:
    if operation != "+" and  operation != "-" and operation != "*"\
            and operation != "/" and operation != "^":
        print("неправильно выбрано действие")
        operation = input("выберите действие : (+  -  *  /  ^) ")
        continue
    else:
        break

second_number = float(input("введите второе число:  "))

if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    print(first_number / second_number)
elif operation == "^":
    print(first_number ** second_number)



