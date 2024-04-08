import unittest
import parameterized
from unittest.mock import Mock, MagicMock


def sum(a, b):
    if a is None or b is None:
        return None
    if not isinstance(a, int):
        raise ValueError("a is not a number")
    if not isinstance(b, int):
        raise ValueError("b is not a number")
    return a + b


# x = {"name": "Martins"}
# y = {"name": "Martins"}
# print(x is y)
# print(x == y)


class MyTestCases(unittest.TestCase):
    """creating a test case class where all tests (function) are going"""

    def setUp(self) -> None:
        # runs before each test methods
        self.result = 1 + 2

    def tearDown(self) -> None:
        # runs after each test methods
        self.result = None
        print("\nNew Test.....\n")

    def test_one(self):
        self.assertEqual(self.result, 3, "3 === 3")
        # self.assertEquals(self.result, 3, "it should also pass") deprecated
        self.assertNotEqual(self.result, 4, "3 !== 4")
        #
        self.assertFalse(self.result == 2, "3 !== 2")
        self.assertTrue(self.result == 3, "3 === 3")
        #
        self.assertRaises(ValueError, sum, 2, "2")
        #
        self.assertIs(self.result, 3, "self.result is 3")
        self.assertIsNot(self.result, 4, "self.result is not 4")
        #
        self.assertIsNone(None, "it should be None")
        self.assertIsNotNone(self.result, "it is not None")
        #
        self.assertIn(3, [1, 2, 3], "3 is in the list")
        self.assertNotIn(4, [1, 2, 3], "4 is not in the list")
        #
        self.assertIsInstance(4, int, "4 is an instance of int")
        self.assertNotIsInstance("Martins", int, "Martins in not an int instance")

    @unittest.skip("I don't have an idea of what to test now")
    def test_nonsense(self):
        pass

    @parameterized.parameterized.expand([(1, 2, 6), (2, 4, 9)])
    def test_parameterized(self, a, b, expectation) -> None:
        sum = self.result + a + b
        self.assertEqual(sum, expectation)


if __name__ == "__main__":
    unittest.main(verbosity=True)
