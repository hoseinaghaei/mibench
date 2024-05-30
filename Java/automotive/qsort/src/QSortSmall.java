import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class QSortSmall {
    private static final int MAX_ARRAY = 60000;

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Usage: java QSortSmall <file>");
            System.exit(-1);
        }

        String filename = args[0];
        String[] array = new String[MAX_ARRAY];
        int count = 0;

        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = reader.readLine()) != null && count < MAX_ARRAY) {
                array[count] = line.trim();
                count++;
            }
        } catch (IOException e) {
            e.printStackTrace();
            System.exit(-1);
        }

        System.out.println("\nSorting " + count + " elements.\n");

        String[] filledArray = Arrays.copyOfRange(array, 0, count);

        Arrays.sort(filledArray, (a, b) -> b.compareTo(a));

        for (String str : filledArray) {
            System.out.println(str);
        }
    }
}
