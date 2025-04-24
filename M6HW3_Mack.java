
import java.util.Scanner;

public class M6HW3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter salesperson's name: ");
        String name = scanner.nextLine();

        System.out.print("Enter number of widgets sold: ");
        int sold = scanner.nextInt();

        System.out.print("Enter number of widgets returned: ");
        int returned = scanner.nextInt();

        int netWidgets = sold - returned;
        double commission = 500 + (netWidgets * 0.10); // base salary + commission

        System.out.println("\n--- Commission Details ---");
        System.out.println("Salesperson: " + name);
        System.out.println("Net Widgets Sold: " + netWidgets);
        System.out.println("Total Pay (Base + Commission): $" + commission);
    }
}
