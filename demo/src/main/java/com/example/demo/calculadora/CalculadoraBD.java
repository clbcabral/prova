/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.demo.calculadora;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

/**
 *
 * @author cleber
 */
public class CalculadoraBD extends CalculadoraConsole {

    private String arquivoBanco;

    public CalculadoraBD(String arquivoBanco) {
        this.arquivoBanco = arquivoBanco;
    }

    private Connection abrirConexao() throws SQLException  {
        String url = String.format("jdbc:sqlite:%s", this.arquivoBanco);
        return DriverManager.getConnection(url);
    }
    
    private void persistirResultado(String frase, double resultado) {
        String sql = """
                   INSERT INTO calculadora 
                     (frase, resultado) 
                   VALUES 
                     (?, ?)
                   """;
        try (Connection conexao = this.abrirConexao();
             PreparedStatement ps = conexao.prepareStatement(sql);
                ) {
            ps.setString(1, frase);
            ps.setDouble(2, resultado);
            ps.executeUpdate();
        } catch (Exception e) {
            System.err.println("Erro ao perssistir dados:");
            e.printStackTrace();
        }
    }

    @Override
    public double calcular(String frase) {
        double resultado = super.calcular(frase);
        this.persistirResultado(frase, resultado);
        return resultado;
    }

}
