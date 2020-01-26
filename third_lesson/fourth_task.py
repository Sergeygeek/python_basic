def my_func(x, y):
    y = abs(y)
    res = 1
    while y > 0:
        res *= x
        y -= 1
    return 1/res


print(my_func(2, -3))
