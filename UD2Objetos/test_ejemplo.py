import unittest
from UD2Objetos.cuenta_corriente import CuentaCorriente

class TestCuentaCorriente(unittest.TestCase):

    def test_constructor(self):
        c = CuentaCorriente(123, "Juan", 1000)
        self.assertEqual(c.saldo, 1000)

    def test_setter_saldo(self):
        c = CuentaCorriente(123, "Juan")
        c.saldo = 3000
        self.assertEqual(c.saldo, 3000)

    def test_suma_cuentas(self):
        c1 = CuentaCorriente(1, "A", 100)
        c2 = CuentaCorriente(2, "B", 20)

        c1 = c1 + c2
        self.assertEqual(c1.saldo, 300)
        self.assertIn("B", c1._CuentaCorriente__titular)

    def test_numero_de_cuentas(self):
        inicio = CuentaCorriente.getNumCuenta()
        CuentaCorriente(99, "Z")
        final = CuentaCorriente.getNumCuenta()
        self.assertEqual(final, inicio + 1)

if __name__ == '__main__':
    unittest.main()
