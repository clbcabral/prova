/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.demo.oo;

/**
 *
 * @author cleber
 */
public class Gato extends Animal implements Barulhento {

    public Gato() {
        super("Gato");
    }
    
    public Gato(String nome) {
        super(nome);
    }
    
    public void ronronar() {
        System.out.println(String.format("%s ronrona.", this.getNome()));
    }

    @Override
    public void fazBarulho() {
        this.ronronar();
    }
}
