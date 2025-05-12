import java.util.Scanner;

public class Mack_Final {

    // Constant for Sales Tax
    public static final double SALES_TAX_RATE = 0.07;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        displayInfo();

        // Step 1: Get item count
        int itemCount = getItemCount(scanner);

        // Step 2: Get total item cost
        double subtotal = getItemPrices(scanner, itemCount);

        // Step 3: Calculate sales tax
        double taxDue = getSalesTax(subtotal);

        // Step 4: Calculate total owed
        double totalOwed = getTotalOwed(subtotal, taxDue);

        // Step 5: Display all values
        displayValues(itemCount, subtotal, taxDue, totalOwed);
    }

    // Method 1: Display personal info
    public static void displayInfo() {
        System.out.println("Your Name: Antonio Mack Jr");
        System.out.println("2025 Spring CIS 115 Final Exam");
        System.out.println("I did not use AI to help me with this final");
        System.out.println("I used only concepts covered in class");
        System.out.println("--------------------------------------------------");
    }

    // Function 2: Get number of items
    public static int getItemCount(Scanner scanner) {
        System.out.print("Enter the number of items purchased: ");
        int count = scanner.nextInt();
        return count;
    }

    // Function 3: Get item prices with validation and subtotal
    public static double getItemPrices(Scanner scanner, int itemCount) {
        double total = 0.0;
        for (int i = 1; i <= itemCount; i++) {
            double price;
            while (true) {
                System.out.print("Enter price for item #" + i + ": ");
                price = scanner.nextDouble();
                if (price >= 0) {
                    break;
                } else {
                    System.out.println("Price cannot be negative. Please re-enter.");
                }
            }
            total += price;
        }
        return total;
    }

    // Function 4: Get sales tax
    public static double getSalesTax(double subtotal) {
        return subtotal * SALES_TAX_RATE;
    }

    // Function 5: Get total owed
    public static double getTotalOwed(double subtotal, double tax) {
        return subtotal + tax;
    }

    // Method 6: Display final values
    public static void displayValues(int itemCount, double subtotal, double tax, double total) {
        System.out.println("--------------------------------------------------");
        System.out.println("Number of Items: " + itemCount);
        System.out.printf("Subtotal: $%.2f\n", subtotal);
        System.out.printf("Tax Due: $%.2f\n", tax);
        System.out.printf("Total Owed: $%.2f\n", total);
    }
}
