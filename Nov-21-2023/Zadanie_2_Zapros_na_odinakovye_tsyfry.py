# 2. Запросить у пользователя трехзначное и число и проверить, есть ли в нем одинаковые цифры.

user_data = input('Введите трехзначное число: ')
try:
    user_int = int(user_data)
except ValueError:
    print('Ошибка! Введите трехзначное число!')
else:
    if 100 <= user_int <= 999:
        number1 = user_int // 100
        number2 = (user_int // 10) % 10
        number3 = user_int % 10
        
        if number1 == number2 or number2 == number3 or number1 == number3:
            print('В вашем числе есть одинаковые цифры')
        else:
            print('В вашем числе нет одинаковых цифр')