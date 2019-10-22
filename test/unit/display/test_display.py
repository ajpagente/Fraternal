import unittest
import sys, os
from display.tables import SimpleConsoleTable
from display.format_specs import FormatSpecification
from display.string_format import WarningFormatter

class TestSimpleConsoleTable(unittest.TestCase):
    def test_header_created_no_column_match(self):
        """Ensure that the table returned is not empty and the properties are set correctly. The header items will not match the formatter. Actual content is not validated."""
        header = ['One', 'Two', 'Three', 'Four']
        fs = FormatSpecification('Protection Level', ['Dangerous'], WarningFormatter())
        ct = SimpleConsoleTable(header, fs)
        table = ct.get_table()
        actual = table.table
        self.assertIsNotNone(actual)
        self.assertEqual(ct.column_count, 4)
        self.assertEqual(len(ct.rows), 1)
        self.assertIsNone(ct.column_num)

    def test_header_created_column_match(self):
        """Ensure that the table returned is not empty and the properties are set correctly. One header item matches the formatter. Actual content is not validated."""
        header = ['One', 'Two', 'Three', 'Four']
        fs = FormatSpecification('Four', ['Dangerous'], WarningFormatter())
        ct = SimpleConsoleTable(header, fs)
        table = ct.get_table()
        actual = table.table
        self.assertIsNotNone(actual)
        self.assertEqual(ct.column_count, 4)
        self.assertEqual(len(ct.rows), 1)
        self.assertEqual(ct.column_num, 3)

    def test_add_short_row(self):
        header = ['One', 'Two', 'Three', 'Four']
        ct = SimpleConsoleTable(header)
        ct.add_row(['a','b'])
        self.assertEqual(len(ct.rows), 2)

        table = ct.get_table()
        actual = table.table
        self.assertIsNotNone(actual)
        actual = ct.rows[1]
        expected = ['a', 'b', '', '']
        self.assertEqual(actual, expected)
        self.assertEqual(ct.column_count, 4)
        self.assertIsNone(ct.column_num)

    def test_add_too_long_row(self):
        header = ['One', 'Two']
        ct = SimpleConsoleTable(header)

        self.assertRaises(ValueError, ct.add_row, ['a','b','c','d'])
        self.assertEqual(ct.column_count, 2)
        self.assertEqual(len(ct.rows), 1)
        self.assertIsNone(ct.column_num)

        table = ct.get_table()
        actual = table.table
        self.assertIsNotNone(actual)

    def test_add_exact_len_row(self):
        header = ['One', 'Two', 'Three', 'Four']
        ct = SimpleConsoleTable(header)
        ct.add_row(['a','b','c','d'])
        self.assertEqual(len(ct.rows), 2)
        table = ct.get_table()
        actual = table.table
        self.assertIsNotNone(actual)
        actual = ct.rows[1]
        expected = ['a', 'b', 'c', 'd']
        self.assertEqual(actual, expected)
        self.assertEqual(ct.column_count, 4)
        self.assertIsNone(ct.column_num)

    def test_row_format(self):
        """Validates that all properties are correct after a row is formatted. The formatting is not validated."""
        header = ['One', 'Two', 'Three', 'Four']
        fs = FormatSpecification('Three', ['c'], WarningFormatter())
        ct = SimpleConsoleTable(header, fs)
        ct.add_row(['a','b','c','d'])
        table = ct.get_table()
        actual = table.table
        self.assertIsNotNone(actual)
        self.assertEqual(ct.column_count, 4)
        self.assertEqual(len(ct.rows), 2)
        self.assertEqual(ct.column_num, 2)
        print(actual)

if __name__ == '__main__':
    unittest.main()