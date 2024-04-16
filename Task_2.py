"""Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида “10.25%”.
В результате получаем словарь с именем в качестве ключа и суммой премии
в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии"""

names = ['Иван', 'Николай', 'Василий']
wages = [80_000, 100_000, 120_000]
percents = ['12.00%', '10.25%', '16.50%']
dictionary = {k: v * float(p[:-1])/100 for k, v, p in zip(names, wages, percents)}
print(dictionary)