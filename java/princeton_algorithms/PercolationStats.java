import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class PercolationStats {
    
    private int numTrials;
    private int gridSize;    
    private double[] thresholds;
    
    // perform trials independent experiments on an n-by-n grid
    public PercolationStats(int n, int trials) {
        if (n<=0) {
            throw new IllegalArgumentException("n must be greater than 0.");
        }
        if (trials<=0) {
            throw new IllegalArgumentException("t must be greater than 0.");
        }
        
        gridSize = n;
        numTrials = trials;
        thresholds = new double[numTrials];
        
        for ( int i=0; i<trials; i++ ) {
            thresholds[i] = getThreshold();
        }
    }
    
    private double getThreshold() {
        Percolation test = new Percolation(gridSize);
        int i;
        int j; //grid coordinates
        int count = 0;
        while (!test.percolates()) { //until percolation
            do {
                i = StdRandom.uniform(gridSize) + 1;
                j = StdRandom.uniform(gridSize) + 1;
            } while (test.isOpen(i, j));
            test.open(i, j);
            count++;
            
        }
        return (float)count/(gridSize * gridSize);
    }
    
    // sample mean of percolation threshold
    public double mean() {
        return StdStats.mean(thresholds);
    }
    
    // sample standard deviation of percolation threshold
    public double stddev() {
        if (numTrials==1) {
            return Double.NaN;
        }
        return StdStats.stddev(thresholds);
    }
    
    // low  endpoint of 95% confidence interval
    public double confidenceLo() {
        return mean() - 1.96*stddev()/Math.sqrt(numTrials);
    }
    
    // high endpoint of 95% confidence interval
    public double confidenceHi() {
        return mean() + 1.96*stddev()/Math.sqrt(numTrials);
    }
    
    // test client (described below)
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int trials = Integer.parseInt(args[1]);
        PercolationStats stat = new PercolationStats(n, trials);
        StdOut.printf("mean                     = %f%n", stat.mean());
        StdOut.printf("stddev                   = %f%n", stat.stddev());
        StdOut.printf("95%% connfidence interval = %f, %f%n", stat.confidenceLo(), stat.confidenceHi());
    }
}



