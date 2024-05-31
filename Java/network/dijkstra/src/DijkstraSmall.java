import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class DijkstraSmall {
    public static final int NUM_NODES = 100;
    public static final int NONE = 9999;

    private static final int[][] AdjMatrix = new int[NUM_NODES][NUM_NODES];
    private static final Node[] rgnNodes = new Node[NUM_NODES];
    private static final Queue qHead = new Queue();

    static {
        for (int i = 0; i < NUM_NODES; i++) {
            rgnNodes[i] = new Node();
            rgnNodes[i].iDist = NONE;
            rgnNodes[i].iPrev = NONE;
        }
    }

    public static void printPath(Node[] rgnNodes, int chNode) {
        if (rgnNodes[chNode].iPrev != NONE) {
            printPath(rgnNodes, rgnNodes[chNode].iPrev);
        }
        System.out.print(chNode + " ");
    }

    public static void dijkstra(int start, int end) {
        for (int ch = 0; ch < NUM_NODES; ch++) {
            rgnNodes[ch].iDist = NONE;
            rgnNodes[ch].iPrev = NONE;
        }

        if (start == end) {
            System.out.println("Shortest path is 0 in cost. Just stay where you are.");
        } else {
            rgnNodes[start].iDist = 0;
            rgnNodes[start].iPrev = NONE;
            qHead.enqueue(new QItem(start, 0, NONE));

            while (!qHead.empty()) {
                QItem qHeadDequeue = qHead.dequeue();
                for (int i = 0; i < NUM_NODES; i++) {
                    int iCost = AdjMatrix[qHeadDequeue.iNode][i];
                    if (iCost != NONE) {
                        if (rgnNodes[i].iDist == NONE || rgnNodes[i].iDist > (iCost + qHeadDequeue.iDist)) {
                            rgnNodes[i].iDist = qHeadDequeue.iDist + iCost;
                            rgnNodes[i].iPrev = qHeadDequeue.iNode;
                            qHead.enqueue(new QItem(i, qHeadDequeue.iDist + iCost, qHeadDequeue.iNode));
                        }
                    }
                }
            }

            System.out.print("Shortest path is " + rgnNodes[end].iDist + " in cost. Path is: ");
            printPath(rgnNodes, end);
            System.out.println();
        }
    }

    public static void main(String[] args) throws IOException {
        if (args.length < 1) {
            System.out.println("Usage: java Dijkstra <filename>");
            System.out.println("Only supports matrix size defined in NUM_NODES.");
            return;
        }

        String filename = args[0];
        BufferedReader br = new BufferedReader(new FileReader(filename));
        for (int i = 0; i < NUM_NODES; i++) {
            String[] row = br.readLine().trim().split("\\s+");
            for (int j = 0; j < NUM_NODES; j++) {
                AdjMatrix[i][j] = Integer.parseInt(row[j]);
            }
        }
        br.close();

        int i = 0;
        int j = NUM_NODES / 2;
        while (i < 20) {
            j = j % NUM_NODES;
            dijkstra(i, j);
            i++;
            j++;
        }
    }
}
