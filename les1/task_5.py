"""
Задание 5*.Усовершенствовать программу «Банковский депозит».
Третьим аргументом в функцию должна передаваться фиксированная
ежемесячная сумма пополнения вклада. Необходимо в главной функции
реализовать вложенную функцию подсчета процентов для пополняемой суммы.
Примем, что клиент вносит средства в последний день каждого месяца,
кроме первого и последнего. Например, при сроке вклада в 6 месяцев
пополнение происходит в течение 4 месяцев. Вложенная функция возвращает
сумму дополнительно внесенных средств (с процентами),
а главная функция — общую сумму по вкладу на конец периода.

Примечание: используем функциональный подход (не ООП)
Пример: 10 тыс на 24 мес, пополнение - по 100
chargable_deposit(10000, 24, 100)
к концу срока: 13739.36
"""


def deposit(amount, months, extra):
    def extra_deposit(extra, months, percent):
        extra_total = 0
        for i in range(months - 2):
            extra_total += extra
            extra_total += extra_total * percent / 100 / 12
        # добавляем последний месяц, так как в нем нет доп депозита
        extra_total += extra_total * percent / 100 / 12
        return round(extra_total, 2)

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
    total += float(extra_deposit(extra, months, percent))
    return round(total, 2)


print(deposit(10000, 24, 100))
