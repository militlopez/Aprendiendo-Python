import unittest 

from descuentos import descuento_producto

class DescuentoTest(unittest.TestCase):
    def test_diez_porciento(self):
        self.assertEqual(descuento_producto(20000,10),18000)
    def test_cienmil(self):
        self.assertEqual(descuento_producto(100000,10),90000)
    def test_cliente(self):
        self.assertEqual(descuento_producto(100000,10),85000)

# para que los tests solo se ejecuten cuando corres el archivo directamente:
if __name__=='__main__':
    unittest.main()