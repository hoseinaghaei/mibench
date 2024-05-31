public class BitCount2 {

    public static int bitCount(long number) {
        number = ((number & 0xAAAAAAAAL) >> 1) + (number & 0x55555555);
        number = ((number & 0xCCCCCCCCL) >> 2) + (number & 0x33333333);
        number = ((number & 0xF0F0F0F0L) >> 4) + (number & 0x0F0F0F0F);
        number = ((number & 0xFF00FF00L) >> 8) + (number & 0x00FF00FF);
        number = ((number & 0xFFFF0000L) >> 16) + (number & 0x0000FFFF);
        return (int) number;
    }

    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java BitCount <number>");
            System.exit(-1);
        }

        for (String arg : args) {
            try {
                long n = Integer.parseInt(arg);
                long i = bitCount(n);
                System.out.printf("%d contains %d bit%s set%n", n, i, (i != 1) ? "s" : "");
            } catch (NumberFormatException e) {
                System.out.println("Invalid number: " + arg);
            }
        }
    }
}

