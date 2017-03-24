from os.path import isdir, isfile
from commons.types import *
import re


def is_int(value):
    """
    Verifies that value is an integer.
    """
    try:
        int(value)
    except ValueError:
        print('** Error: "' + str(value) + '" is not an integer.')
        raise ValueError


def is_float(value):
    """
    Verifies that value is a float.
    """
    try:
        float(value)
    except ValueError:
        print('** Error: "' + str(value) + '" is not a float.')
        raise ValueError


def is_dir(value):
    """
    Verifies that value is a path to an existing directory.
    """
    if not (type(value) is str and isdir(value)):
        print('** Error: "' + str(value) + '" is not a path to an existing directory.')
        raise ValueError


def is_file_i(value):
    """
    Verifies that value is a path to an existing file.
    """
    if not (type(value) is str and isfile(value)):
        print('** Error: "' + str(value) + '" is not a path to an existing file.')
        raise ValueError


def is_file_o(value):
    """
    Verifies that value is a path to an existing output directory.
    """
    if not (type(value) is str and isdir('/'.join(value.split('/')[:-1]))):
        print('** Error: "' + str(value) + '" is not a path to an existing file.')
        raise ValueError


def is_cross(value):
    """
    Verifies that value is a 'cross' format.
    """
    if value not in CROSS_VALUES:
        print('** Error: "' + str(value) + '" is not a proper CROSS value.')
        raise ValueError


def is_bool(value):
    """
    Verifies that value is a boolean.
    """
    try:
        bool(value)
    except ValueError:
        print('** Error: "' + str(value) + '" is not a boolean.')
        raise ValueError


def is_str(value):
    """
    Verifies that value is a string.
    """
    if not type(value) is str:
        print('** Error: "' + str(value) + '" is not a string.')
        raise ValueError


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
