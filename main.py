class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.current_row = 0
        self.current_col = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_row >= len(self.list_of_list):
            raise StopIteration

        if self.current_col >= len(self.list_of_list[self.current_row]):
            self.current_row += 1
            self.current_col = 0
            return self.__next__()

        item = self.list_of_list[self.current_row][self.current_col]
        self.current_col += 1
        return item

def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':
    test_1()