import unittest
from tax import calc_tax

class TestCalcTax(unittest.TestCase):

    def test_calc_tax_with_incorrect_amount_type_should_raise_error(self):
        self.assertRaises(TypeError, calc_tax, 'ten', 0.23, 20)

    def test_calc_tax_with_incorrect_tax_rate_type_should_raise_error(self):
        self.assertRaises(TypeError, calc_tax, 100, '0.23', 20)

    def test_calc_tax_with_incorrect_amount_value_should_raise_error(self):
        self.assertRaises(ValueError, calc_tax, -100, 0.23, 20)

    def test_calc_tax_with_incorrect_tax_rate_value_should_raise_error(self):
        self.assertRaises(ValueError, calc_tax, 100, 1.23, 20)
        self.assertRaises(ValueError, calc_tax, 100, 0.0, 20)

    def test_calc_tax_with_incorrect_age_type_should_raise_error(self):
        self.assertRaises(TypeError, calc_tax, 100, 0.23, '20')
        self.assertRaises(TypeError, calc_tax, 100, 0.23, 20.0)

    def test_calc_tax_with_incorrect_age_value_should_raise_error(self):
        self.assertRaises(ValueError, calc_tax, 100, 0.23, -1)

    def test_calc_tax_with_tax_rate_twenty_three_and_age_under_18_tax_value_less_then_5000(self):
        self.assertEqual(2300, calc_tax(10000, 0.23, 17))

    def test_calc_tax_with_tax_rate_twenty_three_and_age_under_18_tax_value_more_then_5000(self):
        self.assertEqual(5000, calc_tax(100000, 0.23, 17))

    def test_calc_tax_with_tax_rate_twenty_three_and_age_under_18_tax_value_equal_5000(self):
        self.assertAlmostEqual(5000, calc_tax(100000, 0.05, 17))

    def test_calc_tax_with_tax_rate_twenty_three_and_age_between_18_and_65(self):
        self.assertEqual(23000, calc_tax(100000, 0.23, 50))

    def test_calc_tax_with_tax_rate_twenty_three_and_age_over_65_tax_value_less_then_8000(self):
        self.assertEqual(2300, calc_tax(10000, 0.23, 70))

    def test_calc_tax_with_tax_rate_twenty_three_and_age_over_65_tax_value_more_then_8000(self):
        self.assertEqual(8000, calc_tax(100000, 0.23, 70))

    def test_calc_tax_with_tax_rate_twenty_three_and_age_over_65_tax_value_equal_8000(self):
        self.assertAlmostEqual(8000, calc_tax(100000, 0.08, 70))

    def test_calc_tax_with_tax_rate_twenty_three_and_age_equal_18_tax_value_less_then_5000(self):
        self.assertEqual(2300, calc_tax(10000, 0.23, 18))

    def test_calc_tax_with_tax_rate_twenty_three_and_age_equal_18_tax_value_more_then_5000(self):
        self.assertEqual(5000, calc_tax(100000, 0.23, 18))

    def test_calc_tax_with_tax_rate_twenty_three_and_age_equal_18_tax_value_equal_5000(self):
        self.assertAlmostEqual(5000, calc_tax(100000, 0.05, 18))

    def test_calc_tax_with_tax_rate_twenty_three_and_age_equal_65(self):
        self.assertAlmostEqual(23000, calc_tax(100000, 0.23, 65))
