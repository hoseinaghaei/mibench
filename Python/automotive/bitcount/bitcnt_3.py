# Bits table

bits = [
    0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8
]


def ntbl_bitcount(x):
    return (
            bits[x & 0x0000000F] +
            bits[(x & 0x000000F0) >> 4] +
            bits[(x & 0x00000F00) >> 8] +
            bits[(x & 0x0000F000) >> 12] +
            bits[(x & 0x000F0000) >> 16] +
            bits[(x & 0x00F00000) >> 20] +
            bits[(x & 0x0F000000) >> 24] +
            bits[(x & 0xF0000000) >> 28]
    )


def BW_btbl_bitcount(x):
    class Union:
        def __init__(self, value):
            self.ch = [(value >> (i * 8)) & 0xFF for i in range(4)]

    U = Union(x)
    return sum(bits[ch] for ch in U.ch)


def AR_btbl_bitcount(x):
    ptr = x.to_bytes((x.bit_length() + 7) // 8, 'little')
    accu = 0
    for byte in ptr:
        accu += bits[byte]
    return accu


if __name__ == "__main__":
    import sys

    for arg in sys.argv[1:]:
        n = int(arg)
        i = ntbl_bitcount(n)
        print("{} contains {} bit{} set".format(n, i, "s" if i != 1 else ""))
