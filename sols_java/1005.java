import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        String num1_str = entrada.next();
        String num2_str = entrada.next();

        double num1 = Double.parseDouble(num1_str);
        double num2 = Double.parseDouble(num2_str);

        double soma = num1 * 3.5 + num2 * 7.5;
        double media = soma / 11;
        String media_5_casas = String.format("%.5f", media);
        String media_formatada = media_5_casas.replace(",", ".");
        
        System.out.printf("MEDIA = %s\n", media_formatada);
        entrada.close();
    }
}
