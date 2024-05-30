import java.util.Arrays;

public class SolveCubic {

    public static double[] solveCubic(double a, double b, double c, double d) {
        double[] x = new double[3];
        Arrays.fill(x, 0.0);

        double a1 = b / a;
        double a2 = c / a;
        double a3 = d / a;

        double q = (a1 * a1 - 3.0 * a2) / 9.0;
        double r = (2.0 * a1 * a1 * a1 - 9.0 * a1 * a2 + 27.0 * a3) / 54.0;
        double r2_q3 = r * r - q * q * q;

        int solutions;
        if (r2_q3 <= 0) {
            solutions = 3;
            double theta = Math.acos(r / Math.sqrt(q * q * q));
            x[0] = -2.0 * Math.sqrt(q) * Math.cos(theta / 3.0) - a1 / 3.0;
            x[1] = -2.0 * Math.sqrt(q) * Math.cos((theta + 2.0 * Math.PI) / 3.0) - a1 / 3.0;
            x[2] = -2.0 * Math.sqrt(q) * Math.cos((theta + 4.0 * Math.PI) / 3.0) - a1 / 3.0;
        } else {
            solutions = 1;
            x[0] = Math.pow(Math.sqrt(r2_q3) + Math.abs(r), 1 / 3.0);
            x[0] += q / x[0];
            x[0] *= r < 0.0 ? 1 : -1;
            x[0] -= a1 / 3.0;
        }

        double[] result = new double[solutions];
        System.arraycopy(x, 0, result, 0, solutions);
        return result;
    }
}
