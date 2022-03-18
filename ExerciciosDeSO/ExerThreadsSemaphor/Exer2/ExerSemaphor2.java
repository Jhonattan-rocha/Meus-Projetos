package Exer2;

import java.util.Random;
import java.util.concurrent.Semaphore;

public class ExerSemaphor2 extends Thread{

    public int id;

    Semaphore semaphore;

    public ExerSemaphor2(int Id, Semaphore semaphore){
        this.semaphore = semaphore;
        this.id = Id;
    }

    public void cozimento(int Id){
        Random r = new Random();
        int tempo = 0;
        if (Id % 2 == 0){
            System.out.println("Sopa de Cebola "+id+" cozinhando");
            System.out.println("");
            tempo = r.nextInt((1200 - 600) + 1) + 600;
            try {
                sleep(tempo);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            float por = tempo/100f;
            for (float p = 0; p < por; p+=por){
                try {
                    System.out.println("Sopa de Cebola "+id+" " + p + "% concluido");
                    sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            System.out.println("Sopa de Cebola "+id+" concluido");
            try {
                semaphore.acquire();
                try {
                    sleep(500);
                    System.out.println("Sopa de Cebola "+id+" entregue");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                semaphore.release();
            }

        }else {
            System.out.println("Lasanha a Bolonhesa "+id+" cozinhando");
            tempo = r.nextInt((800 - 500) + 1) + 500;
            try {
                sleep(tempo);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            float por = tempo/100f;
            for (float p = 0; p <= 100; p+=por){
                try {
                    System.out.println("Lasanha a Bolonhesa "+id+" " + p + "% concluido");
                    sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            System.out.println("Lasanha a Bolonhesa "+id+" concluido");
            try {
                semaphore.acquire();
                try {
                    sleep(500);
                    System.out.println("Lasanha a Bolonhesa "+id+" entregue");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                semaphore.release();
            }
        }
    }

    @Override
    public void run() {
        cozimento(id);
    }
}
