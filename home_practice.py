import json
from pprint import pprint
import os

import menu
import openfile






text=""
dic_en_rus = {}


test = menu.Menus()
test.show_menu()
# if __name__ == "__main__":
print('\033[33m' +'\033[1m'+ "Welcome to my firt Dictionary")




def dic_to_file(word, translate):
    dic_en_rus.update({word: translate})
    with open('dictionary.json', 'r+', encoding='utf-8') as file:
        json.dump(dic_en_rus, file, indent=2, ensure_ascii=False)
    return f'слово {word.upper()} и его значение {translate.upper()} успешно сохранены.'


def checking(dic):
    if text in dic.keys():
        print('\n' + f'перевод слово на русский: -> ' + '\033[31m' +'\033[1m' + dic[text])

    else:
        print('\033[32m'+"Данное слово не найдено!! \nВведите его значение для записи в словарь:")
        text_translate = input().lower().strip()
        print('\033[34m'+dic_to_file(text, text_translate))


if os.path.exists('dictionary.json'):
    pass
else:
    file = open('dictionary.json', 'a+', encoding='utf-8-sig')
    file.close()


read = openfile.OpenFile()
if read.opening_read('dictionary.json'):
    dic_en_rus = read.opening_json('dictionary.json')
    checking(dic_en_rus)
else:
    print("словарь пустой\n" + f'Введите значение слово {text} для записи в словарь:')
    translate = input().lower().strip()
    print(dic_to_file(text, translate))
