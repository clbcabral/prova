
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
    
    @Test
    public void dadaUmaFrase_entaoDeveSomar() {
        Calculadora calculadora = new Calculadora();
        double resultado = calculadora.calcular("1 mais 2");
        Assertions.assertEquals(resultado, 3);
    }
    
    @Test
    public void dadaUmaFrase_entaoDeveSubtrair() {
        Calculadora calculadora = new Calculadora();
        double resultado = calculadora.calcular("2 menos 3");
        Assertions.assertEquals(resultado, -1);
    }
    
    @Test
    public void dadaUmaFrase_entaoDeveDividir() {
        Calculadora calculadora = new Calculadora();
        double resultado = calculadora.calcular("4 dividido por 1");
        Assertions.assertEquals(resultado, 4);
    }
    
    @Test
    public void dadaUmaFrase_entaoDeveDividir2() {
        Calculadora calculadora = new Calculadora();
        double resultado = calculadora.calcular("4 dividido por 0");
        Assertions.assertTrue(Double.isInfinite(resultado));
    }
    
    @Test
    public void dadaUmaFrase_entaoDeveMultiplicar() {
        Calculadora calculadora = new Calculadora();
        double resultado = calculadora.calcular("2 vezes 4");
        Assertions.assertEquals(resultado, 8);
    }
    
    @Test
    public void dadaUmaFrase_entaoDeveDarErro() {
        Calculadora calculadora = new Calculadora();
        Assertions.assertThrows(IllegalArgumentException.class, () -> {
            calculadora.calcular("2 pipoca 4");
        });
    }
}
