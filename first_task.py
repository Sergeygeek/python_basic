name = input('Введите имя - ')

print(f'Здравствуйте {name}.')

num1 = 12
num2 = 25

answer = int(input(f'Введите сумму {num1} и {num2} - '))

if answer:
    if answer == num1 + num2:
        print('Вы ответили верно')
    else:
        print('Ответ неверный')
else:
    print('Введите число')
