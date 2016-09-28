import java.util.Scanner;
import java.util.HashMap;

public class SpaceWeight {
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        
        int earth_weight;
        int planet_id;
        double native_weight;
                
        System.out.print("Please enter your current earth weight (pounds): ");
        earth_weight = input.nextInt();
        
        System.out.println("\n\nI have information for the following planets:");
        System.out.println("\t1. Venus\t2. Mars\t\t3.Jupiter");
        System.out.println("\t4. Saturn\t5. Uranus\t6. Neptune");
        
        System.out.print("\nWhich planet are you visiting? ");
        planet_id = input.nextInt(); 
        
        HashMap<Integer, Double> gravity = new HashMap<Integer,Double>();
        gravity.put(1, 0.78);
        gravity.put(2, 0.39);
        gravity.put(3, 2.65);
        gravity.put(4, 1.17);
        gravity.put(5, 1.05);
        gravity.put(6, 1.23);
        
        native_weight = earth_weight / gravity.get(planet_id);
                
        System.out.printf("\nYour weight would be %.2f pounds on that planet\n", native_weight);
    }
}
