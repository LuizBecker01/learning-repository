//Exercício de fixação - Seção 4 - Video 24

import java.util.Locale;

public class Exercice01 {
    public static void main(String[] args) {
        String pruduct1 = "Computer";
        String product2 = "Office desk";
        
        int age = 30;
        int code = 5290;
        char gender = 'F';
        
        double price1 = 2100.0;
        double price2 = 650.50;
        double measure = 53.234567;
        
        System.out.println("Products:");
        System.out.printf("%s, which price is $ %.2f%n", pruduct1, price1);
        System.out.printf("%s, which price is $ %.2f%n", product2, price2);
        System.out.println("Record: " + age + " years old, code " + code + " and gender: " + gender);
        System.out.println("Measure with eight decimal places: " + measure);
        System.out.printf("Rounded (three decimal places): %.3f%n", measure);
        Locale.setDefault(Locale.US);
        System.out.printf("US decimal point: %.4f%n", measure);
    }
}