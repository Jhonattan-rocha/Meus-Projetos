package Exer2;

import java.util.concurrent.Semaphore;

public class ExerSemaphorMain {
    public static void main(String[] args) {
        Semaphore semaphore = new Semaphore(1);
        for (int i = 0; i < 5; i++) {
            Thread t = new ExerSemaphor2(i, semaphore);
            t.start();
        }
    }
}
