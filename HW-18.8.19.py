number_of_people = int(input('Введите требуемое количество билетов:'))

# Добавил блокировку ввода на недопустимые значения количества людей: -ꚙ, 0.
# Начало:
while number_of_people <= 0:
    number_of_people = int(input('Недопустимое число! \nВведите требуемое количество билетов:'))
# Конец.

sum_price = 0

for cycle in range(number_of_people):
    print('Введите возраст', cycle + 1, '\b-го посетителя:')
    age = int(input())
    if age >= 100 or age <= 0:
        # Добавляю блокировку на ввод недопустимых значений возраста: -ꚙ, 0, 100, +ꚙ.
        while age >= 100 or age <= 0:
            print('Недопустимое число!\nВведите возраст', cycle + 1, '\b-го посетителя:')
            age = int(input())
        # Вложил кусок кода из тела цикла for, т.к. без него, sum_price, из выхода цикла while, равнялся нулю,
        # а операторы elif в теле цикла for не выполнялись из-за истинности в блоке if.
        if 0 < age < 18:
            sum_price += 0
        elif 18 <= age <= 25:
            sum_price += 990
        elif 25 < age < 100:
            sum_price += 1390
    # Конец блокировки.
    elif 0 < age < 18:
        sum_price += 0
    elif 18 <= age <= 25:
        sum_price += 990
    elif 25 < age < 100:
        sum_price += 1390
# Конец цикла for.

if number_of_people > 3:
    sum_price = sum_price - (sum_price * 0.1)

# Добавил, условие, что, если все участники конференции несовершеннолетние, то билеты бесплатны.
if sum_price == 0:
    print('Билеты бесплатны!')
else:
    print('Итоговая сумма:', int(sum_price), 'рублей')
