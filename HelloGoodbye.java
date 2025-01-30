
public class HelloGoodbye {
    public static void main(String[] args) {
        // Display initial greeting message
        System.out.println("Hello and welcome to the program!");

        // Ask for the user's name
        String name = System.console().readLine("What is your name? ");

        // Check if the user entered a name or canceled the input
        if (name != null && !name.trim().isEmpty()) {
            // Personalized greeting message
            System.out.println("Hello, " + name + "! It's nice to meet you.");
        } else {
            // Handle case where no name was entered
            System.out.println("Hello! It's nice to meet you.");
        }

        // Ask if the user wants to continue
        String response = System.console().readLine("Would you like to continue? (yes/no) ");

        // If the user chooses YES, say goodbye
        if ("yes".equalsIgnoreCase(response)) {
            System.out.println("Thank you for using the program. Goodbye!");
        } else {
            // If the user chooses NO, say goodbye
            System.out.println("Goodbye! Hope to see you again!");
        }
    }
}