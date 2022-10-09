text = """
Мобильный телефон 3000

ru от 1 шт 18000

ru от 5 шт 17000

en от 1 шт 15000

мобильный телефон 2000

en от 20 шт 18000

en от 50 шт 17000

ru от 1 шт 15000

"""
text=text.replace("от", "от_")
text=text.replace("шт", "")
countries = ['ru', 'en']
from_price = ['от 1', 'от 5', 'от 20', 'от 50']

lines = [line.strip() for line in text.split("\n") if line.strip()]

data={}
flage=""
for line in lines:
    if line[:2] in countries:
        line = line.split()
        if line[0] not in data[flage]:
            data[flage].update({line[0]:{line[1]:int(line[2])}})
        else:
            data[flage][line[0]].update({line[1]: int(line[2])})
    else:
        data[line]={}
        flage=line
print(data)