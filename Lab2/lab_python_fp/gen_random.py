from random import randint
def get_random(num_count, begin, end):
    for i in range(num_count):
        yield randint(begin, end)

if __name__ == '__main__':
    for i in get_random(5, 1, 3):
        print(i, end=' ')
