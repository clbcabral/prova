/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.demo.calculadora;

import java.io.BufferedWriter;
import java.io.FileWriter;

/**
 *
 * @author cleber
 */
public class CalculadoraArquivo extends CalculadoraConsole {

    private String caminhoArquivo;
    private boolean acrescentarConteudo;

    public CalculadoraArquivo(String caminhoArquivo, boolean acrescentarConteudo) {
        this.caminhoArquivo = caminhoArquivo;
        this.acrescentarConteudo = acrescentarConteudo;
    }
    
    @Override
    public double calcular(String frase) {
        double resultado = super.calcular(frase);
        try {
            FileWriter escritor = new FileWriter(this.caminhoArquivo, 
                    this.acrescentarConteudo);
            BufferedWriter buffer = new BufferedWriter(escritor);
            buffer.write(frase);
            buffer.newLine();
            buffer.write(String.valueOf(resultado));
            buffer.newLine();
            buffer.close();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        return resultado;
    }
    
}
