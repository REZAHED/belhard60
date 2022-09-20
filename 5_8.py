# 1. Вводится строка, вывести из строки только цифры
text = input("введите текст")
for i in range(0, len(text)):
   if text[i].isdigit():
       print(text[i])
