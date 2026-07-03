import java.util.Scanner;

public class EmployeeSystem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("--- 🏢 Employee Entry ---");
        
        System.out.print("Enter Name: ");
        String name = sc.nextLine();
        
        System.out.print("Enter Salary: ");
        String salary = sc.nextLine();
        
        System.out.println("\n--- Saved Profile ---");
        System.out.println("Employee Name: " + name);
        System.out.println("Monthly Salary: " + salary);
    }
}
