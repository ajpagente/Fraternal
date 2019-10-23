import logging

from display.string_format import BaseConsoleStringFormatter

class FormatSpecification():
    def __init__(self, values, formatter):
        if not isinstance(values, list):
            raise ValueError('values must be a list.')

        if not isinstance(formatter, BaseConsoleStringFormatter):
            raise ValueError('formatter must be an instance of BaseConsoleStringFormatter.')

        self.values = values
        self.formatter = formatter

    def _format_(self, string):
        """ Returns the formatted string. """
        return self.formatter.format(string)

    def apply_format(self, string):
        """ Returns the formatted string if it matches any of the value, otherwise the same string is returned. """
        for value in self.values:
            if (value == string):
                return self._format_(string)
        return string

class RowFormatSpecification(FormatSpecification):
    def __init__(self, header, column_name, values, formatter):
        super().__init__(values, formatter)

        if not isinstance(header, list):
            raise ValueError('header must be a list.')

        if not isinstance(column_name, str):
            raise ValueError('column_name must be a string.')

        self.column_name = column_name
        self.column_num = self._column_num_(header)
        if not self.column_num:
            raise ValueError('The column name does not match a column in the header.')


    def format_row(self, row):
        """ If successful, the row is formatted, otherwise the row is not changed. """
        try:
            row[self.column_num] = self.apply_format(row[self.column_num])
        except:
            logging.info('Exception during row formatting.')
            pass

    def _column_num_(self, header):
        """Returns the index of the header item that matches the column_name. Otherwise, return None"""
        column_num = 0
        for item in header:
            if item == self.column_name:
                return column_num
            column_num = column_num + 1
        return None