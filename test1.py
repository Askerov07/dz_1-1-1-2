class flatiterator:
    def __init__(self, list_of_lists):
        self.flatten_list = [item for sublist in list_of_lists for item in sublist]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.flatten_list):
            result = self.flatten_list[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, 'нет']
    ]

    for flat_iterator_item, check_item in zip(flatiterator(list_of_lists_1),
                                              ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, 'нет']):
        assert flat_iterator_item == check_item

    assert list(flatiterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, 'нет']


if __name__ == '__main__':
    test_1()
