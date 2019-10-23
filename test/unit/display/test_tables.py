import unittest
import sys, os
from display.tables import SimpleConsoleTable
from display.format_specs import RowFormatSpecification
from display.string_format import WarningFormatter

class TestSimpleConsoleTable(unittest.TestCase):
    def test_header_created(self):
        """Ensure that the table returned is not empty and the properties are set correctly. The header items will not match the formatter. Actual content is not validated."""
        header = ['One', 'Two', 'Three', 'Four']
        fs = RowFormatSpecification(header, 'Three', ['Dangerous'], WarningFormatter())
        ct = SimpleConsoleTable(header, fs)
        actual = ct.get_table()
        self.assertIsNotNone(actual)
        self.assertEqual(len(ct.rows), 1)

    def test_add_exact_len_row(self):
        header = ['One', 'Two', 'Three', 'Four']
        ct = SimpleConsoleTable(header)
        
        ct.add_row(['a','b','c','d'])
        self.assertEqual(len(ct.rows), 2)

        actual = ct.get_table()
        self.assertIsNotNone(actual)
        
        actual = ct.rows[1]
        expected = ['a', 'b', 'c', 'd']
        self.assertEqual(actual, expected)

    def test_add_short_row(self):
        header = ['One', 'Two', 'Three', 'Four']
        ct = SimpleConsoleTable(header)
        ct.add_row(['a','b'])
        self.assertEqual(len(ct.rows), 2)

        actual = ct.get_table()
        self.assertIsNotNone(actual)
        actual = ct.rows[1]
        expected = ['a', 'b', '', '']
        self.assertEqual(actual, expected)


    def test_add_too_long_row(self):
        header = ['One', 'Two']
        ct = SimpleConsoleTable(header)

        self.assertRaises(ValueError, ct.add_row, ['a','b','c','d'])
        self.assertEqual(len(ct.rows), 1)

        actual = ct.get_table()
        self.assertIsNotNone(actual)

    def test_row_format(self):
        """Validates that all properties are correct after a row is formatted. The formatting is not validated."""
        header = ['One', 'Two', 'Three', 'Four']
        fs = RowFormatSpecification(header, 'Three', ['c'], WarningFormatter())
        ct = SimpleConsoleTable(header, fs)
        ct.add_row(['a','b','c','d'])
        actual = ct.get_table()
        self.assertIsNotNone(actual)
        self.assertEqual(len(ct.rows), 2)


if __name__ == '__main__':
    unittest.main()