public class QItem {
    public int iNode;
    public int iDist;
    public int iPrev;

    public QItem(int iNode, int iDist, int iPrev) {
        this.iNode = iNode;
        this.iDist = iDist;
        this.iPrev = iPrev;
    }
}