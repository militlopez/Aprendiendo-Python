import unittest
from funciones import par_impar

# el nombre de la clase empieza con mayus
class TestParImpar(unittest.TestCase):
# cada método de test prueba un caso distinto
    def test_cero(self):
        self.assertEqual(par_impar(0),"cero")
    def test_par(self):
        self.assertEqual(par_impar(4),"par")
    def test_impar(self):
        self.assertEqual(par_impar(7),"impar")
    def test_par_negativo(self):
        self.assertEqual(par_impar(-4),"par")
    def test_impar_negativo(self):
        self.assertEqual(par_impar(-7),"impar")

if __name__=='__main__':
    unittest.main()