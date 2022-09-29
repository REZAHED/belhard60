text = """
Мобильный телефон 3000

ru от 1 шт 18000

ru от 5 шт 17000
"""
countries = ['ru', 'en', 'fr']
from_price = ['от 1', 'от 5', 'от 20', 'от 50']

text2= text.strip().split('\n')
for i in range(0,len(text2)):
    if text2[i]=='':
        text2.pop(i)
print(text2)

data = {
    'Мобильный телефон 3000' : {
        'ru' : {
            'от 1' : 18000,
            'от 5' : 17000

        },
        'en' : {
            'от 1' : 18000,
            'от 5' : 17000
    }
}
}