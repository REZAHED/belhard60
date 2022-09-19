# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе число

first_number = float(input("введите первое число:  "))
operation = input("выберите действие : (+  -  *  /  ^) ")
oper = ["+", "-", "*", "/", "^"]
while operation not in oper:
        print("неправильно выбрано действие")
        operation = input("Пожалуйста выберите действие : (+  -  *  /  ^) ")
else:

    second_number = float(input("введите второе число:  "))

if operation == "+":
    print("\n" + f"Результат  {first_number} +"
                 f" {second_number}  =  {first_number + second_number}")

elif operation == "-":
    print("\n" + f"Результат  {first_number} +"
                 f" {second_number}  =  {first_number - second_number}")
elif operation == "*":
    print("\n" + f"Результат  {first_number} +"
                 f" {second_number}  =  {first_number * second_number}")
elif operation == "/":
    print("\n" + f"Результат  {first_number} +"
                 f" {second_number}  =  {first_number / second_number}")
elif operation == "^":
    print("\n" + f"Результат  {first_number} +"
                 f" {second_number}  =  {first_number ** second_number}")



