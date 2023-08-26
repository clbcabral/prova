/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.demo.oo;

/**
 *
 * @author cleber
 */
public class Cachorro extends Animal implements Barulhento {

    public Cachorro() {
        super("Cachorro");
    }
    
    public Cachorro(String nome) {
        super(nome);
    }
    
    public void latir() {
        System.out.println(String.format("%s late.", this.getNome()));
    }

    @Override
    public void fazBarulho() {
        this.latir();
    }
    
}
