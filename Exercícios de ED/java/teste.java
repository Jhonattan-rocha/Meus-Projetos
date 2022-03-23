import controller.Criar_Vetor;
import controller.Exercicio_01;

public class teste {
    public void mergesort(Comparable[] a) {
        Comparable[] tmparray = new Comparable[a.length];
        mergesort(a, tmparray, 0, a.length - 1);
    }



    private static void mergesort(Comparable[] a, Comparable[] tmparray, int left, int right) {
        if (left < right) {
            int center = (left + right) / 2;
            mergesort(a, tmparray, left, center);
            mergesort(a, tmparray, center + 1, right);
            merge(a, tmparray, left, center + 1, right);
        }
    }

    private static void merge(Comparable[] a, Comparable[] tmpArray, int leftPos, int rightPos, int rightEnd) {
        int leftEnd = rightPos - 1;
        int tmpPos = leftPos;
        int numElements = rightEnd - leftPos + 1;
        while (leftPos <= leftEnd && rightPos <= rightEnd)



            if (a[leftPos].compareTo(a[rightPos]) <=0)
                tmpArray[tmpPos++] = a [leftPos++];



            else
                tmpArray [tmpPos++] = a[rightPos++];



        while (leftPos <= leftEnd)
            tmpArray[tmpPos++] = a[leftPos++];



        while (rightPos <= rightEnd)
            tmpArray [tmpPos++] = a[rightPos++];



        for (int i = 0; i < numElements; i++, rightEnd--)
            a [rightEnd] = tmpArray[rightEnd];



    }



    public class Principal_Exercicio_06_ED {

        public static void main(String[] args) {

            Criar_Vetor Vetor = new Criar_Vetor();
            int vet1[] = Vetor.criarVetor(10);
            int vet2[] = Vetor.criarVetor(10);
            int vet3[] = Vetor.criarVetor(10);
            int vet4[] = Vetor.criarVetor(10);
            int vet5[] = Vetor.criarVetor(10);

            controller.Exercicio_01 Controller = new controller.Exercicio_01();

            Controller.insertionSort(vet1);
            Controller.bubbleSort(vet2);
            Controller.selectionsort(vet3);
            Controller.quickSort(vet4);
            Controller.mergesort(vet5);

        }

    }
}
