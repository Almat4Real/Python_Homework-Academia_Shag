# Запросите у пользователя координаты x и y для двух точек. Вычислите расстояние между этими точками.

user_data_x1 = input('Введите координаты x1: ')
user_data_x2 = input('Введите координаты x2: ')
user_data_y1 = input('Введите координаты y1: ')
user_data_y2 = input('Введите координаты y2: ')

try:
    x1 = int(user_data_x1)
    x2 = int(user_data_x2)
    y1 = int(user_data_y1)
    y2 = int(user_data_y2)
except ValueError:
    print('Убедитесь, что вы ввели правильные данные!!!')
else:
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    print('Расстояние между точками составляет: ', distance)