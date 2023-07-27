import unittest
from invert import Matrix3x3


class TestMatrix(unittest.TestCase):
    def test_determinant(self):
        with self.assertRaises(ValueError):
            Matrix3x3.find_determinant()

    def test_matrix(self):
        pass
