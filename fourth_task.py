number = int(input('Введите целое положительное число - '))

biggestNumber = 0

while number > 0:
    tempNumber = number % 10
    
    if tempNumber == 9:
        biggestNumber = tempNumber
        break

    if tempNumber > biggestNumber:
        biggestNumber = tempNumber

    number = (number - tempNumber) / 10

print(int(biggestNumber))
