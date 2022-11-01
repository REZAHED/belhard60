import openfile
class Menus():

    def show_menu(self=None):

        print("выбирайте из списка:")
        print("""
        [1] поиск в словаре
        [2] посмотреть записанные слова
        [0] меню
        """)
    def secound_menu(self=None):

        print("Файл пустой!")
        print("выбирайте из списка:")
        print("""
                [0] вернуться в меню

                    """)

    show_menu()
    lst = ['1', '2' , '0']
    start = input('\033[32m' + '\033[1m' + "ваш выбор::-> ").lower().strip()
    while start not in lst:
        start = input('\033[32m' + '\033[1m' + "введите правильный номер:-> ").lower().strip()
    if start == '1':
        text = input('\033[32m' + '\033[1m' + "Введите слово для перевода:-> ").lower().strip()
    elif start == '2':
         read = openfile.OpenFile()
         print('\033[32m' + '\033[1m' + str(read.opening_json('dictionary.json')))
    elif start == '0':
        show_menu()
