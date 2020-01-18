firstResult = int(input('Введите начальное значение - '))
wannaResult = int(input('Введите значение, которого вы хотите добиться - '))
day = 1

while firstResult < wannaResult:
    firstResult += firstResult * 0.1
    day += 1

print(day)
