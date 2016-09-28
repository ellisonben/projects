import javax.swing.*;
import java.awt.*;

public class FrameWithPanel {
    public static void main(String[] args) {
        PanelFrame f = new PanelFrame();
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}

class PanelFrame extends JFrame {
    public PanelFrame() {
        setTitle("This is a frame with a panel.");
        setSize(300,200);
        setLocation(0,200); //location window pops up on screen
        
        Panel panel = new Panel();
        Container cp = getContentPane();
        cp.add(panel);
    }
}

class Panel extends JPanel {
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawString("Hi", 200, 100); // words, x, y
    }
}
