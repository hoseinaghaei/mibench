import java.util.Random;

public class BitCount {

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java BitCountBenchmark <iterations>");
            System.exit(1);
        }

        int iterations = Integer.parseInt(args[0]);

        FunctionWrapper[] funcs = {
                BitCount1::bitCount,        // Optimized 1 bit/loop counter
                BitCount2::bitCount,        // Ratko's mystery algorithm
                BitCount4::ntblBitcnt,     // Recursive bit count by nybbles
                BitCount3::ntblBitcount,   // Non-recursive bit count by nybbles
                BitCount3::BW_btblBitcount,// Non-recursive bit count by bytes (BW)
                BitCount3::AR_btblBitcount,// Non-recursive bit count by bytes (AR)
                BitCount::bit_shifter                // Shift and count bits
        };

        String[] funcsName = {
                "Optimized 1 bit/loop counter",
                "Ratko's mystery algorithm",
                "Recursive bit count by nybbles",
                "Non-recursive bit count by nybbles",
                "Non-recursive bit count by bytes (BW)",
                "Non-recursive bit count by bytes (AR)",
                "Shift and count bits"
        };

        System.out.println("Bit counter algorithm benchmark\n");

        long minTime = Long.MAX_VALUE;
        String minFunc = "";
        long maxTime = Long.MIN_VALUE;
        String maxFunc = "";

        for (int i = 0; i < funcs.length; i++) {
            long startTime = System.nanoTime();
            int totalBits = 0;
            Random rand = new Random();
            int seed = rand.nextInt();

            for (int j = 0; j < iterations; j++) {
                totalBits += funcs[i].apply(seed);
                seed += 13;
            }

            long elapsedTime = System.nanoTime() - startTime;

            if (elapsedTime < minTime) {
                minTime = elapsedTime;
                minFunc = funcsName[i];
            }

            if (elapsedTime > maxTime) {
                maxTime = elapsedTime;
                maxFunc = funcsName[i];
            }

            System.out.printf("%-38s > Time: %.3f sec; Bits: %d%n", funcsName[i], elapsedTime / 1e9, totalBits);
        }

        System.out.println("\nBest  > " + minFunc);
        System.out.println("Worst > " + maxFunc);
    }

    public static int bit_shifter(int x) {
        int i, n;
        for (i = n = 0; x != 0 && i < (Integer.SIZE); ++i, x >>= 1) {
            n += (int) (x & 1L);
        }
        return n;
    }

    @FunctionalInterface
    interface FunctionWrapper {
        int apply(int x);
    }
}
