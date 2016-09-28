public class CompareTo {
    public static void main(String[] args) {
        System.out.println("This will test out the compareTo() method.\n");
        
        //it gives a positive value when a is after b alphabetically
        // a.compareTo(b) - a and b are Strings
                
        System.out.print("Comparing \"axe\" with \"dog\" gives a value of: ");
        System.out.println("axe".compareTo("dog"));
        
        System.out.print("Comparing \"zaaaaaaa\" with \"azzzzzzzzzz\" gives a value of: ");
        System.out.println("zaaaaaaa".compareTo("azzzzzzzzzz"));
        
        System.out.print("Comparing \"dog\" with \"axe\" gives a value of: ");
        System.out.println("dog".compareTo("axe"));
        
        System.out.print("Comparing \"axe\" with \"add\" gives a value of: ");
        System.out.println("axe".compareTo("add"));
        
        System.out.print("Comparing \"axe\" with \"adder\" gives a value of: ");
        System.out.println("axe".compareTo("adder"));
        
        System.out.print("Comparing \"axe\" with \"addu\" gives a value of: ");
        System.out.println("axe".compareTo("addu"));
        
        System.out.print("Comparing \"axe\" \"axeaxe\" gives a value of: ");
        System.out.println("axe".compareTo("axeaxe"));
        
        System.out.print("Comparing \"axe\" \"axeaxeaxe\" gives a value of: ");
        System.out.println("axe".compareTo("axeaxeaxe"));       
    }
}
