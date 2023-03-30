package pesquisa.sequencial.java;

import java.util.Arrays;

/**
 * Main
 */
public class Main {
    public static void main(String[] args) {
        String lista[] = {"A","C","F", "B", "C"};
        System.out.println(Arrays.binarySearch(lista,"B"));
        
    }
}