# products = []
#
# i = 1
#
# while True:
#     name = input('Введите название товара - ')
#     price = int(input('Введите цену товара - '))
#     quantity = int(input('Введите количество товара - '))
#     unit = input('Введите единицу измерения - ')
#     is_done = input('Продолжить?(y/n)')
#     products.append((i, {"название": name, "цена": price, "количество": quantity, "ед.": unit}))
#     i += 1
#     if is_done == 'n':
#         break
#
# print(products)

products1 = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 3, 'ед.': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 4000, 'количество': 5, 'ед.': 'шт.'})
]

total_data = {}

for el in products1:
    for key, value in el[1].items():
        total_data.setdefault(key)
        total_data.update(key)

print(total_data)
