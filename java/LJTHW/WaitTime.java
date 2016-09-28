import javax.swing.*;

public class WaitTime { 
    public static void main(String[] args) {
        
        String name = JOptionPane.showInputDialog("What is your surname?");
        
        if (name.compareTo("Carswell") <= 0) {
            System.out.printf("You don't have to wait long, %s.\n", name);
        }
        else if (name.compareTo("Jones") <= 0) {
            System.out.printf("The wait is not too bad, %s.\n", name);
        }
        else if (name.compareTo("Smith") <= 0) {
            System.out.printf("Looks like a bit of a wait, %s.\n", name);
        }
        else if (name.compareTo("Young") <= 0) {
            System.out.printf("It's gonna be a while, %s.\n", name);
        }
        else {
            System.out.printf("Sorry, I hope you haven't made plans, %s.\n", name);
        }
        
        System.exit(0);
    }
}
