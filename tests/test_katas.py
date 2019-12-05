import unittest
import katas
import random
import math


class TestKatas(unittest.TestCase):
    def test_add(self):
        # self.fail("TODO: Write add unit test")
        self.assertIsNotNone(katas.add)
        for _ in range(10):
            x = random.randrange(-100, 100)
            y = random.randrange(-100, 100)
            self.assertEqual(katas.add(x, y), x + y)

    def test_multiply(self):
        # self.fail("TODO: Write multiply unit test")
        self.assertIsNotNone(katas.multiply)
        for _ in range(10):
            x = random.randrange(-100, 100)
            y = random.randrange(-100, 100)
            self.assertEqual(katas.multiply(x, y), x * y)

    def test_power(self):
        # self.fail("TODO: Write power unit test")
        self.assertIsNotNone(katas.power)
        for _ in range(10):
            x = random.randrange(-10, 10)
            n = random.randrange(0, 10)
            self.assertEqual(katas.power(x, n), x ** n)

    def test_factorial(self):
        # self.fail("TODO: Write factorial unit test")
        self.assertIsNotNone(katas.factorial)
        for x in range(10):
            self.assertEqual(katas.factorial(x), math.factorial(x))

    def test_fibonacci(self):
        # self.fail("TODO: Write fibonacci unit test")
        self.assertIsNotNone(katas.fibonacci)
        fibs = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
        for x in range(1, 11):
            self.assertEqual(katas.fibonacci(x), fibs[x-1])


if __name__ == '__main__':
    unittest.main()
