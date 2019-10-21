from terminaltables import SingleTable
from colorama import Fore, Back, Style

from android.android import get_permission_protection_level
from android.android import get_permission_added
from android.android import get_permission_deprecated

def display_tabulated(data):   
    # formatted = format_table(data)
    # table = SingleTable(formatted)
    table = SingleTable(data)
    print(table.table)

def display_permissions(permissions):
    formatted = []
    formatted.append(['Permissions', 'Protection Level', 'Added', 'Deprecated'])
    for permission in permissions:
        split_perm = permission.split('.')
        short_perm = split_perm[-1]
        protection_level = get_permission_protection_level(short_perm)
        if protection_level == 'Dangerous':
            protection_level = format_warning(protection_level)
        added = get_permission_added(short_perm)
        deprecated = get_permission_deprecated(short_perm)
        formatted.append([permission,protection_level,added,deprecated])
    table = SingleTable(formatted)
    print(table.table)


def format_field(field, color=Fore.BLUE):
    return color + field + Fore.RESET

def format_warning(field, fore=Fore.WHITE, back=Back.RED):
    return fore + back + field + Fore.RESET + Back.RESET

def format_lookout(field, fore=Fore.WHITE, back=Back.BLUE):
    return fore + back + field + Fore.RESET + Back.RESET

def format_info(field, fore=Fore.WHITE, back=Back.GREEN):
    return fore + back + field + Fore.RESET + Back.RESET

def format_table(data):
    formatted = []
    for field,value in data:
        formatted.append([format_field(field), value])
    return formatted