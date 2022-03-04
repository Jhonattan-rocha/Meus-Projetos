import java.util.Arrays;
import java.util.Objects;

public class ExerciciosDeRecursividade {
    public static void main(String[] args) {
        System.out.println(palindromo(("Amor a Roma".toLowerCase()).split("")));
        System.out.println(palindromo(("Amor".toLowerCase()).split("")));
        System.out.println(Arrays.toString(menorValor(new int[]{5, 4, 1, 3, 2})));
        System.out.println(somaIntervalo(0, 6));
        System.out.println(multi_soma(10, 10));
    }
    public static int[] menorValor(int[] vetor) {
        int aux;
        if (vetor.length == 2){
            if (vetor[0] < vetor[1]){
                return new int[]{vetor[0]};
            }else {
                return new int[]{vetor[1]};
            }
        } else {
            int[] vetor2 = new int[vetor.length - 1];
            if (vetor[vetor.length - 2] < vetor[vetor.length - 1]) {
                System.arraycopy(vetor, 0, vetor2, 0, vetor.length - 1);
            } else {
                aux = vetor[vetor.length-2];
                vetor[vetor.length-2] = vetor[vetor.length-1];
                vetor[vetor.length-1] = aux;
                System.arraycopy(vetor, 0, vetor2, 0, vetor.length - 1);
            }
            return menorValor(vetor2);
        }
    }
    public static Boolean palindromo(String[] letras){
        if (letras.length == 2){
            return Objects.equals(letras[0], letras[1]);
        } else if (letras.length == 1){
            return true;
        }
        else {
            String[] letras2 = new String[letras.length - 2];
            if (Objects.equals(letras[0], letras[letras.length - 1])) {
                System.arraycopy(letras, 1, letras2, 0, letras.length - 2);
            } else {
                return false;
            }
            return palindromo(letras2);
        }
    }
    public static int somaIntervalo(int num, int num2){
        if (num2 < num){
            if (num > num2)
                return num - num2;
            return num2 - num;
        } else {
            num2 -= 1;
            return somaIntervalo(num, num2)+num2;
        }
    }
    public static int multi_soma(int n, int n2){
        if (n2 == 0){
            return 0;
        } else {
            n2 -= 1;
            return multi_soma(n, n2) + n;
        }
    }
}
