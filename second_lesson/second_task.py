user_list = []

while True:
    item = input('Введите значение для добавления в список(Чтобы выйти ввелите "Exit") - ')
    if item == 'Exit':
        break
    user_list.append(item)

for el in user_list:
    print(el)

i = 0

while i < len(user_list):
    if i + 1 == len(user_list):
        break
    user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
    i += 2

print('Второй список')
for el in user_list:
    print(el)
