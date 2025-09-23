import java.util.Scanner;

public class M4HW1_Mack{
    public static void main(String[] args) {
        // Constants
        final double WIDGET_PRICE = 4.79;
        final double BASE_SALARY = 2000;

        // Declare variables
        String salespersonName;
        int widgetsSold, widgetsReturned, netWidgetsSold;
        double widgetSalesAmount, commissionAmount, monthlySalary;
        double commissionRate = 0.0;

        // Create scanner object for input
        Scanner scanner = new Scanner(System.in);

        // Input salesperson's name
        System.out.print("Enter salesperson's name: ");
        salespersonName = scanner.nextLine();

        // Input widgets sold and returned
        System.out.print("Enter widgets sold: ");
        widgetsSold = scanner.nextInt();
        System.out.print("Enter widgets returned: ");
        widgetsReturned = scanner.nextInt();

        // Calculate net widgets sold
        netWidgetsSold = widgetsSold - widgetsReturned;

        // Calculate widget sales amount
        widgetSalesAmount = netWidgetsSold * WIDGET_PRICE;

        // Determine the commission rate based on net widgets sold
        if (netWidgetsSold <= 100) {
            commissionRate = 0.10; // 10%
        } else if (netWidgetsSold <= 199) {
            commissionRate = 0.15; // 15%
        } else if (netWidgetsSold <= 299) {
            commissionRate = 0.20; // 20%
        } else {
            commissionRate = 0.25; // 25%
        }

        // Calculate commission amount
        commissionAmount = commissionRate * widgetSalesAmount;

        // Calculate monthly salary
        monthlySalary = commissionAmount + BASE_SALARY;

        // Output results
        System.out.println("Sales Person: " + salespersonName);
        System.out.println("Net Widgets Sold: " + netWidgetsSold);
        System.out.println("Widgets Sales Amount: " + String.format("%.2f", widgetSalesAmount));
        System.out.println("Commission Amount: " + String.format("%.2f", commissionAmount));
        System.out.println("Monthly Salary: " + String.format("%.2f", monthlySalary));

        // Close the scanner
        scanner.close();
    }
}
