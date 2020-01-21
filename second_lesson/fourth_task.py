user_string = input('Введите строку - ')

string_list = user_string.split()

i = 1

for el in string_list:
    if len(el) > 10:
        el = el[:10]
    print(f'{i}. {el}')
    i += 1
