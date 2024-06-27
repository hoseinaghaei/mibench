import sys
import math
import random


def fft_float(num_samples, inverse_transform, real_in, imag_in=None):
    def is_power_of_two(x):
        if x < 2:
            return False
        return (x & (x - 1)) == 0

    def number_of_bits_needed(power_of_two):
        if power_of_two < 2:
            raise ValueError(f"Error: argument {power_of_two} to number_of_bits_needed is too small")
        i = 0
        while power_of_two > 1:
            power_of_two >>= 1
            i += 1
        return i

    def reverse_bits(index, num_bits):
        rev = 0
        for _ in range(num_bits):
            rev = (rev << 1) | (index & 1)
            index >>= 1
        return rev

    if not is_power_of_two(num_samples):
        print(f"Error in fft():  NumSamples={num_samples} is not power of two")
        exit(1)

    DDC_PI = math.pi
    num_bits = number_of_bits_needed(num_samples)
    angle_numerator = 2.0 * DDC_PI
    if inverse_transform:
        angle_numerator = -angle_numerator

    real_out = [0.0] * num_samples
    imag_out = [0.0] * num_samples if imag_in else [0.0] * num_samples

    for i in range(num_samples):
        j = reverse_bits(i, num_bits)
        real_out[j] = real_in[i]
        imag_out[j] = imag_in[i] if imag_in else 0.0

    block_end = 1
    block_size = 2
    while block_size <= num_samples:
        delta_angle = angle_numerator / block_size
        sm2 = math.sin(-2 * delta_angle)
        sm1 = math.sin(-delta_angle)
        cm2 = math.cos(-2 * delta_angle)
        cm1 = math.cos(-delta_angle)
        w = 2 * cm1
        ar = [0.0] * 3
        ai = [0.0] * 3

        for i in range(0, num_samples, block_size):
            ar[2] = cm2
            ar[1] = cm1
            ai[2] = sm2
            ai[1] = sm1

            for j in range(i, i + block_end):
                ar[0] = w * ar[1] - ar[2]
                ar[2] = ar[1]
                ar[1] = ar[0]
                ai[0] = w * ai[1] - ai[2]
                ai[2] = ai[1]
                ai[1] = ai[0]
                k = j + block_end
                tr = ar[0] * real_out[k] - ai[0] * imag_out[k]
                ti = ar[0] * imag_out[k] + ai[0] * real_out[k]
                real_out[k] = real_out[j] - tr
                imag_out[k] = imag_out[j] - ti
                real_out[j] += tr
                imag_out[j] += ti
        block_end = block_size
        block_size <<= 1

    if inverse_transform:
        denom = float(num_samples)
        for i in range(num_samples):
            real_out[i] /= denom
            imag_out[i] /= denom

    return real_out, imag_out


def main():
    if len(sys.argv) < 3:
        print("Usage: fft <waves> <length> -i")
        print("-i performs an inverse fft")
        print("make <waves> random sinusoids")
        print("<length> is the number of samples")
        sys.exit(-1)

    invfft = len(sys.argv) == 4 and sys.argv[3] == "-i"
    max_waves = int(sys.argv[1])
    max_size = int(sys.argv[2])

    random.seed(1)

    real_in = [0.0] * max_size
    imag_in = [0.0] * max_size
    coeff = [random.randint(0, 1000) for _ in range(max_waves)]
    amp = [random.randint(0, 1000) for _ in range(max_waves)]

    for i in range(max_size):
        for j in range(max_waves):
            if random.randint(0, 1):
                real_in[i] += coeff[j] * math.cos(amp[j] * i)
            else:
                real_in[i] += coeff[j] * math.sin(amp[j] * i)

    real_out, imag_out = fft_float(max_size, invfft, real_in, imag_in)

    print("RealOut:")
    print("\t".join(f"{val:.6f}" for val in real_out))
    print("\nImagOut:")
    print("\t".join(f"{val:.6f}" for val in imag_out))


if __name__ == "__main__":
    main()
