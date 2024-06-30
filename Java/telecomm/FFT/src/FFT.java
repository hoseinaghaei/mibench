import java.util.Random;

public class FFT {

    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: fft <waves> <length> -i");
            System.out.println("-i performs an inverse fft");
            System.out.println("make <waves> random sinusoids");
            System.out.println("<length> is the number of samples");
            System.exit(-1);
        }

        boolean inverseTransform = args.length == 3 && args[2].equals("-i");
        int maxWaves = Integer.parseInt(args[0]);
        int maxSize = Integer.parseInt(args[1]);

        Random random = new Random(1);

        double[] realIn = new double[maxSize];
        double[] imagIn = new double[maxSize];
        int[] coeff = new int[maxWaves];
        int[] amp = new int[maxWaves];

        for (int i = 0; i < maxWaves; i++) {
            coeff[i] = random.nextInt(1001);
            amp[i] = random.nextInt(1001);
        }

        for (int i = 0; i < maxSize; i++) {
            for (int j = 0; j < maxWaves; j++) {
                if (random.nextInt(2) == 0) {
                    realIn[i] += coeff[j] * Math.cos(amp[j] * i);
                } else {
                    realIn[i] += coeff[j] * Math.sin(amp[j] * i);
                }
            }
        }

        double[][] result = fftFloat(maxSize, inverseTransform, realIn, imagIn);
        double[] realOut = result[0];
        double[] imagOut = result[1];

        System.out.println("RealOut:");
        for (double val : realOut) {
            System.out.printf("%f ", val);
        }

        System.out.println("\nImagOut:");
        for (double val : imagOut) {
            System.out.printf("%f ", val);
        }
    }

    public static double[][] fftFloat(int numSamples, boolean inverseTransform, double[] realIn, double[] imagIn) {
        if (!isPowerOfTwo(numSamples)) {
            System.out.println("Error in fft():  NumSamples=" + numSamples + " is not power of two");
            System.exit(1);
        }

        final double DDC_PI = Math.PI;
        int numBits = numberOfBitsNeeded(numSamples);
        double angleNumerator = 2.0 * DDC_PI;
        if (inverseTransform) {
            angleNumerator = -angleNumerator;
        }

        double[] realOut = new double[numSamples];
        double[] imagOut = new double[numSamples];

        for (int i = 0; i < numSamples; i++) {
            int j = reverseBits(i, numBits);
            realOut[j] = realIn[i];
            imagOut[j] = imagIn != null ? imagIn[i] : 0.0;
        }

        int blockEnd = 1;
        int blockSize = 2;
        while (blockSize <= numSamples) {
            double deltaAngle = angleNumerator / blockSize;
            double sm2 = Math.sin(-2 * deltaAngle);
            double sm1 = Math.sin(-deltaAngle);
            double cm2 = Math.cos(-2 * deltaAngle);
            double cm1 = Math.cos(-deltaAngle);
            double w = 2 * cm1;
            double[] ar = new double[3];
            double[] ai = new double[3];

            for (int i = 0; i < numSamples; i += blockSize) {
                ar[2] = cm2;
                ar[1] = cm1;
                ai[2] = sm2;
                ai[1] = sm1;

                for (int j = i; j < i + blockEnd; j++) {
                    ar[0] = w * ar[1] - ar[2];
                    ar[2] = ar[1];
                    ar[1] = ar[0];
                    ai[0] = w * ai[1] - ai[2];
                    ai[2] = ai[1];
                    ai[1] = ai[0];
                    int k = j + blockEnd;
                    double tr = ar[0] * realOut[k] - ai[0] * imagOut[k];
                    double ti = ar[0] * imagOut[k] + ai[0] * realOut[k];
                    realOut[k] = realOut[j] - tr;
                    imagOut[k] = imagOut[j] - ti;
                    realOut[j] += tr;
                    imagOut[j] += ti;
                }
            }
            blockEnd = blockSize;
            blockSize <<= 1;
        }

        if (inverseTransform) {
            for (int i = 0; i < numSamples; i++) {
                realOut[i] /= numSamples;
                imagOut[i] /= numSamples;
            }
        }

        return new double[][] { realOut, imagOut };
    }

    private static boolean isPowerOfTwo(int x) {
        if (x < 2) {
            return false;
        }
        return (x & (x - 1)) == 0;
    }

    private static int numberOfBitsNeeded(int powerOfTwo) {
        if (powerOfTwo < 2) {
            throw new IllegalArgumentException("Error: argument " + powerOfTwo + " to numberOfBitsNeeded is too small");
        }
        int i = 0;
        while (powerOfTwo > 1) {
            powerOfTwo >>= 1;
            i++;
        }
        return i;
    }

    private static int reverseBits(int index, int numBits) {
        int rev = 0;
        for (int i = 0; i < numBits; i++) {
            rev = (rev << 1) | (index & 1);
            index >>= 1;
        }
        return rev;
    }
}
