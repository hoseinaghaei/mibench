import sys

MAX_ARRAY = 60000


class MyStringClass:
    def __init__(self, qstring):
        self.qstring = qstring

def main():
    if len(sys.argv) < 2:
        print("Usage: python qsort_small.py <file>")
        sys.exit(-1)

    filename = sys.argv[1]
    array = []

    with open(filename, "r") as fp:
        count = 0
        for line in fp:
            if count >= MAX_ARRAY:
                break
            array.append(MyStringClass(line.strip()))
            count += 1

    print("\nSorting {} elements.\n".format(count))
    array.sort(key=lambda x: x.qstring, reverse=True)

    for item in array:
        print(item.qstring)


if __name__ == "__main__":
    main()
