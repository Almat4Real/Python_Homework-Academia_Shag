# 7. Запросить у пользователя длину окружности и периметр квадрата. Определить, может ли такая окружность поместиться в указанный квадрат. 

import math

user_circle_len = input('Введите длину окружности: ')
user_square_perimeter = input('Введите периметр квадрата: ')
try:
    circle_len = float(user_circle_len)
    square_perimeter = float(user_square_perimeter)
except ValueError:
    print('Вы ввели неверные данные!')
else:
    radius = circle_len / (2 * math.pi)
    square_side = square_perimeter / 4
    diameter = 2 * radius   
    
    if diameter < square_side:
        print('Всё поместится')
    else:
        print('Увы, но не поместится')