import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
    
    private WeightedQuickUnionUF uf;
    private int side_len;
    private int bottom_index;
    private int top_index = 0;
    private boolean[][] opened;
    
    private void inputCheck(int i, int j) {
        if (i <= 0 || i > side_len) {
            throw new IndexOutOfBoundsException("invalid i-value");
        }
        if (j <= 0 || j > side_len) {
            throw new IndexOutOfBoundsException("invalid j-value");
        }
    }
    
    private int ijTo1D(int i, int j) {
        return (i-1) * side_len + j;
    }
    
    // create n-by-n grid, with all sites blocked
    public Percolation(int n) {
        if (n<=0) {
            throw new IllegalArgumentException("n must be greater than 0.");
        }
        side_len = n;
        uf = new WeightedQuickUnionUF(side_len * side_len + 2);
        //additional 2 for the top and bottom nodes
        opened = new boolean[side_len][side_len];
        bottom_index = side_len * side_len + 1;
    }    
    
    // open site (row i, column j) if it is not open already
    public void open(int i, int j)  {        
        inputCheck(i, j);
        if (!isOpen(i, j)) {
            opened[i-1][j-1] = true;
            
            //connect to top and bottom virtual nodes
            if (i == 1) {
                uf.union(ijTo1D(i,j), top_index);
            }
            if (i == side_len) {
                uf.union(ijTo1D(i,j), bottom_index);
            }
            
            //connect to neighbours if available/open (shor-circuit eval)
            if (i > 1 && isOpen(i-1, j)) {
                uf.union(ijTo1D(i, j), ijTo1D(i-1, j));
            }
            if (i != side_len && isOpen(i+1, j)) {
                uf.union(ijTo1D(i, j), ijTo1D(i+1, j));
            }
            if (j > 1 && isOpen(i, j-1)) {
                uf.union(ijTo1D(i, j), ijTo1D(i, j-1));
            }
            if (j != side_len && isOpen(i, j+1)) {
                uf.union(ijTo1D(i, j), ijTo1D(i, j+1));
            }
        }
    }   
    
    // is site (row i, column j) open?
    public boolean isOpen(int i, int j) {
        inputCheck(i, j);
        return opened[i-1][j-1];
    }
    
    // is site (row i, column j) full?
    public boolean isFull(int i, int j)  {
        inputCheck(i, j);
        return uf.connected(ijTo1D(i, j), top_index);
    }
    // does the system percolate?
    public boolean percolates() {
        return uf.connected(top_index, bottom_index);
    }
    
    // test client (optional)
    public static void main(String[] args) {
        
    }
}

        
        
