import sys
from math import sqrt

MAX_ARRAY = 60000


class My3DVertexClass:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.distance = sqrt(x ** 2 + y ** 2 + z ** 2)


def main():
    if len(sys.argv) < 2:
        print("Usage: python qsort_large.py <file>")
        sys.exit(-1)

    filename = sys.argv[1]
    array = []

    with open(filename, "r") as fp:
        count = 0
        for line in fp:
            if count >= MAX_ARRAY:
                break
            x, y, z = map(int, line.split())
            array.append(My3DVertexClass(x, y, z))
            count += 1

    print("\nSorting {} vectors based on distance from the origin.\n".format(count))
    array.sort(key=lambda a: a.distance)

    for item in array:
        print("{} {} {}".format(item.x, item.y, item.z))


if __name__ == "__main__":
    main()
