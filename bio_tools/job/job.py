import subprocess
from parameters.check_types import is_file_o
from parameters.parameters import Parameters


class Job:
    """
    Object Job stores information about a tool and implement methods to
    work with a tool.
    """
    def __init__(self, tool, module, parameters=None, user_settings=None):
        self.name = tool.name
        self.path = ('./tools/' + tool.name.lower() + '/' +
                     module.lower() + '.json')
        self.parameters = Parameters(self.path)
        self.user_settings = Parameters('./user_defaults.json')
        self.cmd = ''
        self.update()
        self.qsub_file = None

    def update(self):
        """
        Generate / regenerate the cmd string from parameters
        """
        self.cmd = ''
        for p in self.parameters.list:
            parameter = getattr(self.parameters, p)
            self.cmd += self.write_parameter(parameter)

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
        try:
            is_file_o(file_p)
            file_f = open(file_p, 'w')
            for name in self.user_settings.list:
                setting = getattr(self.user_settings, name)
                to_write = self.write_parameter(setting)
                if to_write:
                    file_f.write('#! "' + to_write + '\n')
            file_f.write('\n' + self.cmd)
            self.qsub_file = file_p
        except ValueError:
            print('** Error: could not generate qsub file.')

    def submit(self):
        """
        Submit a shell file with the command as a job on an HPC platform.
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
            self.parameters.set_from_dictionary(arg)
        elif (isinstance(arg, str)):
            self.parameters.set_from_json(arg)
        self.update()

    def write_parameter(self, parameter):
        cmd = ''
        if parameter.value:
            if parameter.flag:
                cmd += parameter.flag + ' '
            cmd += str(parameter.value) + ' '
        elif parameter.required:
            if parameter.flag:
                cmd += parameter.flag + ' '
            cmd += str(parameter.default) + ' '
        return cmd
