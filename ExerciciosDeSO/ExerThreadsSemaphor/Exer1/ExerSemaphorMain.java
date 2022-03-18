package Exer1;

import java.util.concurrent.Semaphore;

public class ExerSemaphorMain {
    public static void main(String[] args) {
        Semaphore semaphore = new Semaphore(1);
        for (int i = 0; i < 21; i++) {
            Thread t = new ExerSemaphor1(i, semaphore);
            t.start();
        }
    }
}
