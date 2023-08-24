/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.demo.algoritmos;

/**
 *
 * @author cleber
 */
public class BubbleSort implements Ordenavel {

    @Override
    public void ordenar(int[] ar) {
        int n = ar.length;
        for (int i = 0; i < n; i++) {
            boolean jaOrdenado = true;
            for (int j = 0; j < n - i - 1; j++) {
                if (ar[j] > ar[j + 1]) {
                    int aux = ar[j];
                    ar[j] = ar[j + 1];
                    ar[j + 1] = aux;
                    jaOrdenado = false;
                }
            }
            if (jaOrdenado) {
                break;
            }
        }
    }

}
