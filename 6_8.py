# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны
dic = {"Belarus": ["Minsk", "Vitebsk", "Gomel", "Mogilev"], "Spain": ["Madrid", "Barcelona"],
       "Germany": ["Berlin", "Frankfurt"]}
text = input("where are you from?: ").lower().title()


def getcity(name):
    for i,j in dic.items():
        if text in j:
            return i

print(f"you are from {getcity(text)}")