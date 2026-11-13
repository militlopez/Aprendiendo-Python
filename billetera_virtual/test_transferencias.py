import unittest
from transferencias import(
    transferir,
    MONTO_INVALIDO,
    SALDO_INSUFICIENTE,
    LIMITE_DIARIO,
    LIMITE_EXCEDIDO,
    APROBADA)

class TestTransferir(unittest.TestCase):
    # HU001
    def test_aprobada_por_envio_normal(self):
        self.assertEqual(transferir(50000,40000,100000),APROBADA)
    def test_monto_cero(self):
        self.assertEqual(transferir(50000,0,100000),MONTO_INVALIDO)
    def test_limite_excedido(self):
        self.assertEqual(transferir(),LIMITE_EXCEDIDO)
if __name__=="__main__":
    unittest.main()