from terminaltables import SingleTable
from colorama import Fore, Back, Style

def display_tabulated(data):   
    formatted = format_table(data)
    table = SingleTable(formatted)
    print(table.table)

def display_permissions(permissions):
    formatted = []
    formatted.append(['Permissions'])
    for permission in permissions:
        formatted.append([permission])
    table = SingleTable(formatted)
    print(table.table)


def format_field(field, color=Fore.BLUE):
    return color + field + Fore.RESET

def format_table(data):
    formatted = []
    for field,value in data:
        formatted.append([format_field(field), value])
    return formatted