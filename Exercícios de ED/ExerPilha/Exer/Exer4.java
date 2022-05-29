package Exer;

public class Exer4 {
    public static void main(String[] args) {
        separarValoresEmPilhaEfila();
    }
    public static void separarValoresEmPilhaEfila(){
        Pilha pilha = new Pilha(null);
        Fila fila = new Fila();

        Fila filaPopulada = new Fila();
        for (int i = 1; i < 41; i++) {
            filaPopulada.inserir(i);
        }
        // par na pilha
        // impar na fila
        int len = filaPopulada.cont;
        for (int i = 0; i < len; i++) {
            int valor = filaPopulada.remover();
            if(valor % 2 == 0){
                pilha.push(String.valueOf(valor));
            }else{
                fila.inserir(valor);
            }
        }

        int tamnho = fila.cont;

        for (int i = 0; i < tamnho; i++) {
            System.out.println("Fila: ");
            System.out.println(fila.remover());
        }

        tamnho = pilha.elementos;
        for (int i = 0; i < tamnho; i++) {
            System.out.println("Pilha: ");
            System.out.println(pilha.pop());
        }

    }
}
