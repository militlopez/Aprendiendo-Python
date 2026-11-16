import unittest
from fizzbuzz import fizzbuzz

# el nombre de la clase empieza con mayus
class TestFizzbuzz(unittest.TestCase):
# def dentro del class se llama "metodo"
    def test_multiplo_3(self):
# segun el criterio de aceptación debe devolver fizz
        self.assertEqual(fizzbuzz(9),"fizz")
    def test_multiplo_5(self):
        self.assertEqual(fizzbuzz(20),"buzz")
    def test_multiplo_3_and_multiplo_5(self):
        self.assertEqual(fizzbuzz(15),"fizzbuzz")
    def test_no_multiplo(self):
        self.assertEqual(fizzbuzz(98),98)
    def test_0(self):
        self.assertEqual(fizzbuzz(0),"fizzbuzz")
    def test_multiplo_negativo(self):
        self.assertEqual(fizzbuzz(-15),"fizzbuzz")

if __name__=='__main__':
    unittest.main()