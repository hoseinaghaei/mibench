
import java.util.Arrays;

public class BasicMathLarge {

    public static void main(String[] args) {
        System.out.println("********* CUBIC FUNCTIONS ***********");
        testCubicFunctions();

        System.out.println("********* RANDOM CUBIC FUNCTIONS ***********");
        testRandomCubicFunctions();

        System.out.println("********* INTEGER SQR ROOTS ***********");
        testIntegerSqrRoots();

        System.out.println("********* ANGLE CONVERSION ***********");
        testAngleConversion();
    }

    private static void testCubicFunctions() {
        double[][] coefficients = {
                {1.0, -10.5, 32.0, -30.0},
                {1.0, -4.5, 17.0, -30.0},
                {1.0, -3.5, 22.0, -31.0},
                {1.0, -13.7, 1.0, -35.0},
                {3.0, 12.34, 5.0, 12.0},
                {-8.0, -67.89, 6.0, -23.6},
                {45.0, 8.67, 7.5, 34.0},
                {-12.0, -1.7, 5.3, 16.0}
        };

        for (double[] coeff : coefficients) {
            double[] solutions = SolveCubic.solveCubic(coeff[0], coeff[1], coeff[2], coeff[3]);
            printSolutions(solutions);
        }
    }

    private static void testRandomCubicFunctions() {
        for (int a = 1; a < 10; a++) {
            for (int b = 40; b > 0; b--) {
                for (int c = 5; c < 15; c++) {
                    for (int d = -90; d > -500; d -= 10) {
                        double[] solutions = SolveCubic.solveCubic(a, b / 4.0, c + 0.61, d / 100.0);
                        printSolutions(solutions);
                    }
                }
            }
        }
    }

    private static void testIntegerSqrRoots() {
        for (int i = 0; i <= 100000; i += 2) {
            long q = usqrt(i);
            System.out.println("sqrt(" + i + ") = " + q);
        }

        for (long l = 0x3fed0169L; l < 0x3fed4169L; l++) {
            long q = usqrt(l);
            System.out.printf("sqrt(%X) = %X%n", l, q);
        }
    }

    private static void testAngleConversion() {
        for (double x = 0; x <= 360; x += 0.001) {
            System.out.printf("%3.0f degrees = %.12f radians%n", x, Math.toRadians(x));
        }

        for (double x = 0; x <= 2 * Math.PI + 1e-6; x += Math.PI / 5760) {
            System.out.printf("%.12f radians = %3.0f degrees%n", x, Math.toDegrees(x));
        }
    }

    private static void printSolutions(double[] solutions) {
        System.out.print("Solutions:");
        for (double solution : solutions) {
            System.out.print(" " + String.format("%.6f", solution));
        }
        System.out.println();
    }

    public static long usqrt(long x) {
        return (long) Math.sqrt(x);
    }

}

