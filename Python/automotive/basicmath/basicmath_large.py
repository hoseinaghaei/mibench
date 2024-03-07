from cubic import solve_cubic
from isqrt import usqrt
from rad2deg import rad2deg, deg2rad
import math


def main():
    print("********* CUBIC FUNCTIONS ***********")
    a, b, c, d = 1.0, -10.5, 32.0, -30.0
    count, solution = solve_cubic(a, b, c, d)
    print("Solutions:", end='')
    for i in range(count):
        print(" {:.6f}".format(solution[i]), end='')
    print()

    a, b, c, d = 1.0, -4.5, 17.0, -30.0
    count, solution = solve_cubic(a, b, c, d)
    print("Solutions:", end='')
    for i in range(count):
        print(" {:.6f}".format(solution[i]), end='')
    print()

    a, b, c, d = 1.0, -3.5, 22.0, -31.0
    count, solution = solve_cubic(a, b, c, d)
    print("Solutions:", end='')
    for i in range(count):
        print(" {:.6f}".format(solution[i]), end='')
    print()

    a, b, c, d = 1.0, -13.7, 1.0, -35.0
    count, solution = solve_cubic(a, b, c, d)
    print("Solutions:", end='')
    for i in range(count):
        print(" {:.6f}".format(solution[i]), end='')
    print()

    a, b, c, d = 3.0, 12.34, 5.0, 12.0
    count, solution = solve_cubic(a, b, c, d)
    print("Solutions:", end='')
    for i in range(count):
        print(" {:.6f}".format(solution[i]), end='')
    print()

    a, b, c, d = -8.0, -67.89, 6.0, -23.6
    count, solution = solve_cubic(a, b, c, d)
    print("Solutions:", end='')
    for i in range(count):
        print(" {:.6f}".format(solution[i]), end='')
    print()

    a, b, c, d = 45.0, 8.67, 7.5, 34.0
    count, solution = solve_cubic(a, b, c, d)
    print("Solutions:", end='')
    for i in range(count):
        print(" {:.6f}".format(solution[i]), end='')
    print()

    a, b, c, d = -12.0, -1.7, 5.3, 16.0
    count, solution = solve_cubic(a, b, c, d)
    print("Solutions:", end='')
    for i in range(count):
        print(" {:.6f}".format(solution[i]), end='')
    print()

    print("********* RANDOM CUBIC FUNCTIONS ***********")
    for a in range(1, 10, 1):
        for b in range(40, 0, -1):
            for c in range(5, 15):
                for d in range(-90, -500, -10):
                    count, solution = solve_cubic(a, b / 4, c + 0.61, d / 100)
                    print("Solutions:", end='')
                    for i in range(count):
                        print(" {:.6f}".format(solution[i]), end='')
                    print()

    print("********* INTEGER SQR ROOTS ***********")
    for i in range(0, 100000, 2):
        q = usqrt(i)
        print("sqrt({}) = {}".format(i, q.sqrt))

    print()
    for l in range(0x3fed0169, 0x3fed4169):
        q = usqrt(l)
        print("sqrt({:X}) = {:X}".format(l, q.sqrt))

    print("********* ANGLE CONVERSION ***********")
    x = 0
    while x < 361:
        print("{:3.0f} degrees = {:.12f} radians".format(x, deg2rad(x)))
        x += 0.001
    print()

    x = 0
    while x < 2 * math.pi + 1e-6:
        print("{:.12f} radians = {:3.0f} degrees".format(x, rad2deg(x)))
        x += math.pi / 5760


if __name__ == "__main__":
    main()
