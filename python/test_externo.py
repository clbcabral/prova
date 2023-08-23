from unittest.mock import Mock, patch
import unittest
from externo import Chamador


class CasoTesteConsultaExterna(unittest.TestCase):

    def test_consulta_externa_comum(self):
        chamador = Chamador()
        res = chamador.faz_chamada_externa()
        self.assertTrue(res is not None)

    def test_consulta_externa_mockada(self):
        chamador = Chamador()
        mock = Mock(chamador.faz_chamada_externa)
        mock.return_value = 'okok'
        self.assertEqual(mock(), 'okok')

    @patch('externo.Chamador.faz_chamada_externa')
    def test_consulta_externa_mockada2(self, chamador):
        chamador.return_value = 'abc'
        print(chamador())