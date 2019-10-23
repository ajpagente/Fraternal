import unittest

from display.format_specs import FormatSpecification
from display.format_specs import RowFormatSpecification
from display.string_format import WarningFormatter

class TestFormatSpecification(unittest.TestCase):
    def test_valid_init(self):
        fs = FormatSpecification(['one','two'], WarningFormatter())
        self.assertIsNotNone(fs)

    def test_invalid_init(self):
        self.assertRaises(ValueError, FormatSpecification, 'one', WarningFormatter())
        self.assertRaises(ValueError, FormatSpecification, ['one'], None)

    def test_format_with_match(self):
        fs = FormatSpecification(['one','two'], WarningFormatter())
        string = 'two'
        formatted = fs.apply_format(string)
        self.assertIsNotNone(formatted)
        self.assertNotEqual(string, formatted)
     
    def test_format_no_match(self):
        fs = FormatSpecification(['one','two'], WarningFormatter())
        string = 'three'
        formatted = fs.apply_format(string)
        self.assertIsNotNone(formatted)
        self.assertEqual(string, formatted)

class TestRowFormatSpecification(unittest.TestCase):
    def test_valid_init(self):
        fs = RowFormatSpecification(['H1','H2'], 'H2', ['one','two'], WarningFormatter())
        self.assertIsNotNone(fs)

    def test_invalid_init(self):
        self.assertRaises(ValueError, RowFormatSpecification, 'H1', 'H1', ['one'], WarningFormatter())
        self.assertRaises(ValueError, RowFormatSpecification, ['H1', 'H2'], ['H1'], ['one'], WarningFormatter())
        self.assertRaises(ValueError, RowFormatSpecification, ['H1','H2'], 'H2', 'one', WarningFormatter())
        self.assertRaises(ValueError, RowFormatSpecification, ['H1','H2'], 'H2', ['one'], None)

    def test_valid_format_row(self):
        fs = RowFormatSpecification(['H1','H2'], 'H2', ['one','two'], WarningFormatter())
        row = ['three', 'two']
        fs.format_row(row)
        self.assertIsNotNone(row)
        self.assertNotEqual(row, ['three', 'two'])

    def test_no_match_format_row(self):
        fs = RowFormatSpecification(['H1','H2'], 'H2', ['one','two'], WarningFormatter())
        row = ['three', 'four']
        fs.format_row(row)
        self.assertIsNotNone(row)
        self.assertEqual(row, ['three', 'four'])

    def test_short_format_row(self):
        """ Validates the row does not change if it is too short"""
        fs = RowFormatSpecification(['H1','H2','H3','H4'], 'H4', ['one','two'], WarningFormatter())
        row = ['three', 'four']
        fs.format_row(row)
        self.assertIsNotNone(row)
        self.assertEqual(row, ['three', 'four'])

if __name__ == '__main__':
    unittest.main()