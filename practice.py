count = 0
sex = "укажите свой пол м\ж? "
sex_correct = "укажите свой пол правильно м\ж? "
age = "укажите свой возраст  "
while count <= 1 :
    sex2 = input(sex)
    if sex2 == 'м' or "ж" :
        print("информация сохранена")
    else :
        sex3 = input(sex_correct)
    age2 = int(input(age))

    if sex2 == "м" and age2 <= 20:
            print("ты еще мальчик")
    elif age2 > 20 and sex2 == "м":
            print('ты уже мужчина')
    if sex2 == "ж" and age2 <= 20:
        print("ты еще девушка")
    elif sex2 == "ж" and age2 > 20:
        print('ты уже женщина')


    count +=1
    if count <= 1:
            print("попробуйте еще раз и укажите другой пол")
else:
    print('Спасибо за ваше участие')