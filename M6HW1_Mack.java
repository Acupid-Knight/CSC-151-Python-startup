
import java.util.Scanner;

public class M6HW1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter employee name: ");
        String name = scanner.nextLine();

        System.out.print("Enter hourly pay rate: ");
        double rate = scanner.nextDouble();

        System.out.print("Enter hours worked: ");
        double hours = scanner.nextDouble();

        double grossPay = rate * hours;

        System.out.println("\n--- Gross Pay Details ---");
        System.out.println("Employee Name: " + name);
        System.out.println("Hourly Rate: $" + rate);
        System.out.println("Hours Worked: " + hours);
        System.out.println("Gross Pay: $" + grossPay);
    }
}
