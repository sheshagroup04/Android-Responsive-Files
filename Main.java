import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the value of multiplication: ");
        float a = scanner.nextFloat();
        for (int i = 1; i <= 1000; i++) {
            System.out.println("<dimen name=\"dim_" + i + "\">" + (a * i) + "dp</dimen>");
        }
    }
}