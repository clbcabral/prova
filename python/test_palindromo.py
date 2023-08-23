import unittest
from palindromo import palindromo


class CasoTestePalindromo(unittest.TestCase):

    def test_deve_identificar_palidromo(self):
        res = palindromo(palavra='arara')
        self.assertEqual('S', res)
        res = palindromo(palavra='ana')
        self.assertEqual('S', res)

    def test_nao_deve_identificar_palidromo(self):
        res = palindromo(palavra='chuveiro')
        self.assertEqual('N', res)
    
    def test_deve_marcar_como_invalido(self):
        res = palindromo(palavra='pé')
        self.assertEqual('?', res)
    
    def test_deve_marcar_como_invalido2(self):
        res = palindromo(palavra='')
        self.assertEqual('?', res)