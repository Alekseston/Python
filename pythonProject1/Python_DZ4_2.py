# Задача №2
# Обменник. Создать скрипт, который будет запускаться из консоли 1 раз и, выдавать результат и закрываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится ответ в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "Конвертированная сумма в USD = int"
#                 "Конвертированная сумма в EUR = int"
#                 "Конвертированная сумма в CHF = int"
#                 "Конвертированная сумма в GBP = int"
#                 "Конвертированная сумма в CNY = int"
# 3.Валюту пользователя определите сами.
dict_data = {'USD': 78, 'EUR': 89, 'CHF': 86, 'GBP': 107, 'CNY': 12}
a = int(input())
print('Ты ввёл int (RUB)', a)
for i, y in dict_data.items():
    r = int(a / y)
    print('конвертированная сумма в '+i+' = int', r)