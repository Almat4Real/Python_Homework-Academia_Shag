# Запросите у пользователя текущее время (часы и минуты) и выведите, сколько часов и минут осталось до следующего дня.

hour_const = 23
minute_const = 60

user_hour = input('Укажите текущее время - часы: ')
user_minute = input('Укажите текущее время - минуты: ')

try:
    hour = int(user_hour)
    minute = int(user_minute)
except ValueError:
    print('Вы ввели неверные данные')
else:
    real_hour = abs(hour_const - hour)
    real_minute = abs(minute_const - minute)
    print('До конца следующего дня осталось:', real_hour, 'часов и', real_minute, 'минут')