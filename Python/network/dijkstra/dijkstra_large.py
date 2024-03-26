NUM_NODES = 100
NONE = 9999

class Node:
    def __init__(self):
        self.iDist = NONE
        self.iPrev = NONE

class QItem:
    def __init__(self, i_node, i_dist, i_prev):
        self.iNode = i_node
        self.iDist = i_dist
        self.iPrev = i_prev

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def empty(self):
        return len(self.items) == 0

AdjMatrix = [[NONE] * NUM_NODES for _ in range(NUM_NODES)]
rgnNodes = [Node() for _ in range(NUM_NODES)]
qHead = Queue()


def print_path(rgn_nodes, ch_node):
    if rgn_nodes[ch_node].iPrev != NONE:
        print_path(rgn_nodes, rgn_nodes[ch_node].iPrev)
    print(ch_node, end=" ")


def dijkstra(start: int, end: int):
    for ch in range(NUM_NODES):
        rgnNodes[ch].iDist = NONE
        rgnNodes[ch].iPrev = NONE

    if start == end:
        print("Shortest path is 0 in cost. Just stay where you are.")
    else:
        rgnNodes[start].iDist = 0
        rgnNodes[start].iPrev = NONE
        qHead.enqueue(QItem(start, 0, NONE))

        while not qHead.empty():
            q_head_dequeue = qHead.dequeue()
            for i in range(NUM_NODES):
                iCost = AdjMatrix[q_head_dequeue.iNode][i]
                if iCost != NONE:
                    if rgnNodes[i].iDist == NONE or rgnNodes[i].iDist > (iCost + q_head_dequeue.iDist):
                        rgnNodes[i].iDist = q_head_dequeue.iDist + iCost
                        rgnNodes[i].iPrev = q_head_dequeue.iNode
                        qHead.enqueue(QItem(i, q_head_dequeue.iDist + iCost, q_head_dequeue.iNode))

        print(f"Shortest path is {rgnNodes[end].iDist} in cost. Path is: ", end="")
        print_path(rgnNodes, end)
        print()

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: dijkstra <filename>")
        print("Only supports matrix size is #define'd.")
        return

    # Open the adjacency matrix file
    filename = sys.argv[1]
    with open(filename, "r") as fp:
        # Make a fully connected matrix
        for i in range(NUM_NODES):
            row = list(map(int, fp.readline().split()))
            AdjMatrix[i] = row

    # Finds 20 shortest paths between nodes
    i = 0
    j = NUM_NODES // 2
    while i < 100:
        j = j % NUM_NODES
        dijkstra(i, j)
        i += 1
        j += 1

if __name__ == "__main__":
    main()
