# Код Морзе для представления цифр и букв использует тире и точки. Напишите
# функцию для кодирования текстового сообщения в соответствии с кодом Морзе.
# (словари в помощь)

text = input("введите текст: ").upper()
dic = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-." }
lst=[]
for i in range(len(text)):
    if text[i] not in dic:
        lst.append("")
    else:
        lst.append(dic[text[i]])
print(" ".join(lst))