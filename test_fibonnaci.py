import unittest
import fibonnaci

class   TestFibonnaci(unittest.TestCase):
    def test_nth(self):
        self.assertEqual(fibonnaci.sequence(1), 1)
        self.assertEqual(fibonnaci.sequence(2), 1)
        self.assertEqual(fibonnaci.sequence(3), 2)
        self.assertEqual(fibonnaci.sequence(4), 3)
        self.assertEqual(fibonnaci.sequence(5), 5)
        self.assertEqual(fibonnaci.sequence(6), 8)
        self.assertEqual(fibonnaci.sequence(7), 13)
        self.assertEqual(fibonnaci.sequence(8), 21)
        self.assertEqual(fibonnaci.sequence(9), 34)

if __name__ == '__main__':
    unittest.main()