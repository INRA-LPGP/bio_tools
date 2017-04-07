from collections import OrderedDict
import json
from .parameter import Parameter
from commons.parameter import *


class Parameters:

    def __init__(self, json_path):
        self.list = []
        json_data = self.load_json(json_path)
        if not json_data:
            print('** Could not load default parameters.')
        for name, data in json_data.items():
            try:
                setattr(self, name, Parameter(name=data[NAME],
                                              type_s=data[TYPE],
                                              default=data[DEFAULT],
                                              flag=data[FLAG],
                                              required=data[REQUIRED]))
                self.list.append(name)
            except KeyError:
                print('** Error: parameter "' + name + '" does not exist.')
            except ValueError:
                print('** Error: could not affect value "' + str(data) +
                      '" to parameter "' + name + '".')

    def set_from_dictionary(self, dictionary):
        """
        Loads a json file containing the following information about
        each parameter: Name, Value.
        """
        for name, data in dictionary.items():
            try:
                p = getattr(self, name)
                f = getattr(p, 'set_value')
                setattr(p, name, f(data))
            except KeyError:
                print('** Error: parameter "' + name + '" does not exist.')
            except ValueError:
                print('** Error: could not affect value "' + str(data) +
                      '" to parameter "' + name + '".')
            except TypeError:
                if parameters is None or len(parameters) == 0:
                    print('** Error: empty parameters dictionary')
                if dictionary is None or len(dictionary) == 0:
                    print('** Error: empty values dictionary')

    def set_from_json(self, path):
        """
        Loads a json file containing the following information about
        each parameter: Name, Value.
        """
        json_data = self.load_json(path)
        if not json_data:
            raise FileNotFoundError('Could not load parameters file.')
        self.set_from_dictionary(json_data)

    def load_json(self, path):
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
            return json.load(parameters_f, object_pairs_hook=OrderedDict)
        except json.decoder.JSONDecodeError:
            print('** Error: could not load parameters from file "' +
                  path + '".\n' +
                  'There is an error in the JSON file.')
            raise FileNotFoundError('COUCOU')
