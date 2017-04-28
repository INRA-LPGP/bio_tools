import subprocess
import os
from bio_tools.parameters.type_checks import is_file_o
from bio_tools.parameters.parameters import Parameters
from bio_tools.commons.types import *
import bio_tools.resources as resources


class Job:
    """
    Object Job stores information about a tool and implement methods to
    work with a tool.
    """
    def __init__(self, tool, module, parameters=None, settings=None,
                 env=None):
        self.instructions = tool.INSTRUCTIONS
        self.name = tool.NAME
        if module:
            self.tool_path = os.path.join(resources.TOOLS,
                                          tool.MODULES[module])
        else:
            self.tool_path = os.path.join(resources.TOOLS,
                                          tool.DEFAULTS)
        self.parameters = Parameters(self.tool_path)
        if parameters:
            self.parameters.set_from_dictionary(parameters)
        self.env = env
        if env:
            self.user_settings = Parameters(os.path.join(resources.ENVS,
                                                         env.DEFAULTS))
        else:
            self.user_settings = None
        self.cmd = ''
        if parameters:
            self.update()
        self.qsub_file_path = None

    def update(self):
        """
        Generate / regenerate the cmd string from parameters
        """
        self.cmd = ''
        for name, par in self.parameters.list.items():
            # self.cmd += self.write_parameter(data)
            self.cmd += par.write()

    def run(self):
        """
        Run command and capture output for verification.
        """
        result = subprocess.Popen(self.cmd, shell=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)
        while True:
            line = result.stdout.readline()
            if not line:
                break

    def create_qsub_file(self, file_p='./denovo_map.sh'):
        """
        Generate a shell file with the command in the format required
        to submit a job on an HPC platform.
        """
        if self.env:
            try:
                is_file_o(file_p)
                file_f = open(file_p, 'w')
                for name, data in self.user_settings.list.items():
                    to_write = self.write_setting(data)
                    if to_write:
                        file_f.write(to_write)
                for instruction in self.instructions:
                    file_f.write(instruction + '\n')
                file_f.write('\n' + self.cmd)
                self.qsub_file = file_p
            except ValueError:
                print('** Error: could not generate qsub file.')
        else:
            print('** Error: you need to specify an environment to generate' +
                  ' a qsub file. Available environments: ' +
                  resources.environments.show())

    def submit(self):
        """
        Submit a shell file with the command as a job on an SGE platform.
        Maybe this should also be in resources/env/sge or something
        """
        try:
            if not self.qsub_file:
                self.create_qsub_file()
            qsub_cmd = 'qsub ' + self.qsub_file
            result = subprocess.Popen(qsub_cmd, shell=True,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT)
            if not result:
                return None
        except ValueError:
            print('** Error: qsub file not found. Did you generate a shell' +
                  ' file before submitting?')

    def set_parameters(self, arg):
        if (isinstance(arg, dict)):
            self.parameters.set_from_dictionary(arg)
        elif (isinstance(arg, str)):
            self.parameters.set_from_json(arg)
        self.update()

    def set_user_settings(self, arg):
        if (isinstance(arg, dict)):
            self.user_settings.set_from_dictionary(arg)
        elif (isinstance(arg, str)):
            self.user_settings.set_from_json(arg)
        self.update()

    # Move this to parameter
    def write_parameter(self, parameter):
        cmd = ''
        if parameter.value:
            if parameter.flag:
                cmd += parameter.flag + ' '
            if parameter.type != BOOL:
                cmd += str(parameter.value) + ' '
        elif parameter.required and parameter.default:
            print('** Warning: setting default value for required parameter ' +
                  parameter.name + ' (' +
                  parameter.default + ')')
            if parameter.flag:
                cmd += parameter.flag + ' '
            if parameter.type != BOOL:
                cmd += str(parameter.default) + ' '
        return cmd

    # This is crap
    def write_setting(self, setting):
        cmd = '#'
        if setting.value:
            if setting.value == 'SHELL':
                cmd += setting.value
            if setting.flag:
                cmd += '$ ' + setting.flag + ' '
            cmd += str(setting.value) + ' '
            cmd = cmd.rstrip(' ') + '\n'
        elif setting.required:
            if setting.value == 'SHELL':
                cmd += setting.value
            if setting.flag:
                cmd += '$ ' + setting.flag + ' '
            cmd += str(setting.default) + ' '
            cmd = cmd.rstrip(' ') + '\n'
        else:
            cmd = ''
        return cmd
