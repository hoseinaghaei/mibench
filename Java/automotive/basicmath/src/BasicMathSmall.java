import java.util.Arrays;

public class BasicMathSmall {

    public static void main(String[] args) {
        System.out.println("********* CUBIC FUNCTIONS ***********");
        double a, b, c, d;

        a = 1.0; b = -10.5; c = 32.0; d = -30.0;
        double[] solutions1 = SolveCubic.solveCubic(a, b, c, d);
        printSolutions(solutions1);

        a = 1.0; b = -4.5; c = 17.0; d = -30.0;
        double[] solutions2 = SolveCubic.solveCubic(a, b, c, d);
        printSolutions(solutions2);

        a = 1.0; b = -3.5; c = 22.0; d = -31.0;
        double[] solutions3 = SolveCubic.solveCubic(a, b, c, d);
        printSolutions(solutions3);

        a = 1.0; b = -13.7; c = 1.0; d = -35.0;
        double[] solutions4 = SolveCubic.solveCubic(a, b, c, d);
        printSolutions(solutions4);

        for (int a1 = 1; a1 < 10; a1++) {
            for (int b1 = 10; b1 > 0; b1--) {
                for (int c1 = 5; c1 < 15; c1++) {
                    for (int d1 = -1; d1 > -11; d1--) {
                        double[] solutions = SolveCubic.solveCubic(a1, b1, c1, d1);
                        printSolutions(solutions);
                    }
                }
            }
        }

        System.out.println("********* INTEGER SQUARE ROOTS ***********");
        for (int i = 0; i <= 1000; i++) {
            System.out.println("sqrt(" + i + ") = " + usqrt(i));
        }

        long l = 0x3fed0169L;
        long sqrtL = usqrt(l);
        System.out.printf("\nsqrt(%X) = %X%n", l, sqrtL);

        System.out.println("********* ANGLE CONVERSION ***********");
        for (int X = 0; X <= 360; X++) {
            System.out.printf("%3d degrees = %f radians%n", X, Math.toRadians(X));
        }
        System.out.println();

        double x = 0;
        while (x < 2 * Math.PI + 1e-6) {
            System.out.printf("%f radians = %f degrees%n", x, Math.toDegrees(x));
            x += Math.PI / 100;
        }
    }

    public static long usqrt(long x) {
        return (long) Math.sqrt(x);
    }

    public static void printSolutions(double[] solutions) {
        System.out.print("Solutions:");
        for (double solution : solutions) {
            System.out.print(" " + String.format("%.6f", solution));
        }
        System.out.println();
    }
}
