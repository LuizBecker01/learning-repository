import java.util.Locale;

public class Main {
    public static void main(String[] args) {
        
        System.out.println("Hello World!");
        System.out.println("Good Day!");

        //variaveis
        double x = 10.35784;
        String nome = "Maria";
        int idade = 31;
        double renda = 4000.0;
        System.out.println(x);
        System.out.printf("%.2f%n", x);
        System.out.printf("%.4f%n", x);
        Locale.setDefault(Locale.US); // Padrao americano, troca a virgula pelo ponto
        System.out.printf("%.4f%n", x);
        System.out.println("RESULTADO = " + x + " METROS");
        System.out.printf("RESULTADO = %.2f METROS%n", x);

        System.out.printf("%s tem %d anos e ganha R$ %.2f reais%n", nome, idade, renda);
    }
}