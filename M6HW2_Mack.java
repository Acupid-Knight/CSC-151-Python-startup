import java.util.Scanner;

public class M6HW2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter Homeowner's Name: ");
        String name = input.nextLine();

        System.out.print("Enter Previous Month's Reading: ");
        double previousReading = input.nextDouble();

        System.out.print("Enter Current Month's Reading: ");
        double currentReading = input.nextDouble();

        double waterUsage = currentReading - previousReading;
        double charge = (waterUsage * 0.20) + 50.00;

        System.out.println("\nHomeowner's Name: " + name);
        System.out.println("Previous Reading: " + previousReading);
        System.out.println("Current Reading: " + currentReading);
        System.out.println("Water Usage: " + waterUsage + " gallons");
        System.out.println("Total Monthly Bill: $" + charge);

        input.close();
    }
}
