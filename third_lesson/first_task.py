dividend = input('Введите делимое - ')
divider = input('Введите делитель - ')


def division(dividend, divider):
    try:
        dividend = int(dividend)
        divider = int(divider)
        result = dividend / divider
    except ValueError:
        return "Введено неверное значение"
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    return result


print(division(dividend, divider))
