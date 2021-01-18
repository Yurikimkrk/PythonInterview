"""
Задание 4. Написать программу «Банковский депозит».
Она должна состоять из функции и ее вызова с аргументами.
Клиент банка делает депозит на определенный срок.
В зависимости от суммы и срока вклада определяется
процентная ставка:
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых).
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых).
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых).
Необходимо написать функцию, в которую будут передаваться параметры:
сумма вклада и срок вклада. Каждый из трех банковских продуктов должен
быть представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24).
Ключам соответствуют значения начала и конца диапазона суммы вклада и
значения процентной ставки для каждого срока. В функции необходимо
проверять принадлежность суммы вклада к одному из диапазонов и
выполнять расчет по нужной процентной ставке. Функция возвращает
сумму вклада на конец срока.

Примечание: используем функциональный подход (не ООП)
Вы можете сделать расчет без капитализации и с капитализацией

Пример без капитализации: 10 тыс на 24 мес
deposit(10000, 24)
к концу срока: 11300

Пример с капитализацией (ежемесячной): 10 тыс на 24 мес
deposit(10000, 24)
к концу срока: 11384.29
"""


def deposit(amount, months):
    if amount not in range(1000, 1000001) or months not in [6, 12, 24]:
        return 'Неправильные сумма вклада и/или срок'

    bank_products = (
        {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
        {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
        {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5},
    )

    global percent
    percent = 0
    for product in bank_products:
        # верхний диапазон вклада не попадает в проверку ниже, но возможен
        if amount == 1000000:
            percent = bank_products[2][months]
            break
        if amount >= product['begin_sum'] and amount < product['end_sum']:
            percent = product[months]

    total = amount
    for i in range(months):
        profit = total * percent / 100 / 12
        total += profit

    return round(total, 2)


print(deposit(10000, 24))
