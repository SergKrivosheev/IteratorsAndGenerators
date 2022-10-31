def flat_generator(object):
    cursor = 0
    while cursor < len(object):
        for obj in object:
            object_list = obj
            for item in object_list:
                yield f'{item}'
            cursor += 1


def main():

    nested_list = [
            ['1', '2', '3'],
            ['d', 'e', 'f', 'h', False],
            [1, 2, None]
        ]

    for item in flat_generator(nested_list):
        print(item)

    flat_list = [item for item in flat_generator(nested_list)]
    print(flat_list)

if __name__ == '__main__':
    main()