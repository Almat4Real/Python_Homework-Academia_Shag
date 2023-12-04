# Задание 1
# Решите задачу о спецсимволах из предыдущей домашней работы, но используя операторы match и case.

user_data = input("Введите число от 0 до 9: ")
try:
    number = int(user_data)
except ValueError:
    print('Вы ввели некорректные данные!')
else:
    match number:
        case 0:
            print(')')
        case 1:
            print('!')
        case 2:
            print('@')
        case 3:
            print('#')
        case 4:
            print('$')
        case 5:
            print('%')
        case 6:
            print('^')
        case 7:
            print('&')
        case 8:
            print('*')
        case 9:
            print('(')
        case _:
            print('Нет символа для такого числа')
    