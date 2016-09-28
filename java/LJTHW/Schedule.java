public class Schedule {
    public static void main(String[] args) {
        
        // This could probably be done a lot more simply using Hashmaps.
        
        //Class and teacher variables
        String course1 = "English";
        String teacher1 = "Ms. Oxtoby";
        String course2 = "Physics";
        String teacher2 = "Mr. Seed";
        String course3 = "Chemistry";
        String teacher3 = "Mrs. Cook";
        String course4 = "Mathematics";
        String teacher4 = "Mr. El-Salahi";
        String course5 = "Business Studies";
        String teacher5 = "Mr. Collins";
        String course6 = "Art & Design";
        String teacher6 = "Mr. Hindle";
        String course7 = "Religious Studies";
        String teacher7 = "Mr. Robson";
        String course8 = "Computer Technology";
        String teacher8 = "Mr. Chester";
        
        // This is the top line
        System.out.print("+");
        for (int i = 0; i<50; i++) {
            System.out.print("-");
        }
        System.out.println("+");
        
        //Teacher1
        System.out.print("| 1 |");
        for (int i=0; i<(27-course1.length()); i++) {
            System.out.print(" ");
        }
        System.out.print(course1 + " |");
        for (int i=0; i<(16-teacher1.length()); i++) {
            System.out.print(" ");
        }
        System.out.println(teacher1 + " |");
        
        //Teacher2
        System.out.print("| 2 |");
        for (int i=0; i<(27-course2.length()); i++) {
            System.out.print(" ");
        }
        System.out.print(course2 + " |");
        for (int i=0; i<(16-teacher2.length()); i++) {
            System.out.print(" ");
        }
        System.out.println(teacher2 + " |");
        
        //Teacher3
        System.out.print("| 3 |");
        for (int i=0; i<(27-course3.length()); i++) {
            System.out.print(" ");
        }
        System.out.print(course3 + " |");
        for (int i=0; i<(16-teacher3.length()); i++) {
            System.out.print(" ");
        }
        System.out.println(teacher3 + " |");
        
        //Teacher4
        System.out.print("| 4 |");
        for (int i=0; i<(27-course4.length()); i++) {
            System.out.print(" ");
        }
        System.out.print(course4 + " |");
        for (int i=0; i<(16-teacher4.length()); i++) {
            System.out.print(" ");
        }
        System.out.println(teacher4 + " |");
        
        //Teacher5
        System.out.print("| 5 |");
        for (int i=0; i<(27-course5.length()); i++) {
            System.out.print(" ");
        }
        System.out.print(course5 + " |");
        for (int i=0; i<(16-teacher5.length()); i++) {
            System.out.print(" ");
        }
        System.out.println(teacher5 + " |");
        
        //Teacher6
        System.out.print("| 6 |");
        for (int i=0; i<(27-course6.length()); i++) {
            System.out.print(" ");
        }
        System.out.print(course6 + " |");
        for (int i=0; i<(16-teacher6.length()); i++) {
            System.out.print(" ");
        }
        System.out.println(teacher6 + " |");
        
        //Teacher7
        System.out.print("| 7 |");
        for (int i=0; i<(27-course7.length()); i++) {
            System.out.print(" ");
        }
        System.out.print(course7 + " |");
        for (int i=0; i<(16-teacher7.length()); i++) {
            System.out.print(" ");
        }
        System.out.println(teacher7 + " |");
        
        //Teacher8
        System.out.print("| 8 |");
        for (int i=0; i<(27-course8.length()); i++) {
            System.out.print(" ");
        }
        System.out.print(course8 + " |");
        for (int i=0; i<(16-teacher8.length()); i++) {
            System.out.print(" ");
        }
        System.out.println(teacher8 + " |");
        
        // This is the bottom line
        System.out.print("+");
        for (int i = 0; i<50; i++) {
            System.out.print("-");
        }
        System.out.println("+");
    }
}
