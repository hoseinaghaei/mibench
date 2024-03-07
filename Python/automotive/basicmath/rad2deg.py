import math

def rad2deg(rad):
    return 180.0 * rad / math.pi

def deg2rad(deg):
    return math.pi * deg / 180.0

if __name__ == "__main__":
    for X in range(0, 361, 45):
        print("{:3.0f} degrees = {:.12f} radians".format(X, deg2rad(X)))
    print("")
    x = 0
    while x < 2 * math.pi + 1e-6:
        print("{:.12f} radians = {:3.0f} degrees".format(x, rad2deg(x)))
        x += math.pi / 6