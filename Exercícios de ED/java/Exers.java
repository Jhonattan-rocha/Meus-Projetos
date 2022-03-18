import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class Exers {
	
	public static ArrayList<Long> Lista = new ArrayList<>();
	public static ArrayList<String> ListaNomes = new ArrayList<>();

	public static void main(String[] args) {
		System.out.println("Primeiro teste");
		int[] vetor = criarVetor(10);
		Comparable[] vetor2 = criarVetor2(10);
		insertionSort(vetor);
		bubblesort(vetor);
		selectionSort(vetor);
		mergeSort(vetor2);
		quickSorte(vetor);
		
		System.out.println("Tempos: ");
		System.out.println(Lista);
		System.out.println(ListaNomes);
		Lista = new ArrayList<>();
		ListaNomes = new ArrayList<>();

		System.out.println("Segundo teste");
		vetor = criarVetor(100);
		vetor2 = criarVetor2(100);
		insertionSort(vetor);
		bubblesort(vetor);
		selectionSort(vetor);
		mergeSort(vetor2);
		quickSorte(vetor);
		
		System.out.println("Tempos: ");
		System.out.println(Lista);
		System.out.println(ListaNomes);
		Lista = new ArrayList<>();
		ListaNomes = new ArrayList<>();
		
		System.out.println("Terceiro teste");
		vetor = criarVetor(1000);
		vetor2 = criarVetor2(1000);
		insertionSort(vetor);
		bubblesort(vetor);
		selectionSort(vetor);
		mergeSort(vetor2);
		quickSorte(vetor);
		
		System.out.println("Tempos: ");
		System.out.println(Lista);
		System.out.println(ListaNomes);
		Lista = new ArrayList<>();
		ListaNomes = new ArrayList<>();
		
		System.out.println("Quarto teste");
		vetor = criarVetor(10000);
		vetor2 = criarVetor2(10000);
		insertionSort(vetor);
		bubblesort(vetor);
		selectionSort(vetor);
		mergeSort(vetor2);
		quickSorte(vetor);
		
		System.out.println("Tempos: ");
		System.out.println(Lista);
		System.out.println(ListaNomes);
		Lista = new ArrayList<>();
		ListaNomes = new ArrayList<>();
		
		System.out.println("Quinto teste");
		vetor = criarVetor(500000);
		vetor2 = criarVetor2(500000);
		insertionSort(vetor);
		bubblesort(vetor);
		selectionSort(vetor);
		mergeSort(vetor2);
		quickSorte(vetor);
		
		System.out.println("Tempos: ");
		System.out.println(Lista);
		System.out.println(ListaNomes);
		Lista = new ArrayList<>();
		ListaNomes = new ArrayList<>();

		System.out.println("Sexto teste");
		vetor = criarVetor(100000);
		vetor2 = criarVetor2(100000);
		insertionSort(vetor);
		bubblesort(vetor);
		selectionSort(vetor);
		mergeSort(vetor2);
		quickSorte(vetor);
		
		System.out.println("Tempos: ");
		System.out.println(Lista);
		System.out.println(ListaNomes);
		Lista = new ArrayList<>();
		ListaNomes = new ArrayList<>();
		
		System.out.println("Setimo teste");
		vetor = criarVetor(200000);
		vetor2 = criarVetor2(200000);
		insertionSort(vetor);
		bubblesort(vetor);
		selectionSort(vetor);
		mergeSort(vetor2);
		quickSorte(vetor);
		
		System.out.println("Tempos: ");
		System.out.println(Lista);
		System.out.println(ListaNomes);
		
	}
	
	
	public static int[] criarVetor(int tamanhoVetor) {
        Random random = new Random();
        int[] vetor = new int[tamanhoVetor];
        for (int i = 0; i < tamanhoVetor; i++) {
            vetor[i] = random.nextInt(100);
        }
        return vetor;
    }
	
	public static Comparable[] criarVetor2(int tamanhoVetor) {
        Random random = new Random();
        Comparable[] vetor = new Comparable[tamanhoVetor];
        for (int i = 0; i < tamanhoVetor; i++) {
            vetor[i] = random.nextInt(100);
        }
        return vetor;
    }

	public static void insertionSort(int[] vetor) {
		int j;
		int key;
		int i;
		
		long tempoI = System.nanoTime();
		
		for (j = 1; j < vetor.length; j++) 
		{
			key = vetor[j];
			for (i = j - 1; (i >- 0) && (vetor[i] > key); i--)
			{
				vetor[i+1] = vetor[i];	
			}
			vetor[i+1] = key;
		}
		
		long tempoF = System.nanoTime();

		ListaNomes.add("InsertSort");
		Lista.add(tempoF - tempoI);
		
	}
	
	public static void bubblesort(int[] vetor) {
		boolean troca = true;
		int aux;
		long tempoI = System.nanoTime();
		while(troca) {
			troca = false;
			for(int i = 0; i < vetor.length-1; i++)
			{
				if (vetor[i] > vetor[i+1]) {
					aux = vetor[i];
					vetor[i] = vetor[i+1];
					vetor[i+1] = aux;
					troca = true;
				}
			}
		}
		long tempoF = System.nanoTime();

		ListaNomes.add("BubbleSort");
		Lista.add(tempoF - tempoI);
	}
	
	public static void selectionSort(int[] vetor) {
		long tempoI = System.nanoTime();
		for (int fixo = 0; fixo < vetor.length - 1; fixo++) {
			int menor = fixo;
			
			for (int i = menor + 1; i < vetor.length; i++) {
				if(vetor[i] < vetor[menor]) {
					menor = i;
				}
				if (menor != fixo) {
					int t = vetor[fixo];
					vetor[fixo] = vetor[menor];
					vetor[menor] = t;
				}
			}
		}
		long tempoF = System.nanoTime();

		ListaNomes.add("SelectionSort");
		Lista.add(tempoF - tempoI);
	}
	
	public static void mergeSort(Comparable[] a) {
		long tempoI = System.nanoTime();
		Comparable[] tmpArray = new Comparable[a.length];
		mergeSort(a, tmpArray, 0, a.length - 1);
		long tempoF = System.nanoTime();

		ListaNomes.add("MergeSort");
		Lista.add(tempoF - tempoI);
	}
	
	public static void mergeSort(Comparable[] a, Comparable[] tmpArray, int left, int right) {
		if (left < right) {
			int center = (left + right)/2;
			mergeSort(a, tmpArray, left, center);
			mergeSort(a, tmpArray, center+1, right);
			merge(a, tmpArray, left, center+1, right);
		}
	}
	
	public static void merge(Comparable[] a, Comparable[] tmpArray, int leftPos, int rightPos, int rightEnd) {
		int leftEnd = rightPos -1;
		int tmpPos = leftPos;
		int numElements = rightEnd - leftPos +1;
		
		while (leftPos <= leftEnd && rightPos <= rightEnd)
			if (a[leftPos].compareTo(a[rightPos]) <= 0)
				tmpArray[tmpPos++] = a[leftPos++];
			else
				tmpArray[tmpPos++] = a[rightPos++];
		
		while (leftPos <= leftEnd)
			tmpArray[tmpPos++] = a[leftPos++];
		
		while (rightPos <= rightEnd)
			tmpArray[tmpPos++] = a[rightPos++];
		
		for (int i = 0; i < numElements; i++, rightEnd --)
			a[rightEnd] = tmpArray[rightEnd];
	}
	
	public static void quickSorte(int[] vetor) {
		long tempoI = System.nanoTime();
		quickSort(vetor, 0, vetor.length-1);
		long tempoF = System.nanoTime();

		ListaNomes.add("quickSort");
		Lista.add(tempoF - tempoI);
	}
	
	public static void quickSort(int[] vetor, int inicio, int fim) {
		if(inicio < fim) {
			int posicaoPivo = separar(vetor, inicio, fim);
			quickSort(vetor, inicio, posicaoPivo - 1);
			quickSort(vetor, posicaoPivo+1, fim);
		}
	}
	
	public static int separar(int[] vetor, int inicio, int fim) {
		int pivo = vetor[inicio];
		int i = inicio+1, f = fim;
		while (i <= f) {
			if (vetor[i] <= pivo)
				i++;
			else if (pivo < vetor[f])
				f--;
			else {
				int troca = vetor[i];
				vetor[i] = vetor[f];
				vetor[f] = troca;
				i++;
				f--;
			}
		}
		vetor[inicio] = vetor[f];
		vetor[f] = pivo;
		return f;
	}
	
}
