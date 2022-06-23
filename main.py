from collections.abc import Iterable

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]
nested_list2 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]
nested_list3 = [1, 2, [3, 4, [5, 6], 7], 8, ('A', {'B', 'C'})]


class FlatIteration:

    def __init__(self, collection):
        self._collection = sum(collection, [])
        self._cursor = -1

    def __iter__(self):
        return self

    def __next__(self):
        self._cursor += 1
        if self._cursor + 1 > len(self._collection):
            raise StopIteration
        return self._collection[self._cursor]


if __name__ == '__main__':
    # задание №1*
    for item in FlatIteration(nested_list):
        print(item)
    print('-' * 50)

    flat_list = [item for item in FlatIteration(nested_list)]
    print(flat_list)
    print('-' * 50)


    # задание №2*
    def flat_generator(nested_list2):
        for row in nested_list:
            for i in row:
                yield i


    for item in flat_generator(nested_list2):
        print(item)
    print('-' * 50)


    # задание №4*
    def get_list_generator(some_list, ignore_types=(str, bytes)):
        for row in some_list:
            if isinstance(row, Iterable) and not isinstance(row, ignore_types):
                yield from get_list_generator(row)
            else:
                yield row


    for item in get_list_generator(nested_list3):
        print(item)
