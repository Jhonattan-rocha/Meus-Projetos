package Exer;

public class Exer {
    public static void main(String[] args) {
        Pilha pilha = new Pilha(null);
        for (int i = 0; i < 9; i++) {
            pilha.push(String.valueOf(i));
        }
        Pilha pilha2 = inverterPilha(pilha.elementos, pilha);
        imprimir(pilha2);
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
