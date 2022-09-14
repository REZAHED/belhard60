# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

number = int(input("введите количетсво : "))
text_keys = input("введите имя: ")

dic_0 = {"name":text_keys+str(i) for i in range(0,number-1)}
print(dic_0)
#dic_1 = {n:{name:email} for n in range(0,n)}