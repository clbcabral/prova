/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.demo.calculadora;

import java.util.Scanner;

/**
 *
 * @author cleber
 */
public class CalculadoraConsole extends Calculadora {

    public void saudar() {
        System.out.println("Bem-vindo à calculadora console!");
        System.out.println("");
        System.out.println("2 mais 2");
        System.out.println("2 menos 4");
        System.out.println("3 vezes 2");
        System.out.println("6 dividido por 2");
        System.out.println("4 elevado a 2");
        System.out.println("");
        
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            System.out.println("Escreva o seu cálculo com algum dos formatos acima:");
            String frase = scanner.nextLine();
            double resultado = this.calcular(frase);
            System.out.println(resultado);
        }
    }
    
    public static void main(String[] args) {
        CalculadoraConsole calculadora = new CalculadoraConsole();
        calculadora.saudar();
    }
}
