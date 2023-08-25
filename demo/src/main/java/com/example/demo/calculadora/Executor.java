/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.demo.calculadora;

/**
 *
 * @author cleber
 */
public class Executor {

    public static void main(String[] args) {
//        Calculadora calculadora = new CalculadoraConsole();
//        calculadora.saudar();
//        Calculadora calculadora = new CalculadoraArquivo("/tmp/foo.txt",
//                true);
//        calculadora.saudar();
        String banco = "/tmp/banco.db";
        Calculadora calculadora = new CalculadoraBD(banco);
        calculadora.saudar();
    }

}
