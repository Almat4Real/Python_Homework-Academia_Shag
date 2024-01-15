# 6. Запросить у пользователя сумму покупки и вывести сумму к оплате со скидкой: от 200 до 300 – скидка будет 3%, от 300 до 500 – 5%, от 500 и выше – 7%.

user_data = input("Укажите сумму покупки: ")
discount = 0

try:
    sum = float(user_data)
except ValueError:
    print('Вы ввели текст!')
else:
    if 200 < sum < 300:
        discount = 0.03
        cost = sum * discount
        total = sum - cost
    elif 300 < sum < 500:
        discount = 0.05
        cost = sum * discount
        total = sum - cost
    elif sum > 500:
        discount = 0.07
        cost = sum * discount
        total = sum - cost
    else:
        print("Ошибка! На такую сумму скидок нет!")
print('Ваша сумма со скидкой составляет: ', total)


"""VN: программа падает в последней строке:

Укажите сумму покупки: mnogo
Вы ввели текст!
Traceback (most recent call last):
  File "/home/vn/Job/ItStep/HomeWorks/SEP-232.1/Алмат/Nov-21-2023/Zadanie_6_Summa_so_skidkoi.py", line 25, in <module>
    print('Ваша сумма со скидкой составляет: ', total)
                                                ^^^^^
NameError: name 'total' is not defined
"""