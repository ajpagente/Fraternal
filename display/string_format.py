from abc import ABCMeta, abstractmethod
from colorama import Fore, Back, Style

class BaseStringFormatter(metaclass=ABCMeta):
    @abstractmethod
    def table_header(self, string):
        pass

    @abstractmethod
    def field(self, string):
        pass

    @abstractmethod
    def sub_field(self, string):
        pass

    @abstractmethod
    def warning(self, string):
        pass

    @abstractmethod
    def highlight(self, string):
        pass

    @abstractmethod
    def error(self, string):
        pass

    @abstractmethod
    def info(self, string):
        pass

class ConsoleStringFormatter(BaseStringFormatter):
    """
        The ConsoleStringFormatter uses colorama to format a string to be displayed in a console.
    """
    def table_header(self, string):
        return self._format_(string, fore=Fore.BLUE, back=Back.BLACK)

    def field(self, string):
        return self.table_header(string)

    def sub_field(self, string):
        string = ' - ' + string
        return self.table_header(string)

    def error(self, string):
        return self._format_(string, fore=Fore.WHITE, back=Back.RED)
    
    def warning(self, string):
        return self.error(string)

    def highlight(self, string):
        return self._format_(string, fore=Fore.WHITE, back=Back.GREEN)

    def info(self, string):
        return self._format_(string, fore=Fore.WHITE, back=Back.BLUE)

    def _format_(self, string, fore=Fore.WHITE, back=Back.BLACK):
        return fore + back + string + Fore.RESET + Back.RESET
