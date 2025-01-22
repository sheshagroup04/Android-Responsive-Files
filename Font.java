import java.util.Scanner;
public class Font {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the value of multiplication: ");
        float a = scanner.nextFloat();
        for (int i = 1; i <= 100; i++) {
            System.out.println("<dimen name=\"font_size_" + i + "\">" + (a * i) + "sp</dimen>");
        }
    }
}