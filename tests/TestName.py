import unittest

from Geometria_.model.Geometria import Geometria


class TestName(unittest.TestCase):
    def testTest(self):
        self.assertEqual(True, True)

    def setUp(self):
        self.geom = Geometria(1, 1, 1)

    def testName(self):
        self.assertEqual(self.geom.figuraName, "")
        self.geom.set_figuraName(4)
        self.assertEqual(self.geom.figuraName, "Rectangulo")

if __name__ == '__main__':
    unittest.main()