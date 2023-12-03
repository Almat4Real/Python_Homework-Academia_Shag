# Запросите у пользователя координаты x и y для двух точек. Вычислите расстояние между этими точками.

user_data_x1 = input('Введите координаты x1: ')
user_data_x2 = input('Введите координаты x2: ')
user_data_y1 = input('Введите координаты y1: ')
user_data_y2 = input('Введите координаты y2: ')

x1 = int(user_data_x1)
x2 = int(user_data_x2)
y1 = int(user_data_y1)
y2 = int(user_data_y2)

ab = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print('Расстояние между точками составляет: ', ab)