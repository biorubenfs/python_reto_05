import unittest

from Geometria_.model.Geometria import Geometria


class TestGeometria(unittest.TestCase):
    def setUp(self):
        self.geom = Geometria(1, 2, 3)

    def testInstance(self):
        self.assertIsInstance(self.geom, Geometria)

    def testCuadrado(self):
        self.assertEqual(self.geom.areaCuadrado(self.geom.b), 4)

    def testCirculo(self):
        PI = 3.1416
        self.assertEqual(self.geom.areaCirculo(self.geom.c), PI * pow(self.geom.c, 2))


if __name__ == '__main__':
    unittest.main()