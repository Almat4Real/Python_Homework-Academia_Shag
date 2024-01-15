eur = 0.92
uan = 36.55
azn = 1.70

user_data1 = input('Укажите кол-во USD: ')
user_data2 = input("В какую валюту хотите перевести (EUR, UAN, AZN): ")

try:
    dollarAmount = float(user_data1)
except ValueError:
    print("Укажите кол-во долларов в численном формате!")
else:
    try:
        convert = user_data2.upper()
        #VN: upper() не вызывает исключения, можно без try
    except ValueError:
        print("Ошибка! Укажите валюту из списка!")
    else:
        if convert == 'EUR':
            value = dollarAmount * eur
        elif convert == "UAN":
            value = dollarAmount * uan
        elif convert == "AZN":
            value = dollarAmount * azn
        else:
            print("Вы ввели неверную валюту!")
    print('Перевод составляет ', convert, '-', value)