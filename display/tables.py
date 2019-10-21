from terminaltables import SingleTable

class ConsoleTables:
    def __init__(self, header=[]):
        self.header = header
    def get_table(self):
        if not self.header:
            return None
        return None