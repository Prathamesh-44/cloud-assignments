import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        long f = 1;
        for (int i = 2; i <= n; i++) f *= i;
        System.out.println("Factorial of " + n + " = " + f);
    }
}
