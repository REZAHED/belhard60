import json
from pprint import pprint

dic_en_rus = {}
text=""


class OpenFile:

    @staticmethod
    def opening_read(self):
        with open(self, 'r', encoding='utf-8-sig') as file:
            return file.read()

    @staticmethod
    def opening_json(self):
        with open(self, 'r', encoding='utf-8-sig') as file:
            return json.load(file)

read=OpenFile()
if read.opening_read('dictionary.json'):
    dic_en_rus = read.opening_json('dictionary.json')

if __name__ == "__main__":
    pprint("Welcome to my firt English-Russian Dictionary")
    text = input("Введите слово для перевода:-> ").lower().strip()


def dic_to_file(word, translate):
    dic_en_rus.update({word: translate})
    with open('dictionary.json', 'r+', encoding='utf-8') as file:
        json.dump(dic_en_rus, file, indent=2, ensure_ascii=False)
    return f'слово {word.upper()} и его значение {translate.upper()} успешно сохранены.'


def checking(dic):
    if text in dic.keys():
        print('\n' + f'перевод слово на русский: -> ' + dic[text])
        # start()
    else:
        print("Данное слово не найдено!! \nВведите его значение для записи в словарь:")
        text_translate = input().lower().strip()
        print(dic_to_file(text, text_translate))


def read_dictionary(word):
    dic = {}

    if not read.opening_json('dictionary.json'):
        print("словарь пустой\n" + f'Введите значение слово {word} для записи в словарь:')
        translate = input().lower().strip()
        print(dic_to_file(word, translate))
    else:
        dic = read.opening_json('dictionary.json')
    return checking(dic)

if __name__ == "__main__":
    read_dictionary(text)

# start()

# def start():
#
#     text = input("Введите слово для перевода: ").lower().strip()
#     return text

