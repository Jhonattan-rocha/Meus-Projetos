public class Fila {
    public int cont = 0;
    public Node primeiro = null;
    public Node ultimo = null;

    public void inserir(int novoDado){
        Node novo_nodo = new Node(novoDado, null);
        if (primeiro == null){
            primeiro = novo_nodo;
        }
        if (ultimo == null){
            ultimo = novo_nodo;
        }else {
            ultimo.proximo = novo_nodo;
            ultimo = novo_nodo;
        }
        cont++;
    }

    public int remover() {
        assert primeiro != null;
        String primeiroRetorno;
        try {
            primeiroRetorno = String.valueOf(primeiro.dado);
            primeiro = primeiro.proximo;
            if (primeiro == null) {
                ultimo = null;
            }
            cont++;
        } catch (Exception e) {
            return 0;
        }
        cont--;
        return Integer.parseInt(primeiroRetorno);
    }

}
