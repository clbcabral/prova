/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.demo.algoritmos;

/**
 *
 * @author cleber
 */
public class SelectionSort implements Ordenavel {

    @Override
    public void ordenar(int[] ar) {
        int n = ar.length;
        for (int i = 0; i < n - 1; i++) {
            int min = i;
            for (int j = i + 1; j < n; j++) {
                if (ar[j] < ar[min]) {
                    min = j;
                }
            }
            int aux = ar[min];
            ar[min] = ar[i];
            ar[i] = aux;
        }
    }
    
}
