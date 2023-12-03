# Запросите у пользователя десятичное число и выведите его в двоичном, восьмиричном и шестнадцатиричном виде.

user_data = input('Введие десятичное число: ')
try:
    user_int = int(user_data)
except ValueError:
    print('Вы ввели не число!')
else:
    bin_num = bin(user_int)
    oct_num = oct(user_int)
    hex_num = hex(user_int)
    print('Число в двоичном формате: ', bin_num, ', в восьмиричном формате: ', oct_num, ', в шеснадцатиричном формате: ', hex_num)