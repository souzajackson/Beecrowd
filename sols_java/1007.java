import java.util.Scanner;

class Main2{
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int num1 = entrada.nextInt();
        int num2 = entrada.nextInt();
        int num3 = entrada.nextInt();
        int num4 = entrada.nextInt();

        System.out.print("DIFERENCA = ");
        System.out.println(num1 * num2 - num3 * num4);

        entrada.close();
    }
}
