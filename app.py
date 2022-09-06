name = input("Как тебя зовут? ")
letter = "буквы"
letter2 = "букв"
list = []
def func(name):
    i = len(name)
    conut = 0
    if ' ' in name:
        for i in name:
            list.append(i)
            print(i)
        print("""_________________________________________""")
        print(list)
        for space in list:
            if space == ' ':
                conut += 1
        if len(name) <= 4:
            print("длина этого имя состоит из ", len(name)-conut, letter)
        else:
            print("длина этого имя состоит из ", len(name)-conut, letter2)

    else:
        for i in name:
            print(i)

        if len(name) <= 4:
            print("длина этого имя состоит из ", len(name)-conut, letter)
        else:
            print("длина этого имя состоит из ", len(name)-conut, letter2)

func(name)



