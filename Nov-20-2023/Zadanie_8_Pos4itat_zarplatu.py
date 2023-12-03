# Зарплата работника составляет $250 + 10% от продаж. Запросите общую сумму продаж за месяц и посчитайте зарплату.

salary = 250
user_sales = input('Укажите общую сумму продаж за месяц: ')
try:
    sales = int(user_sales)
except ValueError:
    print('Укажите сумму в цифрах!')
else:
    summary_salary = (sales * 0.1) + salary
    print('Ваша зарплата составляет: ', summary_salary)