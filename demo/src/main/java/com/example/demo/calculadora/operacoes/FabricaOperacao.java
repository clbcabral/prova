/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.demo.calculadora.operacoes;

import com.example.demo.calculadora.operacoes.Adicao;
import com.example.demo.calculadora.operacoes.Divisao;
import com.example.demo.calculadora.operacoes.Multiplicacao;
import com.example.demo.calculadora.operacoes.Operavel;
import com.example.demo.calculadora.operacoes.Potenciacao;
import com.example.demo.calculadora.operacoes.Subtracao;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

/**
 *
 * @author cleber
 */
public class FabricaOperacao {

    private static final Map<String, Operavel> OPERACOES = new HashMap<>();

    static {
        OPERACOES.put("mais", new Adicao());
        OPERACOES.put("menos", new Subtracao());
        OPERACOES.put("dividido por", new Divisao());
        OPERACOES.put("vezes", new Multiplicacao());
        OPERACOES.put("elevado a", new Potenciacao());
    }

    private FabricaOperacao() {
    }

    public static Optional<Operavel> getOperacao(String operacao) {
        return Optional.ofNullable(OPERACOES.get(operacao));
    }
}
