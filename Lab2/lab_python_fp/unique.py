class Unique(object):
    def __init__(self, items, **kwargs):
        if 'ignore_case' in kwargs:
            self.items = list(set(map(str.lower, items[1:])))
        else:
            self.items = list(set(map(str, items)))
        self.cur_iter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_iter <= len(self.items) - 1:
            self.cur_iter += 1
            return self.items[self.cur_iter - 1]
        else:
            raise StopIteration

# data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
# print(' '.join(Unique(data, ignore_case=True)))
