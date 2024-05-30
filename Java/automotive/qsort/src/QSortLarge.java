import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Comparator;

public class QSortLarge {
    private static final int MAX_ARRAY = 60000;

    static class My3DVertexClass {
        long x, y, z;
        double distance;

        My3DVertexClass(long x, long y, long z) {
            this.x = x;
            this.y = y;
            this.z = z;
            this.distance = Math.sqrt((double) x * x + (double) y * y + (double) z * z);
        }
    }

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Usage: java QSortLarge <file>");
            System.exit(-1);
        }

        String filename = args[0];
        My3DVertexClass[] array = new My3DVertexClass[MAX_ARRAY];
        int count = 0;

        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = reader.readLine()) != null && count < MAX_ARRAY) {
                String[] parts = line.split("\\s+");
                long x = Long.parseLong(parts[0]);
                long y = Long.parseLong(parts[1]);
                long z = Long.parseLong(parts[2]);
                array[count] = new My3DVertexClass(x, y, z);
                count++;
            }
        } catch (IOException e) {
            e.printStackTrace();
            System.exit(-1);
        }

        System.out.println("\nSorting " + count + " vectors based on distance from the origin.\n");

        // Copy only the filled portion of the array to a new array
        My3DVertexClass[] filledArray = Arrays.copyOfRange(array, 0, count);

        // Sort the filled portion of the array based on distance
        Arrays.sort(filledArray, Comparator.comparingDouble(a -> a.distance));

        for (My3DVertexClass vertex : filledArray) {
            System.out.println(vertex.x + " " + vertex.y + " " + vertex.z);
        }
    }
}
