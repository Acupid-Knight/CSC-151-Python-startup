import java.util.Scanner;

public class M4HW2_Mack {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Step 1: Get US Citizenship status
        System.out.println("Enter your US citizenship status (true/false):");
        boolean isCitizen = scanner.nextBoolean();
        
        if (!isCitizen) {
            System.out.println("You cannot vote because you are not a US citizen.");
            return;
        }

        // Step 2: Get county residency status
        System.out.println("Enter your county residency status (true/false):");
        boolean isResident = scanner.nextBoolean();
        
        if (!isResident) {
            System.out.println("You cannot vote because you do not live in the county.");
            return;
        }

        // Step 3: Get number of days lived in the county
        System.out.println("Enter the number of days you have lived in the county:");
        int daysInCounty = scanner.nextInt();
        
        if (daysInCounty < 30) {
            System.out.println("You cannot vote because you have not lived in the county for 30 days.");
            return;
        }

        // Step 4: Get age
        System.out.println("Enter your age:");
        int age = scanner.nextInt();
        
        if (age < 18) {
            System.out.println("You cannot vote because you are under 18 years of age.");
            return;
        }

        // Step 5: Get felony status
        System.out.println("Enter your felony status (true/false):");
        boolean isFelon = scanner.nextBoolean();
        
        if (isFelon) {
            System.out.println("You cannot vote because you are serving a felony sentence or on probation.");
            return;
        }

        // If all conditions are met
        System.out.println("You are eligible to vote!");
    }
}
