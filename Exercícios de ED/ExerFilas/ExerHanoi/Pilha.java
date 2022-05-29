package ExerHanoi;

public class Pilha {
    public No topo;
    public int elementos;

    public Pilha(No topo) {
        this.topo = topo;
    }

    public void push(String valor){
        No novo_no = new No(null, valor);
        if (this.topo == null){
            this.topo = novo_no;
        }else{
            novo_no.anterior = this.topo;
            this.topo = novo_no;
        }
        elementos++;
    }

    public String pop(){
        No valor = this.topo;
        this.topo = this.topo.anterior;
        elementos--;
        return valor.dado;
    }
}
