import unittest

from BMI500HW4.cluster import Cluster


class TestSimple(unittest.TestCase):

    def test_instance_init(self):
        a = Cluster()
        self.assertTrue(a)


if __name__ == '__main__':
    unittest.main()