# Попросите пользователя ввести дробное число и количество знаков после запятой для округления. Округлите число так, как хочет пользователь.

user_data1 = input('Введите дробное чило: ')
user_data2 = input('Укажите кол-во знаков поле запятой: ')

try:
    num_float = float(user_data1)
except ValueError:
    print('Вы ввели не число!')
else:
    try:
        num_int = int(user_data2)
    except ValueError:
        print('Укажите кол-во знаков после запятой в цифрах!')
    else:
        round_func = round(num_float, num_int)
        print('Результат: ', round_func)