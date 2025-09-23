import java.util.Scanner;


public class HelloGoodbye {
    public static void main(String[] args) {
        // Create a Scanner object to read user input
        Scanner scanner = new Scanner(System.in);

        // Continue the conversation as long as the user says "yes"
        String continueResponse;
        do {
            // Ask a series of questions
            System.out.println("Hello and welcome to the program!");

            // Ask for the user's name
            System.out.print("What is your name? ");
            String name = scanner.nextLine();  // Read name input

            // Respond based on the name
            if (name != null && !name.trim().isEmpty()) {
                System.out.println("Hello, " + name + "! It's nice to meet you.");
            } else {
                System.out.println("Hello! It's nice to meet you.");
            }

            // Ask the user for their age
            System.out.print("How old are you? ");
            int age = scanner.nextInt();  // Read age as an integer

            // Respond based on the user's age
            if (age >= 18) {
                System.out.println("You are an adult.");
            } else {
                System.out.println("You are a minor.");
            }

            // Ask if the user wants to continue
            scanner.nextLine();  // Clear the buffer before the next question
            System.out.print("Would you like to continue? (yes/no) ");
            continueResponse = scanner.nextLine();

            if ("yes".equalsIgnoreCase(continueResponse)) {
                System.out.println("Great! Let's keep talking.");
            } else {
                System.out.println("Goodbye! Hope to see you again!");
            }

        } while ("yes".equalsIgnoreCase(continueResponse)); // Keep asking if the response is "yes"

        scanner.close();  // Close the scanner object to prevent resource leak
    }
}