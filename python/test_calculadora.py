from calculadora import CalculadoraAbstrata
import unittest

class CalculadoraTestCase(unittest.TestCase):

    def test_dadaUmaFrase_entaoDeveSomar(self):
        calculadora = CalculadoraAbstrata()
        resultado = calculadora.calcular('1 mais 2')
        self.assertEqual(3, resultado)

    def test_dadaUmaFrase_entaoDeveSomar2(self):
        calculadora = CalculadoraAbstrata()
        resultado = calculadora.calcular('-2 mais 0')
        self.assertEqual(-2, resultado)

    def test_dadaUmaFrase_entaoDeveSubtrair(self):
        calculadora = CalculadoraAbstrata()
        resultado = calculadora.calcular('-2 menos -8')
        self.assertEqual(6, resultado)
    
    def test_dadaUmaFrase_entaoDeveSubtrair2(self):
        calculadora = CalculadoraAbstrata()
        resultado = calculadora.calcular('2 menos 3')
        self.assertEqual(-1, resultado)

    def test_dadaUmaFrase_entaoDeveDividir(self):
        calculadora = CalculadoraAbstrata()
        resultado = calculadora.calcular('4 dividido por 1')
        self.assertEqual(4, resultado)

    def test_dadaUmaFrase_entaoDeveMultiplicar(self):
        calculadora = CalculadoraAbstrata()
        resultado = calculadora.calcular('2 vezes 4')
        self.assertEqual(8, resultado)

    def test_dadaUmaFrase_entaoDevePotenciar(self):
        calculadora = CalculadoraAbstrata()
        resultado = calculadora.calcular('3 elevado a 2')
        self.assertEqual(9, resultado)

    def test_potencia_zero(self):
        calculadora = CalculadoraAbstrata()
        resultado = calculadora.calcular('3 elevado a 0')
        self.assertEqual(1, resultado)

    def test_divisao_zero(self):
        calculadora = CalculadoraAbstrata()
        with self.assertRaises(ZeroDivisionError):
            calculadora.calcular('3 dividido por 0')