package ExerHanoi;

public class No {
    public No anterior;
    public String dado;
    public No(No anterior, String dado) {
        this.anterior = anterior;
        this.dado = dado;
    }
}