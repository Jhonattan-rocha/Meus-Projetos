package Exemplos;

public class Calculo {
    public int numero;
    public int numero2;

//    public int getNumero() {
//        return numero;
//    }
//
//    public void setNumero(int numero) {
//        this.numero = numero;
//    }
//
//    public int getNumero2() {
//        return numero2;
//    }
//
//    public void setNumero2(int numero2) {
//        this.numero2 = numero2;
//    }

    public Calculo(int n, int n2) {
        this.numero = n;
        this.numero2 = n2;
    }

    public int soma() {
        return numero + numero2;
    }

    public float div() {
        return (float) numero / numero2;
    }

    public int sub() {
        return numero - numero2;
    }

    public int mult() {
        return numero * numero2;
    }
}
