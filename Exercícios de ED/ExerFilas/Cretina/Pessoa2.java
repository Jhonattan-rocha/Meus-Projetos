package Cretina;

public class Pessoa2 extends Pessoa{
    public String rg;

    public Pessoa2(String nome, String documento, int idade, String rg){
        super(nome, documento, idade);
        this.rg = rg;
    }
    public void mostrar(){
        super.mostrar();
        System.out.println(this.rg);
    }
}
