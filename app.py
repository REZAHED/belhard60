name = input("Как тебя зовут? ")
letter = "буквы"
letter2 = "букв"
def func(name):
    i = len(name)
    conut = 0
    if " " in name:
        conut += 1
        for i in name:
            print(i)
        print("""_________________________________________""")
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



