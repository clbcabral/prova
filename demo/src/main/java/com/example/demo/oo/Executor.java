/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.demo.oo;

/**
 *
 * @author cleber
 */
public class Executor {
    
    public static void main(String[] args) {
        
        Cachorro c = new Cachorro();
        c.latir();
        c.comer();
        
        Cachorro toto = new Cachorro("Totó");
        toto.latir();
        
        Gato g = new Gato();
        g.ronronar();
        
        Gato floquinho = new Gato("Floquinho");
        floquinho.ronronar();
        
        Barulhento b1 = new Cachorro();
        b1.fazBarulho();
        
        Barulhento b2 = new Gato();
        b2.fazBarulho();
        
        Gato gt = (Gato) b2;
        gt.ronronar();
    }
}
