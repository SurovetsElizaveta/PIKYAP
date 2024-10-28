# Пример:
goods = [
   {'title': 'Ковер', 'price': 2000, 'color': 'green'},
   {'title': 'Диван для отдыха', 'price': 5300, 'color': 'red'}
]

def field(items, *args):
    assert len(args) > 0
    for i in range(len(items)):
        if len(args) == 1:
            if args[0] in items[i]:
                yield str(items[i][args[0]])
        else:
            print('{', end='')
            for el in args:
                if el in items[i]:
                    yield '{} : {}'.format(el, items[i][el])
            print('}', end='')
        print(', ', end='')

for i in field(goods, 'color', 'title'):
    print(i, end='')
