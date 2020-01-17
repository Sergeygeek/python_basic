time = int(input('Введите время в секундах - '))

hours = time // 3600

if hours < 10:
    hours = str(f'0{hours}')

time = time % 3600

minutes = time // 60

if minutes < 10:
    minutes = str(f'0{minutes}')

seconds = time % 60

if seconds < 10:
    seconds = str(f'0{seconds}')

print(f'{hours}:{minutes}:{seconds}')
