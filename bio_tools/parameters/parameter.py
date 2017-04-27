from distutils.util import strtobool
from . import type_checks
from ..commons.types import *


class Parameter:
    'Parameter object storing all information about a parameter'

    def __init__(self, name, flag, type_s, default, required):
        self.name = name
        self.flag = flag
        self.type = type_s
        self.default = default
        self.required = strtobool(required)
        self.value = None

    def set_value(self, value):
        """
        First check that the given value is of correct type (see type_checks.py)
        Then sets the parameter's value to the given value.
        """
        try:
            self.type_is_correct(value)
            if self.type == INT:
                self.value = (int(value))
            if self.type == FLOAT:
                self.value = (float(value))
            elif self.type == BOOL:
                self.value = strtobool(value)
            else:
                self.value = value
        except ValueError:
            print('*** Error while setting the value for parameter "' +
                  self.name + '"" : ' + self.type + ' expected, ' +
                  'but value was "' + value + '"')
            raise ValueError

    def type_is_correct(self, value):
        """
        Verifies that the value is of the correct type.
        Calls a type checking function according to "type_s" parameter.
        """
        if self.type == INT:
            return type_checks.is_int(value)
        elif self.type == FLOAT:
            return type_checks.is_float(value)
        elif self.type == DIR:
            return type_checks.is_dir(value)
        elif self.type == FILE_I:
            return type_checks.is_file_i(value)
        elif self.type == FILE_O:
            return type_checks.is_file_o(value)
        elif self.type == BOOL:
            return type_checks.is_bool(value)
        elif self.type == STR:
            return type_checks.is_str(value)
