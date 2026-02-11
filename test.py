import unittest
from calculadora import sumar, restar, multiplicar, dividir

class TestOperaciones(unittest.TestCase):

    def test_sumar(self):
        """Prueba la función de sumar con enteros y flotantes."""
        self.assertEqual(sumar(10, 5), 15)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)
        self.assertAlmostEqual(sumar(1.5, 2.5), 4.0)

    def test_restar(self):
        """Prueba la función de restar."""
        self.assertEqual(restar(10, 5), 5)
        self.assertEqual(restar(-1, 1), -2)
        self.assertEqual(restar(-1, -1), 0)
        self.assertAlmostEqual(restar(5.5, 0.5), 5.0)

    def test_multiplicar(self):
        """Prueba la función de multiplicar."""
        self.assertEqual(multiplicar(10, 5), 50)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(3, -4), -12)
        self.assertAlmostEqual(multiplicar(1.5, 2), 3.0)

    def test_dividir(self):
        """Prueba la función de dividir."""
        self.assertEqual(dividir(10, 5), 2)
        self.assertEqual(dividir(-10, 5), -2)
        self.assertAlmostEqual(dividir(5, 2), 2.5)

    def test_dividir_por_cero(self):
        """Prueba que la división por cero lance un ValueError."""
        # Usamos assertRaises como un manejador de contexto
        # para verificar que la excepción esperada es lanzada.
        with self.assertRaises(ValueError):
            dividir(10, 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
