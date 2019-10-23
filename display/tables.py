from terminaltables import SingleTable
from display.string_format import HeaderFormatter

class BaseConsoleTable:
    def _format_header_(self, header, formatter=HeaderFormatter()):
        formatted = []
        for item in header:
            formatted.append(formatter.format(item))
        return formatted

class SimpleConsoleTable(BaseConsoleTable):
    def __init__(self, header, format_specs=None):
        self.rows = []
        self.header = self._format_header_(header)
        self.rows.append(self.header)
        self.format_specs = format_specs

        # self.column_count = len(header)
        
        # self.column_num = self._column_num_(header, format_specs)
        
        

    def add_row(self, row=[]):
        if (len(row) > len(self.header)):
            raise ValueError('The row has too many elements')

        pad_count = len(self.header) - len(row) 
        for _ in range(pad_count):
            row.append('')

        if self.format_specs:
            self.format_specs.format_row(row)
        self.rows.append(row)

    def get_table(self):
        if not self.header:
            return None
        return SingleTable(self.rows).table

    # def _format_row_(self, row):
    #     if not self.column_num:
    #         return row
    #     if (row[self.column_num] == self.format_specs.value[0]):
    #         formatted = row
    #         formatted[self.column_num] = self.format_specs.formatter.format(formatted[self.column_num])
    #         return formatted
    #     else:
    #         return row

    # def _column_num_(self, header, format_specs):
    #     """Returns the index of the header item that matches the column_name in the format_specs. Otherwise, return None"""
    #     if not format_specs:
    #         return None

    #     column_num = 0
    #     for item in header:
    #         if item == format_specs.column_name:
    #             return column_num
    #         column_num = column_num + 1
    #     return None
            