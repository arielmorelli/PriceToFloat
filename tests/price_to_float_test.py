import unittest
from resources.PriceToFloat import price_to_float


class PriceToFloatTest(unittest.TestCase):
    def test_only_number(self):
        test_value = str('111')
        expected = 111.00
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_one_dot(self):
        test_value = str('111.')
        expected = 111.00
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_one_comma(self):
        test_value = str('111,')
        expected = 111.00
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_one_dot_one_number(self):
        test_value = str('111.2')
        expected = 111.20
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_one_comma_one_number(self):
        test_value = str('111,2')
        expected = 111.20
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_one_dot_two_numbers(self):
        test_value = str('111.23')
        expected = 111.23
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_one_comma_two_numbers(self):
        test_value = str('111,23')
        expected = 111.23
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_one_dot_three_numbers_simple(self):
        test_value = str('111.234')
        expected = 111.234
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_one_comma_three_numbers_simple(self):
        test_value = str('111,234')
        expected = 111.234
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_one_dot_many_numbers_simple(self):
        test_value = str('111.234567')
        expected = 111.234567
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_one_comma_many_numbers_simple(self):
        test_value = str('111,234567')
        expected = 111.234567
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_two_dots(self):
        test_value = str('1.111.')
        expected = 1111.00
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_two_commas(self):
        test_value = str('1,111,')
        expected = 1111.00
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_many_dots(self):
        test_value = str('1.111.111.111.')
        expected = 1111111111.00
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_many_commas(self):
        test_value = str('1,111,111,111,')
        expected = 1111111111.00
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_many_dots_one_coma(self):
        test_value = str('1.111.111.111,')
        expected = 1111111111.00
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_many_commas_one_dot(self):
        test_value = str('1,111,111,111.')
        expected = 1111111111.00
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_many_dots_one_coma_three_number(self):
        test_value = str('1.111.111.111,234')
        expected = 1111111111.234
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_many_commas_one_dot_three_number(self):
        test_value = str('1,111,111,111.234')
        expected = 1111111111.234
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_bad_formated_number_many_dots(self):
        test_value = str('1.11.1.111')
        expected = 1111111.00
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

    def test_bad_formated_number_many_commas(self):
        test_value = str('1,11,1,111')
        expected = 1111111.00
        number = price_to_float(test_value)
        self.assertEqual(expected, number)

        # Expect error
    def test_bad_formated_many_dots_many_commas(self):
        test_value = str('1.11.1.111,234,5')
        self.assertRaises(ValueError, price_to_float, test_value)

    def test_bad_formated_many_commas_many_dots(self):
        test_value = str('1,11,1,111.777.')
        self.assertRaises(ValueError, price_to_float, test_value)

