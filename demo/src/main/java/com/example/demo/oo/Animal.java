/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.demo.oo;

/**
 * 
 * @author cleber
 */
public abstract class Animal {

    private String nome;
    
    public Animal(String nome) {
        this.nome = nome;
    }
    
    public void comer() {
        System.out.println(String.format("%s come.", this.nome));
    }
    
    public void dormir() {
        System.out.println(String.format("%s dorme.", this.nome));
    }

    public String getNome() {
        return nome;
    }
}
