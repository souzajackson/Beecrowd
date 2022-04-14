import java.util.Scanner;

class Main{
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int num1 = entrada.nextInt();
        int num2 = entrada.nextInt();
        
        int prod = num1 * num2;

        System.out.println("PROD = " + prod);
    }
}
