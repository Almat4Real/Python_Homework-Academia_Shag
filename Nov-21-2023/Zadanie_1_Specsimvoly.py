# 1. Запросить у пользователя число от 0 до 9 и вывести ему спецсимвол, который расположен на этой клавише (1–!, 2–@, 3–# и т. д). Учтите, что пользователь может ввести что угодно.

user_data = input("Введите число от 0 до 9: ")
try:
    number = int(user_data)
except ValueError:
    print('Вы ввели некорректные данные!')
else:
    if number == 0:
        print(')')
    elif number == 1:
        print('!')
    elif number == 2:
        print('@')
    elif number == 3:
        print('#')
    elif number == 4:
        print('$')
    elif number == 5:
        print('%')
    elif number == 6:
        print('^')
    elif number == 7:
        print('&')
    elif number == 8:
        print('*')
    elif number == 9:
        print('(')
    else:
        print('Нет символа для такого числа')
    
    