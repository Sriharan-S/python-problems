import java.util.Scanner;

public class SimpleInterest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter principal amount: ");
        double principal = scanner.nextDouble();
        
        System.out.print("Enter rate of interest: ");
        double rate = scanner.nextDouble();
        
        System.out.print("Enter time period in years: ");
        int time = scanner.nextInt();
        
        double interest = (principal * rate * time) / 100;
        
        System.out.println("Simple Interest: " + interest);
    }
}
