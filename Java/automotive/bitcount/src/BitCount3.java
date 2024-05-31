public class BitCount3 {

    // Bits table
    private static final int[] bits = {
            0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4,
            1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
            1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
            2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
            1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
            2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
            2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
            3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
            1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
            2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
            2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
            3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
            2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
            3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
            3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
            4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8
    };

    public static int ntblBitcount(long x) {
        return bits[(int) (x & 0x0000000FL)] +
                bits[(int) ((x & 0x000000F0L) >> 4)] +
                bits[(int) ((x & 0x00000F00L) >> 8)] +
                bits[(int) ((x & 0x0000F000L) >> 12)] +
                bits[(int) ((x & 0x000F0000L) >> 16)] +
                bits[(int) ((x & 0x00F00000L) >> 20)] +
                bits[(int) ((x & 0x0F000000L) >> 24)] +
                bits[(int) ((x & 0xF0000000L) >> 28)];
    }

    public static int BW_btblBitcount(long x) {
        return bits[(int) (x & 0xFF)] +
                bits[(int) ((x >> 8) & 0xFF)] +
                bits[(int) ((x >> 16) & 0xFF)] +
                bits[(int) ((x >> 24) & 0xFF)];
    }

    public static int AR_btblBitcount(long x) {
        int count = 0;
        while (x != 0) {
            count += bits[(int) (x & 0xFF)];
            x >>= 8;
        }
        return count;
    }

    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java BitCount <number>");
            System.exit(-1);
        }

        for (String arg : args) {
            try {
                int n = Integer.parseInt(arg);
                int i = ntblBitcount(n);
                System.out.printf("%d contains %d bit%s set%n", n, i, (i != 1) ? "s" : "");
            } catch (NumberFormatException e) {
                System.out.println("Invalid number: " + arg);
            }
        }
    }
}
