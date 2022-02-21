# Задача №1
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз ,
# выдавать результат и закрываться.
# 1. На вход обменнику вводишь количество денег int.
# 2. На выходе в консоль выводится отввет в таком виде:
# "Ты ввёл int (Валюта)""конвертированная сумма в USD = int"
# 3. Валюту пользователя определите сами.

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--money', type=int)
item = parser.parse_args()
convertUsd = item.money / 75.26
print('вы ввели', item.money, 'рублей, это', int(convertUsd), 'долларов')

# Задача №2
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "Конвертированная сумма в USD = int"
#                 "Конвертированная сумма в EUR = int"
#                 "Конвертированная сумма в CHF = int"
#                 "Конвертированная сумма в GBP = int"
#                 "Конвертированная сумма в CNY = int"
#     3. Валюту пользователя определите сами.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--money', type=int)
item = parser.parse_args()

convertUSD = item.money / 75.26
convertEURO = item.money / 86.15
convertCHF = item.money / 82.3
convertGBP = item.money / 103.28
convertCNY = item.money / 11.98

print('Ты ввёл', int(item.money))
print('Конвертированная сумма в USD', int(convertUSD))
print('Конвертированная сумма в EURO', int(convertEURO))
print('Конвертированная сумма в CHF', int(convertCHF))
print('Конвертированная сумма в GBP', int(convertGBP))
print('Конвертированная сумма в CNY', int(convertCNY))

# Задача №3 Обменник.
# Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
# 1. На вход обменнику вводишь количество денег int.
# 2. На выходе в консоль выводится отввет в таком виде:
# "Ты ввёл int (Валюта)"
# "конвертированная сумма в USD = int"
# "конвертированная сумма в EUR = int"
# "конвертированная сумма в CHF = int"
# "конвертированная сумма в GBP = int"
# "конвертированная сумма в CNY = int"
# 3. Скипт должен выдать сообщение  "Введите положительное число."
# Если число меньше 0. "Вы ввели не число.
# Введите число." Если введены буквы.

# 4. Валюту пользователя определите сами.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--money', type=str)
item = parser.parse_args()

try:
    numMoney = int(item.money)
    if numMoney < 0:
        print('Вы ввели отрицательное число повторите попытку')

    elif numMoney > 0:
        convertUSD = numMoney / 75.26
        convertEURO = numMoney / 86.15
        convertCHF = numMoney / 82.3
        convertGBP = numMoney / 103.28
        convertCNY = numMoney / 11.98

        print('Ты ввёл', int(item.money))
        print('Конвертированная сумма в USD', int(convertUSD))
        print('Конвертированная сумма в EURO', int(convertEURO))
        print('Конвертированная сумма в CHF', int(convertCHF))
        print('Конвертированная сумма в GBP', int(convertGBP))
        print('Конвертированная сумма в CNY', int(convertCNY))
except ValueError:
    print("Это не правильный ввод. Это не число вообще! Это строка, попробуйте еще раз.")
except :
    print("Это не правильный ввод. Это не число вообще! Это строка, попробуйте еще раз.")


#
# Обменник. Скрипт запускается в консоли и работает постоянно. Остановится нажатием ctrl+c.
# 1. Скрипт сначала выводит "Выберите валюту из ['USD','EUR','CHF','GBP','CNY']"
# 2. Пользователь вводит один из 5 вариантов ['USD','EUR','CHF','GBP','CNY']
# 3. Потом Скрипт выводит "Введите сумму"
# 4. Пользователь вводит сумму int
# 5. Скрипт выводит:"Вы ввели сумму int и валюту "Валюта" ""конвертированная сумма в "Валюта" = int"
# 6. Скипт должен выдать сообщение  "Введите положительное число." Если число меньше 0.
# "Вы ввели не число. Введите число." Если введены буквы.
# 7. После сообщеня об ошибке, скрипт должен автоматом вернуться к шагу 1.
# 8. Валюту пользователя определите сами

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--money', type=str)
parser.add_argument('--valueMoney', type=str)
item = parser.parse_args()

if item.valueMoney == 'USD':
    try:
        numMoney = int(item.money)
        if numMoney < 0:
            print('Вы ввели отрицательное число повторите попытку')

        elif numMoney > 0:
            convertRUB = numMoney * 75.76

            print('Ты ввёл', int(item.money), 'в ваолюте', item.valueMoney)
            print('Конвертированная сумма в RUB', int(convertRUB))

    except ValueError:
        print("Это не правильный ввод. Это не число вообще! Это строка, попробуйте еще раз.")


if item.valueMoney == 'EUR':
    try:
        numMoney = int(item.money)
        if numMoney < 0:
            print('Вы ввели отрицательное число повторите попытку')

        elif numMoney > 0:
            convertRUB = int(numMoney) * 86.15

            print('Ты ввёл', int(item.money), 'в ваолюте', item.valueMoney)
            print('Конвертированная сумма в RUB', int(convertRUB))

    except ValueError:
        print("Это не правильный ввод. Это не число вообще! Это строка, попробуйте еще раз.")


if item.valueMoney == 'CHF':
    try:
        numMoney = int(item.money)
        if numMoney < 0:
            print('Вы ввели отрицательное число повторите попытку')

        elif numMoney > 0:
            convertRUB = int(numMoney) * 82.3

            print('Ты ввёл', int(item.money), 'в ваолюте', item.valueMoney)
            print('Конвертированная сумма в RUB', int(convertRUB))

    except ValueError:
        print("Это не правильный ввод. Это не число вообще! Это строка, попробуйте еще раз.")


if item.valueMoney == 'GBP':
    try:
        numMoney = int(item.money)
        if numMoney < 0:
            print('Вы ввели отрицательное число повторите попытку')

        elif numMoney > 0:
            convertRUB = int(numMoney) * 103.28

            print('Ты ввёл', int(item.money), 'в ваолюте', item.valueMoney)
            print('Конвертированная сумма в RUB',int(convertRUB))

    except ValueError:
        print("Это не правильный ввод. Это не число вообще! Это строка, попробуйте еще раз.")













