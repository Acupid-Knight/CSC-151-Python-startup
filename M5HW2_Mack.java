import java.util.Scanner;

public class M5HW2_Mack {

    public static void main(String[] args) {
        final double WIDGET_PRICE = 4.79;
        final double BASE_SALARY = 2000.00;
        Scanner input = new Scanner(System.in);
        String repeat;

        do {
            int totalSold = 0;
            int totalReturned = 0;

            // Collect widgets sold
            for (int week = 1; week <= 4; week++) {
                System.out.print("Enter widgets sold for week " + week + ": ");
                int sold = input.nextInt();
                totalSold += sold;
            }

            // Collect widgets returned
            for (int week = 1; week <= 4; week++) {
                System.out.print("Enter widgets returned for week " + week + ": ");
                int returned = input.nextInt();
                totalReturned += returned;
            }

            int netSold = totalSold - totalReturned;
            double salesAmount = netSold * WIDGET_PRICE;

            double commissionRate;
            if (netSold >= 300) {
                commissionRate = 0.25;
            } else if (netSold >= 200) {
                commissionRate = 0.15;
            } else if (netSold >= 100) {
                commissionRate = 0.10;
            } else {
                commissionRate = 0.05;
            }

            double commission = salesAmount * commissionRate;
            double monthlySalary = BASE_SALARY + commission;

            System.out.println("\nSales Person: Anthony Cameron");
            System.out.println("Widgets Sold: " + totalSold);
            System.out.println("Widgets Returned: " + totalReturned);
            System.out.println("Net Widgets Sold: " + netSold);
            System.out.println("Widgets Sales Amount: $" + salesAmount);
            System.out.println("Commission Amount: $" + commission);
            System.out.println("Monthly Salary: $" + monthlySalary);

            System.out.print("\nWould you like to run the program again? (y/n): ");
            repeat = input.next();
        } while (repeat.equalsIgnoreCase("y"));

        input.close();
    }
}

