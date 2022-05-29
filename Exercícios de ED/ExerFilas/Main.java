public class Main{
    public static void main(String[] args) {
        Fila fila1 = new Fila();
//        Fila fila2 = new Fila();
//        Fila fila3 = new Fila();
        int n = 4;
        for (int i = 1; i <= 4; i++) {
            fila1.inserir(i);
//            fila3.inserir(i);
        }
//        separar(fila1, fila2, n);
        System.out.println(fila1.primeiro.dado);
        System.out.println(fila1.primeiro.proximo.dado);
        System.out.println(fila1.primeiro.proximo.proximo.dado);
        System.out.println(fila1.primeiro.proximo.proximo.proximo.dado);
        System.out.println(fila1.ultimo.dado);
//        System.out.println("Valores da Primeira Fila");
//        for (int i = 0; i < fila3.cont; i++) {
//            System.out.println(fila3.remover());
//        }
//        System.out.println("Valores da Segunda Fila");
//        for (int i = 0; i < fila2.cont; i++) {
//            System.out.println(fila2.remover());
//        }

    }

    public static void separar(Fila f1, Fila f2, int n){
        for (int i = 0; i < f1.cont; i++) {
            try {
                int stop = f1.remover();
                if (stop == n){
                    for (int j = 0; j < f1.cont; j++) {
                        int s = f1.remover();
                        if (s!=0)
                            f2.inserir(s);
                    }
                    return;
                }
            }catch (Exception e){
                break;
            }
        }
    }
}
