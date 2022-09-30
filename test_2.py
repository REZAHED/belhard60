text = """
Мобильный телефон 3000

ru от 1 шт 18000

en от 5 шт 17000

Мобильный телефон 400

ru от 1 шт 16000

fr от 5 шт 15000

Мобильный телефон 500000

ru от 1 шт 10000

fr от 5 шт 9000

"""
countries = ['ru', 'en', 'fr']
from_price = ['от 1', 'от 5', 'от 20', 'от 50']



text2= text.replace("\n\n",":}, ").replace("ru","{ru:{").replace("en","{en:{").replace("fr","{fr:{").replace("шт",":")

lst_name=[]
lst_value=[]
dic={}
i=0


# for i in range(len(text2)):
#     if "от" not in text2[i]:
#       lst_value.append(f'{text2[i]}:')
#     elif "ru" or "en" or "fr" in text2[i]:
#         lst_value.append(f'{text2[i]}')

print(dic)
print(dict(lst_value))
print(text2)
# data ={text2[0]:{'ru':{'от 1':'18000'}}}



# data = {
#     'Мобильный телефон 3000': {
#         'ru': {
#             'от 1': 18000,
#             'от 5': 17000
#
#         },
#         'en': {
#             'от 1': 18000,
#             'от 5': 17000
#     }
# }
# }