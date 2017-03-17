from . import check_types
from commons.types import *


class Parameter:
    'Parameter object storing all information about a parameter'
    parameter_count = 0

    def __init__(self, name_s, flag_s, type_s, default_s):
        self.name_s = name_s
        self.flag_s = flag_s
        self.type_s = type_s
        self.default_s = default_s
        self.value_s = None

    def name(self):
        return self.name_s

    def flag(self):
        return self.flag_s

    def type(self):
        return self.type_s

    def default(self):
        return self.default_s

    def value(self):
        return self.value_s

    def set_name(self, name_s):
        self.name_s = name_s

    def set_flag(self, flag_s):
        self.flag_s = flag_s

    def set_type(self, type_s):
        self.type_s = type_s

    def set_default(self, default_s):
        self.default_s = default

    def set_value(self, value_s):
        """
        First check that the given value is of correct type (see check_types.py)
        Then sets the parameter's value to the given value.
        """
        try:
            self.type_is_correct(value_s)
            if self.type_s == INT:
                self.value_s = (int(value_s))
            if self.type_s == FLOAT:
                self.value_s = (float(value_s))
            elif self.type_s == BOOL:
                self.value_s = bool(value_s)
            else:
                self.value_s = value_s
        except TypeError:
            print("The value of parameter " + self.name_s +
                  " should be of type " + self.type_s +
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
        if self.type_s == INT:
            return check_types.is_int(value)
        if self.type_s == FLOAT:
            return check_types.is_float(value)
        elif self.type_s == DIR:
            return check_types.is_dir(value)
        elif self.type_s == FILE_I:
            return check_types.is_file_i(value)
        elif self.type_s == FILE_O:
            return check_types.is_file_o(value)
        elif self.type_s == CROSS:
            return check_types.is_cross(value)
        elif self.type_s == BOOL:
            return check_types.is_bool(value)
        elif self.type_s == STR:
            return check_types.is_str(value)
        elif self.type_s == PIPE:
            return check_types.is_pipe(value)
        elif self.type_s == MAIL:
            return check_types.is_mail(value)
        elif self.type_s == MEMORY:
            return check_types.is_memory(value)
