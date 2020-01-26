my_list = [7, 5, 3, 3, 2]

rate = float(input('Введите рейтинг - '))

if my_list.count(rate):
    first_idx = my_list.index(rate)
    idx_count = my_list.count(rate)
    my_list.insert(first_idx + idx_count, rate)
else:
    for el in my_list:
        if el < rate:
            idx = my_list.index(el)
            my_list.insert(idx, rate)
            break
        my_list.append(rate)
        break

print(my_list)
