def my_func(arg_1, arg_2, arg_3):
    """Первый вариант

    Позиционные параметры:
    arg_1 -- int Первый параметр
    arg_2 -- int Второй параметр
    arg_3 -- int Третий параметр

    """
    # if arg_1 < arg_2 and arg_1 < arg_3:
    #     return arg_2 + arg_3
    # if arg_2 < arg_1 and arg_2 < arg_3:
    #     return arg_1 + arg_3
    # return arg_1 + arg_2

    """Второй вариант"""



first = int(input('Введите первое число - '))
second = int(input('Введите второе число - '))
third = int(input('Введите третье число - '))

print(my_func(first, second, third))
