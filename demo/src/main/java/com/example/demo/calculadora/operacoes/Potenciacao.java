/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.demo.calculadora.operacoes;

/**
 *
 * @author cleber
 */
public class Potenciacao implements Operavel {

    @Override
    public double aplicar(double a, double b) {
        return Math.pow(a, b);
    }
}
