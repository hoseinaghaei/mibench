from math import sqrt, acos, cos, pi, fabs, pow


def solve_cubic(a, b, c, d):
    x = [0, 0, 0]

    a1 = b / a
    a2 = c / a
    a3 = d / a

    q = (a1 * a1 - 3.0 * a2) / 9.0
    r = (2.0 * a1 * a1 * a1 - 9.0 * a1 * a2 + 27.0 * a3) / 54.0
    r2_q3 = r * r - q * q * q

    if r2_q3 <= 0:
        solutions = 3
        theta = acos(r / sqrt(q * q * q))
        x[0] = -2.0 * sqrt(q) * cos(theta / 3.0) - a1 / 3.0
        x[1] = -2.0 * sqrt(q) * cos((theta + 2.0 * pi) / 3.0) - a1 / 3.0
        x[2] = -2.0 * sqrt(q) * cos((theta + 4.0 * pi) / 3.0) - a1 / 3.0
    else:
        solutions = 1
        x[0] = pow(sqrt(r2_q3) + fabs(r), 1 / 3.0)
        x[0] += q / x[0]
        x[0] *= 1 if r < 0.0 else -1
        x[0] -= a1 / 3.0

    return solutions, x


def main():
    a1, b1, c1, d1 = 1.0, -10.5, 32.0, -30.0
    a2, b2, c2, d2 = 1.0, -4.5, 17.0, -30.0

    # should get 3 solutions: 2, 6 & 2.5
    solutions, x = solve_cubic(a1, b1, c1, d1)
    print("Solutions for cubic equation 1:", solutions)
    print("Roots:", x[0:solutions])

    #  should get 1 solution: 2.5
    solutions, x = solve_cubic(a2, b2, c2, d2)
    print("\nSolutions for cubic equation 2:", solutions)
    print("Roots:", x[0:solutions])


if __name__ == "__main__":
    main()
