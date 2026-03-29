

import random


def setup():
    array = [0] * 100
    i = 0
    while i < 100:
        array[i] = random.randrange(0, 20)
        i = i + 1
    return array


if __name__ == '__main__':

    array = setup()
    print(array)
    i = 0
    max = -1
    while i < 100:
        a = array[i]
        if a > max:
            max = a

        i = i + 1

    print(f"максимальноу число это {max}")