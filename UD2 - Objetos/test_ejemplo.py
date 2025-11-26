import unittest
from unittest import TestCase
from ejemplo import CuentaCorriente

class xTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_crearcion_y_atributos(self):
        c = CuentaCorriente(123,"Juan",1000)
        self.assertEqual(c.saldo,1000)
    def test_funcion_sobre_cargada(self):
        self.fail()

    def test_cuenta_corriente(self):
        self.fail()

    def test_alumno(self):
        self.fail()
