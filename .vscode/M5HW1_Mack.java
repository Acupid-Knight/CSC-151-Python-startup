import java.util.Scanner;

public class M5HW1_Mack_A {

    public static void main(String[] args) {
        Scanner k = new Scanner(System.in);
        char grade;
        double average;
        String runAgain;

        do {
            System.out.print("Enter the number of grades to average: ");
            int numGrades = k.nextInt();
            double sum = 0;

            // Collect and validate grades
            for (int i = 1; i <= numGrades; i++) {
                double currentGrade;
                do {
                    System.out.print("Enter grade " + i + ": ");
                    currentGrade = k.nextDouble();
                    if (currentGrade < 0 || currentGrade > 100) {
                        System.out.println("Grade must be between 0 and 100. Please try again.");
                    }
                } while (currentGrade < 0 || currentGrade > 100);
                sum += currentGrade;
            }

            // Calculate average
            average = sum / numGrades;

            // Assign letter grade
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

            // Display results
            System.out.println("Average: " + average);
            System.out.println("Letter Grade: " + grade);

            // Prompt to run again
            System.out.print("Do you want to run the program again? (y/n): ");
            runAgain = k.next();
        } while (runAgain.equalsIgnoreCase("y"));

        System.out.println("Program exited.");
        k.close();
    }
}

