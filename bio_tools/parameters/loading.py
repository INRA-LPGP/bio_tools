import json
from .parameter import Parameter
from commons.parameter import *


def load_json(path):
    """
    Encapsulate loading of json file with appropriate error messages.
    """

    try:
        parameters_f = open(path)
    except FileNotFoundError:
        print('** Error: could not load parameters from file "' +
              path + '".\n' +
              '** The file doesn''t exist or a wrong path was specified in' +
              ' "main.py"')
        return None

    try:
        return json.load(parameters_f)
    except json.decoder.JSONDecodeError:
        print('** Error: could not load parameters from file "' +
              path + '".\n' +
              'There is an error in the JSON file.')
        return None


def set_parameters_from_dictionary(parameters, dictionary):
    """
    Loads a json file containing the following information about
    each parameter: Name, Value.
    """

    for name, data in dictionary.items():
        try:
            parameters[name].set_value(data)
        except KeyError:
            print('** Error: parameter "' + name + '" does not exist.')
            return None
        except ValueError:
            print('** Error: could not affect value "' + str(data) +
                  '" to parameter "' + name + '".')
            return None
        except TypeError:
            if parameters is None or len(parameters) == 0:
                print('** Error: empty parameters dictionary')
            if dictionary is None or len(dictionary) == 0:
                print('** Error: empty values dictionary')
            return None

    return True


def set_parameters_from_json(parameters, path):
    """
    Loads a json file containing the following information about
    each parameter: Name, Value.
    """

    json_data = load_json(path)

    if not json_data:
        print('** Could not load parameters file.')
        return None

    set_parameters_from_dictionary(parameters, json_data)

    return True


def initialize(json_path):
    """
    Loads a json file containing the following information about
    each parameter: Name, Type and Default value.
    """

    json_data = load_json(json_path)

    if not json_data:
        print('** Could not load default parameters.')
        return None

    parameters = {}

    for name, data in json_data.items():
        try:
            parameters[name] = Parameter(name_s=data[NAME],
                                         type_s=data[TYPE],
                                         default_s=data[DEFAULT],
                                         flag_s=data[FLAG])
        except KeyError:
            print('** Error: parameter "' + name + '" does not exist.')
            return None
        except ValueError:
            print('** Error: could not affect value "' + str(data) +
                  '" to parameter "' + name + '".')
            return None

    return parameters


def initialize_tool(tool):
    """
    Initialize parameters from a default JSON file for a given tool.
    """

    json_path = './tools/' + tool + '/parameters.json'

    return initialize(json_path)


def initialize_user(name='user'):
    """
    Initialize user parameters from the default JSON file.
    """

    json_path = './parameters/user.json'

    return initialize(json_path)
