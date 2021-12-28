#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Объявите функцию с именем to_lat , которая принимает строку на кириллице и
# преобразовывает ее в латиницу, используя следующий словарь для замены русских букв на
# соответствующее латинское написание:Функция должна возвращать преобразованную строку. Замены делать без учета регистра
# (исходную строку перевести в нижний регистр – малые буквы). Все небуквенные символы
# "! ?:;.,_" превращать в символ '-' (дефиса). Определите декоратор для этой функции,
# который несколько подряд идущих дефисов, превращает в один дефис. Полученная строка
# должна возвращаться при вызове декоратора. Примените декоратор к функции to_lat и
# вызовите ее Результат работы декорированной функции отобразите на экране

def to_lat(func):
    def g(text, chars=' !?'):
        tmp = ''.join(map(lambda x: x if x not in chars else '-', func(text)))
        while '--' in tmp:
            tmp = tmp.replace('--', '-')
        return tmp

    return g


@to_lat
def h(text):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    return ''.join(map(lambda x: t.get(x, x), txt.lower()))


if __name__ == '__main__':
    txt = 'Функция должна возвращать преобразованную строку'
    print(h(txt, chars='?!:;,. '))
