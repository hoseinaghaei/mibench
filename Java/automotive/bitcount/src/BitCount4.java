
public class BitCount4 {

    // Table lookup for counting bits in each nybble
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

    public static int ntblBitcnt(long x) {
        int cnt = bits[(int) (x & 0x0000000FL)];
        if (x != 0L) {
            cnt += ntblBitcnt(x >>> 4);
        }
        return cnt;
    }

    public static int btblBitcnt(long x) {
        int cnt = bits[(int) (x & 0xFF)];
        if (x != 0L) {
            cnt += btblBitcnt(x >> 8);
        }
        return cnt;
    }

    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java BitCount <number>");
            System.exit(-1);
        }

        for (String arg : args) {
            try {
                int n = Integer.parseInt(arg);
                int i = ntblBitcnt(n);
                System.out.printf("%d contains %d bit%s set%n", n, i, (i != 1) ? "s" : "");
            } catch (NumberFormatException e) {
                System.out.println("Invalid number: " + arg);
            }
        }
    }
}

