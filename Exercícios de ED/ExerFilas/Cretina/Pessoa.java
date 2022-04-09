package Cretina;

public class Pessoa implements TesteInterface {
    public String nome;
    public String documento;
    public int idade;
    private String cpf;

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public Pessoa(String nome, String documento, int idade) {
        this.nome = nome;
        this.documento = documento;
        this.idade = idade;
    }

    public void mostrar(){
        System.out.println(this.nome);
        System.out.println(this.documento);
        System.out.println(this.idade);
    }

    @Override
    public String posses() {
        return null;
    }
}
