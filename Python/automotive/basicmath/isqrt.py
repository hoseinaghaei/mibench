from ctypes import c_uint32

BITSPERLONG = 32

def uint32(val):
    if val < 2 ** 31:
        return val
    return c_uint32(val).value

class IntSqrt:
    def __init__(self, sqrt, frac):
        self.sqrt = sqrt
        self.frac = frac


def usqrt(x):
    a = 0
    r = 0

    for i in range(BITSPERLONG):
        r = uint32(uint32(r << 2) + (x >> (BITSPERLONG - 2)))
        x = uint32(x << 2)
        a = uint32(a << 1)
        e = uint32(uint32(a << 1) + 1)
        if r >= e:
            r -= e
            a = uint32(a + 1)

    return IntSqrt(a, r)


def main():
    l = 0x3fed0169
    for i in range(0, 101):  # Adjust the range accordingly
        q = usqrt(i)
        print("sqrt({:3d}) = {:2d}, remainder = {:2d}".format(i, q.sqrt, q.frac))

    q = usqrt(l)
    print("\nsqrt({:X}) = {:X}, remainder = {:X}".format(l, q.sqrt, q.frac))


if __name__ == "__main__":
    main()
