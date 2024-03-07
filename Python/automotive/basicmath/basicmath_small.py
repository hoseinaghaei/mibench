import math
from cubic import solve_cubic
from isqrt import usqrt
from rad2deg import rad2deg, deg2rad

if __name__ == "__main__":
    a1, b1, c1, d1 = 1.0, -10.5, 32.0, -30.0
    a2, b2, c2, d2 = 1.0, -4.5, 17.0, -30.0
    a3, b3, c3, d3 = 1.0, -3.5, 22.0, -31.0
    a4, b4, c4, d4 = 1.0, -13.7, 1.0, -35.0

    print("********* CUBIC FUNCTIONS ***********")
    # should get 3 solutions: 2, 6 & 2.5
    count, solution = solve_cubic(a1, b1, c1, d1)
    print("Solutions:", end='')
    for i in range(count):
        print(f' {solution[i]}', end='')
    print()

    # should get 1 solution: 2.5
    count, solution = solve_cubic(a2, b2, c2, d2)
    print("Solutions:", end='')
    for i in range(count):
        print(f' {solution[i]}', end='')
    print()

    count, solution = solve_cubic(a3, b3, c3, d3)
    print("Solutions:", end='')
    for i in range(count):
        print(f' {solution[i]}', end='')
    print()

    count, solution = solve_cubic(a4, b4, c4, d4)
    print("Solutions:", end='')
    for i in range(count):
        print(f' {solution[i]}', end='')
    print()

    # Now solve some random equations
    for a in range(1, 10):
        for b in range(10, 0, -1):
            for c in range(5, 15):
                for d in range(-1, -11, -1):
                    count, solution = solve_cubic(a, b, c, d)
                    print("Solutions:", end='')
                    for i in range(count):
                        print(f' {solution[i]}', end='')
                    print()

    print("********* INTEGER SQR ROOTS ***********")
    for i in range(1001):
        print("sqrt({}) = {}".format(i, usqrt(i).sqrt))

    l = 0x3fed0169
    q = usqrt(l)
    print("\nsqrt({:X}) = {:X}".format(l, q.sqrt))

    print("********* ANGLE CONVERSION ***********")
    for X in range(0, 361):
        print("{:3.0f} degrees = {:.12f} radians".format(X, deg2rad(X)))
    print()

    x = 0
    while x < 2 * math.pi + 1e-6:
        print("{:.12f} radians = {:3.0f} degrees".format(x, rad2deg(x)))
        x += math.pi / 100
