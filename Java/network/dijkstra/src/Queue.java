import java.util.LinkedList;

public class Queue {
    private final LinkedList<QItem> items;

    public Queue() {
        this.items = new LinkedList<>();
    }

    public void enqueue(QItem item) {
        this.items.add(item);
    }

    public QItem dequeue() {
        return this.items.removeFirst();
    }

    public boolean empty() {
        return this.items.isEmpty();
    }
}
