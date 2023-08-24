/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.demo.algoritmos;

import com.example.demo.calculadora.Calculadora;
import java.util.Arrays;

/**
 *
 * @author cleber
 */
public class Executor {

    public static void main(String[] args) {

        int[] ar = new int[]{3, 5, 1, 2, 9, 0, 4, 7};

        Ordenavel alg;
        alg = new BubbleSort();
        alg = new SelectionSort();

        alg.ordenar(ar);

        System.out.println(Arrays.toString(ar));
    }
}
