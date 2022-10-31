
class FlatPattern(object):
    def __init__(self, object):
        self.nes_list = object
        self.flatten_list = []
        self._flat_list(self.nes_list)

    def __iter__(self):
        self.cursor = 0
        self.end = len(self.flatten_list)
        self.items_list = []
        return self

    def __next__(self):
        if self.cursor < self.end:
            self.cursor += 1
            return self.flatten_list[self.cursor-1]
        else:
            raise StopIteration

    def _flat_list(self, elem):
        if type(elem) == list:
            for e in elem:
                self._flat_list(e)
        else:
            self.flatten_list.append(elem)
            return elem
def main():
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    flatty = FlatPattern(nested_list)
    for item in flatty:
        print(f'{item}')

    flat_list = [item for item in flatty]
    print(flat_list)

if __name__ == '__main__':
    main()