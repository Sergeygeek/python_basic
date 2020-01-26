name = input('Введите имя - ')
surname = input('Введите фамилию - ')

try:
    year_of_birth = int(input('Введите год рождения - '))
except ValueError:
    'Год рождения это число'

city = input('Введите город проживания - ')
email = input('Введите email - ')
phone = input('Введите телефон - ')


def get_users_data(*args):
    data = ''
    for el in args:
        data += f'{el} '
    return data


print(get_users_data(name, surname, year_of_birth, city, email, phone))
