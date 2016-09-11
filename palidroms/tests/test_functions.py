
import unittest

from palidroms.functions import *

class MyTest(unittest.TestCase):

    def test_checkPalindrom(self):
        self.assertEqual(checkPalindrom(255,16),True)
        self.assertEqual(checkPalindrom(3,2),True)
        self.assertEqual(checkPalindrom(0,2),True)
        self.assertEqual(checkPalindrom(1,2),True)
        self.assertEqual(checkPalindrom(8,2),False)
        self.assertEqual(checkPalindrom(8,3),True)
        self.assertEqual(checkPalindrom(0,2),True)

    def test_processPalidromCheck(self):
        self.assertEqual(
            processPalidromCheck(1,10),
            [[1, 2], [2, 3], [3, 2], [4, 3], [5, 2], [6, 5], [7, 2], [8, 3], [9, 2]])
        self.assertEqual(
            processPalidromCheck(19,20),
            [[19, 18]])


if __name__ == '__main__':
    unittest.main()
