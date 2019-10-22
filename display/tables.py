from terminaltables import SingleTable

class SimpleConsoleTable:
    def __init__(self, header=[], format_specs=None):
        self.header = header
        self.column_count = len(header)
        self.format_specs = format_specs
        self.column_num = self._column_num_(header, format_specs)
        self.rows = []
        self.rows.append(header)

    def add_row(self, row=[]):
        if (len(row) > self.column_count):
            raise ValueError('The row has too many elements')

        count = self.column_count - len(row)
        for _ in range(count):
            row.append('')
        row = self._format_row_(row)
        self.rows.append(row)

    def get_table(self):
        if not self.header:
            return None
        return SingleTable(self.rows)

    def _format_row_(self, row):
        if not self.column_num:
            return row
        if (row[self.column_num] == self.format_specs.value[0]):
            formatted_row = row
            formatted_row[self.column_num] = self.format_specs.formatter.format(formatted_row[self.column_num])
            return formatted_row
        else:
            return row

    def _column_num_(self, header, format_specs):
        """Returns the index of the header item that matches the column_name in the format_specs. Otherwise, return None"""
        if not format_specs:
            return None

        column_num = 0
        for item in header:
            if item == format_specs.column_name:
                return column_num
            column_num = column_num + 1
        return None
            