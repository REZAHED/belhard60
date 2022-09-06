letter = "буквы"
letter2 = "букв"
list = []
def countin():
    list.clear()
    counti = input(" Хотите продолжить? y/n ")
    if counti == 'y':
        func()
    elif counti == 'n':
        print("Спасибо")
        exit()
    elif counti == '':
        countin()

    else:
        countin()

def func():
    name = input("Как тебя зовут? ")
    if name == '':
        func()
    i = len(name)
    conut = 0
    if ' ' in name:
        for i in name:
            list.append(i)
            print(i)
        print("""_________________________________________""")
        for space in list:
            if space == ' ':
                conut += 1
        if len(name) <= 4:
            print("длина этого имя состоит из ", len(name)-conut, letter)
            countin()
        else:
            print("длина этого имя состоит из ", len(name)-conut, letter2)
            countin()

    else:
        for i in name:
            print(i)
        print("""_________________________________________""")
        if len(name) <= 4:
            print("длина этого имя состоит из ", len(name)-conut, letter)
            countin()
        else:
            print("длина этого имя состоит из ", len(name)-conut, letter2)
            countin()
func()





