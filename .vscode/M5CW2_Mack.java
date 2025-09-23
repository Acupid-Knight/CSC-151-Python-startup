import java.util.Scanner;

public class M5CW2_Mack { 
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int score1, score2, score3, score4, score5;

        // Do...While loop to get five grades from the user
        do {
            System.out.print("Enter score 1 (0-100): ");
            score1 = scanner.nextInt();
        } while (score1 < 0 || score1 > 100); // Validate score 1
        
        do {
            System.out.print("Enter score 2 (0-100): ");
            score2 = scanner.nextInt();
        } while (score2 < 0 || score2 > 100); // Validate score 2

        do {
            System.out.print("Enter score 3 (0-100): ");
            score3 = scanner.nextInt();
        } while (score3 < 0 || score3 > 100); // Validate score 3

        do {
            System.out.print("Enter score 4 (0-100): ");
            score4 = scanner.nextInt();
        } while (score4 < 0 || score4 > 100); // Validate score 4

        do {
            System.out.print("Enter score 5 (0-100): ");
            score5 = scanner.nextInt();
        } while (score5 < 0 || score5 > 100); // Validate score 5
        
        // Calculate average
        int average = (score1 + score2 + score3 + score4 + score5) / 5;
        
        // Determine the grade
        char grade;
        if (average >= 90) {
            grade = 'A';
        } else if (average >= 80) {
            grade = 'B';
        } else if (average >= 70) {
            grade = 'C';
        } else if (average >= 60) {
            grade = 'D';
        } else {
            grade = 'F';
        }
        
        // Display the result
        System.out.println("\nThe student's average score is: " + average);
        System.out.println("The student's grade is: " + grade);
        
        scanner.close();
    }
}

