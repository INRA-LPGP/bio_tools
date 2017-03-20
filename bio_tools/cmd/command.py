import subprocess
from parameters.check_types import is_file_o


class Command:
    """
    Object Command implements methods to generate a command based on a set
    of parameters. Other methods also allow to submit the command either on
    a standard computer (run()) or in an HPC environment (submit())
    """

    def __init__(self, parameters_s, user_settings_s=None):
        self.cmd_s = ''
        self.parameters_s = parameters_s
        self.user_settings_s = user_settings_s
        self.qsub_file_s = None
        self.update()

    def update(self, parameters_s=None):
        """
        Generate / regenerate the cmd string from parameters
        """
        if parameters_s:
            self.set_parameters(parameters_s)
        for parameter in self.parameters().values():  # parameters is a dictionary
            if parameter.value() is not None:
                if parameter.flag() is not None:
                    self.cmd_s += parameter.flag() + ' '
                self.cmd_s += str(parameter.value()) + ' '

    def cmd(self):
        return self.cmd_s

    def set_cmd(self, cmd_s):
        self.cmd_s = cmd_s

    def parameters(self):
        return self.parameters_s

    def set_parameters(self, parameters_s):
        self.parameters_s = parameters_s

    def qsub_file(self):
        return self.qsub_file_s

    def set_qsub_file(self, qsub_file_s):
        self.qsub_file_s = qsub_file_s

    def user_settings(self):
        return self.user_settings

    def set_user_settings(self, user_settings_s):
        self.user_settings_s = user_settings_s

    def run(self):
        """
        Run command and capture output for verification.
        """
        result = subprocess.Popen(self.cmd(), shell=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)
        while True:
            line = result.stdout.readline()
            if not line:
                break

    def generate_qsub_file(self, file_p='./denovo_map.sh'):
        """
        Generate a shell file with the command in the format required
        to submit a job on an HPC platform.
        """
        try:
            is_file_o(file_p)
            file_f = open(file_p, 'w')
            for name, setting in self.user_settings_s.items():
                file_f.write('#$ ')
                if setting.flag():
                    file_f.write(str(setting.flag()) + ' ')
                file_f.write(str(setting.value()) + '\n')
            file_f.write('\n' + self.cmd())
            self.set_qsub_file(file_p)
        except ValueError:
            print('** Error: could not generate qsub file.')

    def submit(self):
        """
        Submit a shell file (stored the command as a job on an HPC platform.
        """
        try:
            if not self.qsub_file_s:
                self.generate_qsub_file()
            qsub_cmd = 'qsub ' + self.qsub_file()
            result = subprocess.Popen(qsub_cmd, shell=True,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT)
            if not result:
                return None
        except ValueError:
            print('** Error: qsub file not found. Did you generate a shell' +
                  ' file before submitting?')
