import sys
import time
import random

from bitcnt_1 import bit_count
from bitcnt_2 import bitcount
from bitcnt_3 import ntbl_bitcount, AR_btbl_bitcount, BW_btbl_bitcount
from bitcnt_4 import ntbl_bitcnt


def bit_shifter(x):
    n = 0
    for _ in range(32):
        n += x & 1
        x >>= 1
    return n


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <iterations>")
        sys.exit(1)
    iterations = int(sys.argv[1])

    funcs = [
        bit_count,
        bitcount,
        ntbl_bitcnt,
        ntbl_bitcount,
        BW_btbl_bitcount,
        AR_btbl_bitcount,
        bit_shifter
    ]
    funcs_name = [
        "Optimized 1 bit/loop counter",
        "Ratko's mystery algorithm",
        "Recursive bit count by nybbles",
        "Non-recursive bit count by nybbles",
        "Non-recursive bit count by bytes (BW)",
        "Non-recursive bit count by bytes (AR)",
        "Shift and count bits"
    ]
    results = []

    print("Bit counter algorithm benchmark\n")

    min_func = float('inf')
    min_time = float('inf')

    max_func = 0
    max_time = 0

    for i in range(7):
        start = time.time()

        total_bits = 0
        seed = random.randint(0, 2147483647)
        for j in range(iterations):
            total_bits += funcs[i](seed)
            seed += 13

        elapsed_time = time.time() - start

        if elapsed_time < min_time:
            min_time = elapsed_time
            min_func = funcs_name[i]

        if elapsed_time > max_time:
            max_time = elapsed_time
            max_func = funcs_name[i]

        print(f"{funcs_name[i]:<38}> Time: {elapsed_time:.3f} sec.; Bits: {total_bits}")

    print("\nBest  > ", min_func)
    print("Worst > ", max_func)
