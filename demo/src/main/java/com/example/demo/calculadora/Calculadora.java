/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.demo.calculadora;

import com.example.demo.calculadora.operacoes.FabricaOperacao;
import com.example.demo.calculadora.operacoes.Operavel;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 *
 * @author cleber
 */
public abstract class Calculadora {

    private static final String PADRAO
            = "(-?\\d+)\\s*(mais|menos|vezes|dividido\\s*por|elevado\\s*a)\\s*(-?\\d+)";

    public abstract void saudar();
    
    public double calcular(String frase) {
        Pattern padrao = Pattern.compile(PADRAO);
        Matcher resultado = padrao.matcher(frase);
        if (resultado.find()) {
            double a = Double.valueOf(resultado.group(1));
            String operador = resultado.group(2);
            double b = Double.valueOf(resultado.group(3));
            Operavel operacao = FabricaOperacao
                    .getOperacao(operador)
                    .orElseThrow(() -> new IllegalArgumentException("Operação inválida."));
            return operacao.aplicar(a, b);
        }
        throw new IllegalArgumentException("Operação inválida.");
    }
}
