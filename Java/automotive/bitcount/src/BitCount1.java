public class BitCount1 {

    public static int bitCount(long x) {
        int count = 0;
        while (x != 0) {
            count += 1;
            x = x & (x - 1);
        }
        return count;
    }

    public static void main(String[] args) {
        int x = 29; // Example input
        System.out.println("The number of 1 bits in " + x + " is: " + bitCount(x));
    }
}
