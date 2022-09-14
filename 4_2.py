#Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры
text = input("введите текст: ")
text_nospace = text.replace(" ", "")
lst = [text_nospace.lower()[i] for i in range(0, len(text_nospace))]
dic_number = {lst[i]: lst.count((lst[i])) for i in range(0, len(text_nospace))}

print(dic_number)



