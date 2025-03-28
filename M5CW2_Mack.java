import java.util.Scanner;

public class M5CW2_Mack {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int sum = 0;

        // Use a for loop to add numbers from 1 to 5
        for (int i = 1; i <= 5; i++) {
            sum += i; // Add the current number to sum
        }

        // Output the result
        System.out.println("The sum of the numbers is: " + sum);
    }
}

