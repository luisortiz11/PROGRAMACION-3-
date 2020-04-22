import unittest

from tarea_1 import validador

#Lista de nombres prohibidos
#nompro = ["x","xx", "xxx"]

class Testfunciones(unittest.TestCase):
    def test_validador(self):
        result = validador("xxx")
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
