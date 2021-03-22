import unittest

import PAYE

class TestCalculator(unittest.TestCase):
    def test_lessThan14000(self):
        tax = PAYE.lessThan14000(0)
        self.assertEqual(0, tax)
        tax = PAYE.lessThan14000(1)
        self.assertEqual(0.105, tax)
        tax = PAYE.lessThan14000(14000)
        self.assertEqual(1470, tax)
        tax = PAYE.lessThan14000(14001)
        self.assertIsNone(None, tax)

    def test_lessThan48000(self):
        tax = PAYE.lessThan48000(14000)
        self.assertIsNone(None, tax)
        tax = PAYE.lessThan48000(14001)
        self.assertEqual(1470.175, tax)
        tax = PAYE.lessThan48000(48000)
        self.assertEqual(7420, tax)
        tax = PAYE.lessThan48000(48001)
        self.assertIs(None, tax)

    def test_lessThan70000(self):
        tax = PAYE.lessThan70000(48000)
        self.assertIsNone(None, tax)
        tax = PAYE.lessThan70000(48001)
        self.assertEqual(7420.3, tax)
        tax = PAYE.lessThan70000(70000)
        self.assertEqual(14020, tax)
        tax = PAYE.lessThan70000(70001)
        self.assertIs(None, tax)

    def test_lessThan180000(self):
        tax = PAYE.lessThan180000(70000)
        self.assertIsNone(None, tax)
        tax = PAYE.lessThan180000(70001)
        self.assertEqual(14020.33, tax)
        tax = PAYE.lessThan180000(180000)
        self.assertEqual(50320, tax)
        tax = PAYE.lessThan180000(180001)
        self.assertIs(None, tax)

    def test_over180000(self):
        tax = PAYE.overThan180000(180000)
        self.assertIsNone(None, tax)
        tax = PAYE.overThan180000(180001)
        self.assertEqual(50320.39, tax)

if __name__ == '__main__':
    unittest.main()