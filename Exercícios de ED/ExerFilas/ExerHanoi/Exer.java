package ExerHanoi;

public class Exer {
    public static void main(String[] args) {
//        imprimir(inverterPilha(pilha.elementos, pilha));
//        Pilha p2 = null;
//        p2 = impares(pilha);
//        imprimir(p2);
//        Pilha p2 = excluiNegativos(pilha);
//        imprimir(p2);
        hanoi(3);
    }

    public static void hanoi(int n){
        Pilha pilha1 = new Pilha(null);
        Pilha pilha2 = new Pilha(null);
        Pilha pilha3 = new Pilha(null);
        if (n < 3 || n>7){
            throw new IllegalArgumentException("O número digitado tem que ser maior ou igual a 3 e menor ou igual a 7");
        }
        for (int i = n; i > 0; i--) {
            pilha1.push(String.valueOf(i));
            pilha2.push("|");
            pilha2.push("|");
        }
        int len = pilha1.elementos;
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i<len; i++){
            stringBuilder.append(pilha1.pop()).append(" - ").append(pilha2.pop()).append(" - ").append(pilha3.pop());
        }
    }

    public static Pilha aux(Pilha p1){
        int len = p1.elementos;
        Pilha pilha = new Pilha(null);
        for (int i = 0; i < len; i++) {
            pilha.push(p1.pop());
        }
        return p1;
    }

    public static Pilha excluiNegativos(Pilha p1){
        int len = p1.elementos;
        Pilha p2 = new Pilha(null);
        for (int i = 0; i < len; i++) {
            String elemento = p1.pop();
            if (!(Integer.parseInt(elemento) < 0)){
                p2.push(elemento);
            }
        }
        return p2;
    }

    public static Pilha impares(Pilha p1){
        int len = p1.elementos;
        Pilha p2 = new Pilha(null);
        for (int i = 0; i < len; i++) {
            int elemento = Integer.parseInt(p1.pop());
            if (elemento % 2 == 1){
                p2.push(String.valueOf(elemento));
            }
        }
        return p2;
    }
    public static Pilha pares(Pilha p1){
        int len = p1.elementos;
        Pilha p2 = new Pilha(null);
        for (int i = 0; i < len; i++) {
            int elemento = Integer.parseInt(p1.pop());
            if (elemento % 2 == 0){
                p2.push(String.valueOf(elemento));
            }
        }
        return p2;
    }
    public static Pilha inverterPilha(int len, Pilha p1){
        Pilha p2 = new Pilha(null);
        for(int i = len; i>0; i--){
            p2.push(p1.pop());
        }
        return p2;
    }
    public static void imprimir(Pilha pilha){
        int len = pilha.elementos;
        for (int i = 0; i < len; i++) {
            System.out.println(pilha.pop());
        }
    }
}
