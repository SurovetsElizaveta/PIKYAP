import json
from Lab2.lab_python_fp.cm_timer import cm_timer_1
from Lab2.lab_python_fp.unique import Unique

path = "C:\\Users\\User\\PycharmProjects\\PIKYAP\\Lab2\\data_light.json"

with open(path, encoding='utf-8') as f:
    data = json.load(f)


def print_result(func):
    def wrapper(arg):
        print('\n', func.__name__)
        for el in func(arg):
            print(el, end=', ')
        return func(arg)

    return wrapper


@print_result
def f1(datta):
    if len(data) != 0:
        return sorted(Unique([el['job-name'] for el in datta if 'job-name' in el]))
    raise NotImplemented


@print_result
def f2(items):
    if len(items) != 0:
        return list(filter(lambda x: x[:11] == 'программист', items))
    raise NotImplemented


@print_result
def f3(arg):
    if len(arg) != 0:
        return [el + ' с опытом Python' for el in arg]
    raise NotImplemented


@print_result
def f4(arg):
    if len(arg) != 0:
        from random import randint
        res = [el + f' заработок {randint(100000, 300000)}' for el in arg]
        return res
    raise NotImplemented


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
