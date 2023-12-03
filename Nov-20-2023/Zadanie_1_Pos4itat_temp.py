# Пользователь вводит два значения температуры воздуха: днём и ночью. Посчитайте велечину перепада температуры.

try:
    user_day_temperature = int(input('Введите температуру днем: '))
    user_night_temperature = int(input('Введите температуру ночью: '))
except ValueError:
    print('Вы ввели не число!')
else:
    temperature_differece = abs(user_day_temperature - user_night_temperature)
    print('Перепад температуры составляет: ', temperature_differece)
finally:
    print('Программа окончена')