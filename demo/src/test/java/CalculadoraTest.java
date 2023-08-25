
import com.example.demo.calculadora.Calculadora;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author cleber
 */
public class CalculadoraTest {
    
    private Calculadora calculadora;

    public CalculadoraTest() {
        this.calculadora = new Calculadora() {
            @Override
            public void saudar() {
            }
        };
    }
    
    @Test
    public void dadaUmaFrase_entaoDeveSomar() {
        double resultado = calculadora.calcular("1 mais 2");
        Assertions.assertEquals(resultado, 3);
    }
    
    @Test
    public void dadaUmaFrase_entaoDeveSubtrair() {
        double resultado = calculadora.calcular("2 menos 3");
        Assertions.assertEquals(resultado, -1);
    }
    
    @Test
    public void dadaUmaFrase_entaoDeveDividir() {
        double resultado = calculadora.calcular("4 dividido por 1");
        Assertions.assertEquals(resultado, 4);
    }
    
    @Test
    public void dadaUmaFrase_entaoDeveDividir2() {
        double resultado = calculadora.calcular("4 dividido por 0");
        Assertions.assertTrue(Double.isInfinite(resultado));
    }
    
    @Test
    public void dadaUmaFrase_entaoDeveMultiplicar() {
        double resultado = calculadora.calcular("2 vezes 4");
        Assertions.assertEquals(resultado, 8);
    }
    
    @Test
    public void dadaUmaFrase_entaoDeveMultiplicar2() {
        double resultado = calculadora.calcular("0 vezes 4");
        Assertions.assertEquals(resultado, 0);
    }
    
    @Test
    public void dadaUmaFrase_entaoDevePotenciar() {
        double resultado = calculadora.calcular("2 elevado a 4");
        Assertions.assertEquals(resultado, 16);
    }
    
    @Test
    public void dadaUmaFrase_entaoDevePotenciar2() {
        double resultado = calculadora.calcular("2 elevado a 0");
        Assertions.assertEquals(resultado, 1);
    }
    
    @Test
    public void dadaUmaFrase_entaoDeveDarErro() {
        Assertions.assertThrows(IllegalArgumentException.class, () -> {
            calculadora.calcular("2 pipoca 4");
        });
    }
}
