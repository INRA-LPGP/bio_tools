import pkgutil
from commons.tools import *

# Dynamically imports any submodule inside 'tools'
__all__ = []

for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    __all__.append(module_name)
    module = loader.find_module(module_name).load_module(module_name)
    exec('%s = module' % module_name)


# Reference for future rules

'''
def is_pipe(value):
    """
    Verifies that value is a pipe string (program:command).
    """
    if not (type(value) is str and len(value.split(':')) == 2):
        print('** Error: "' + str(value) + '" is not a pipe command.')
        raise ValueError


def is_mail(value):
    """
    Verifies that value is an email adress (xxx@xxx.xxx).
    """
    if not (type(value) is str and re.match(r'([^@]+)@([^@]+)[.](.+)', value)):
        print('** Error: "' + str(value) + '" is not an email adress.')
        raise ValueError


def is_memory(value):
    """
    Verifies that value is a memory value (1G, 8G, 15G, ...).
    """
    if not (type(value) is str and re.match(r'[h_vmem=]+(\d+)G', value)):
        print('** Error: "' + str(value) + '" is not a valid memory value.')
        raise ValueError

def is_cross(value):
    """
    Verifies that value is a 'cross' format.
    """
    if value not in CROSS_VALUES:
        print('** Error: "' + str(value) + '" is not a proper CROSS value.')
        raise ValueError
'''
