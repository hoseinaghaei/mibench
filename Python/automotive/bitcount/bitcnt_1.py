def bit_count(x):
    count = 0
    while x:
        count += 1
        x = x & (x - 1)
    return count

if __name__ == "__main__":
    import sys
    for arg in sys.argv[1:]:
        n = int(arg)
        i = bit_count(n)
        print("{} contains {} bit{} set".format(n, i, "s" if i != 1 else ""))
