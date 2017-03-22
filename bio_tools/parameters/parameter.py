from distutils.util import strtobool
from . import check_types
from commons.types import *


class Parameter:
    'Parameter object storing all information about a parameter'

    def __init__(self, name_s, flag_s, type_s, default_s, required_s):
        self.name = name_s
        self.flag = flag_s
        self.type = type_s
        self.default = default_s
        self.required = strtobool(required_s)
        self.value = None

    def set_value(self, value_s):
        """
        First check that the given value is of correct type (see check_types.py)
        Then sets the parameter's value to the given value.
        """
        try:
            self.type_is_correct(value_s)
            if self.type == INT:
                self.value = (int(value_s))
            if self.type == FLOAT:
                self.value = (float(value_s))
            elif self.type == BOOL:
                self.value = strtobool(value_s)
            else:
                self.value = value_s
        except ValueError:
            print("The value of parameter " + self.name +
                  " should be of type " + self.type +
                  " but you tried to set the value to " +
                  value_s + ".\nCheck the input for this parameter." +
                  " For more information about value types," +
                  " check file commons.py section Types.")
            raise ValueError

    def type_is_correct(self, value):
        """
        Verifies that the value is of the correct type.
        Calls a type checking function according to "type_s" parameter.
        """
        if self.type == INT:
            return check_types.is_int(value)
        if self.type == FLOAT:
            return check_types.is_float(value)
        elif self.type == DIR:
            return check_types.is_dir(value)
        elif self.type == FILE_I:
            return check_types.is_file_i(value)
        elif self.type == FILE_O:
            return check_types.is_file_o(value)
        elif self.type == CROSS:
            return check_types.is_cross(value)
        elif self.type == BOOL:
            return check_types.is_bool(value)
        elif self.type == STR:
            return check_types.is_str(value)
        elif self.type == PIPE:
            return check_types.is_pipe(value)
        elif self.type == MAIL:
            return check_types.is_mail(value)
        elif self.type == MEMORY:
            return check_types.is_memory(value)
