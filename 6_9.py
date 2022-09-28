# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

dic = {"id_1": {"name": "alex", "surname": "petrov", "tel": "+375297525887", "email": "petrov@mail.ru"},
       "id_2": {"name": "ivan", "surname": "ivanov", "tel": "+375298273437", "email": ""},
       "id_3": {"name": "dmitri", "surname": "slizh", "tel": "+375297525887"}
       }

for i in dic.values():
    if "email" not in i or i["email"] == "":
        print(f" у пользователя {i.get('name')} email не указан ")


