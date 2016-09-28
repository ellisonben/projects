import java.util.Scanner;

public class Collatz {
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        int steps = 0;
        long number;
        long largest;
        System.out.print("Starting number: ");
        number = input.nextInt();
        largest = number;
                
        while (number < 1) {
            System.out.println("This is not an appropriate starting number");
            System.out.println("Please try again: ");
            number = input.nextInt();
        } 
        
        if (number == 1) {
            System.out.println("You have started with one.");
        }
        else {   
            do {
                if (number%2 == 0) {
                    number = number/2;
                }
                else {
                    number = number*3 + 1;
                } 
                
                if (number>largest) {
                    largest = number;
                }
                
                steps++;
                System.out.print(number + "\t");
                
                if (steps%10 == 0) {
                    System.out.println("");
                }
            } while (number != 1);
        }
        
        System.out.printf("\nTerminated after %s steps.", steps);
        System.out.printf("The largest value was %s.\n", largest);
    }
}
