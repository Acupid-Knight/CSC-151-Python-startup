import java.util.Scanner;

class M6CW1_MackA { 
    public static void main(String[] args) {
        runProgram();
    }

    public static void runProgram() {
        System.out.println("Method Project");
        Scanner in = new Scanner(System.in);
        String keep_going = "yes";
        while (keep_going.equalsIgnoreCase("yes")) {
            displayMenu();
            System.out.println();
            System.out.print("Do you want to run the program again? Enter yes or no: ");
            keep_going = in.next();
            System.out.println();
        }
        System.out.println("Program has terminated!");
    }

    public static void displayMenu() {
        System.out.println();
        System.out.println("Menu");
        System.out.println();
        System.out.println("1) M6HW1");
        System.out.println("2) M6HW2");
        System.out.println("3) M6HW3");
        System.out.println("4) Exit");
        System.out.println();
        System.out.print("Selection: ");
        Scanner in = new Scanner(System.in);

        switch (in.nextInt()) {
            case 1:
                getM6HW1();
                displayMenu();
                break;
            case 2:
                getM6HW2();
                displayMenu();
                break;
            case 3:
                getM6HW3();
                displayMenu();
                break;
            case 4:
                System.out.println("Exiting the program");
                break;
            default:
                System.out.println("Unrecognized option.. Try again");
                displayMenu();
        }
    }

    public static void getM6HW1() {
        System.out.println("You picked M6HW1");
        // Add your code for M6HW1 here
    }

    public static void getM6HW2() {
        System.out.println("You picked M6HW2");
        // Add your code for M6HW2 here
    }

    public static void getM6HW3() {
        System.out.println("You picked M6HW3");
        // Add your code for M6HW3 here
    }
}
