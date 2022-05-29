package Exemplos;

import java.util.Objects;
import java.util.Scanner;

public class Teste {
    // byte, short, int, long, String, float, Double, char, boolean
    // +, -, /, *, %, // - aritmeticos
    // && - E, || - OU, ! - Negação, !=
    // =, /=, -=, +=, *=, <=, >=
    // ==
    // ++, soma 1, --, sub 1
    // ++i, i++
    //String - qualquer coisa

    public static void main(String[] args) {
        int v, b;
        String j = "";
        Scanner i = new Scanner(System.in);

        do {
            System.out.println("Digite o primeiro valor:");
            v = i.nextInt();
            System.out.println("Digite o segundo valor:");
            b = i.nextInt();
            System.out.println("Escolha o operador desejado:");
            j = i.next();

            if (Objects.equals(j, "+")) {
                Calculo c = new Calculo(v, b);
                System.out.println(c.soma());
            }
            else if (Objects.equals(j, "-")) {
                Calculo c = new Calculo(v, b);
                System.out.println(c.sub());
            }
            else if (Objects.equals(j, "*")) {
                Calculo c = new Calculo(v, b);
                System.out.println(c.mult());
            }
            else if (Objects.equals(j, "/")) {
                Calculo c = new Calculo(v, b);
                System.out.println(c.div());
            }

        } while (!Objects.equals(j, "s"));


    }

}
