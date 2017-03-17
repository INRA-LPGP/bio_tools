import subprocess
from parameters.check_types import is_file_o


class Command:

    def __init__(self, parameters):
        self.cmd_s = 'denovo_map.pl'
        self.parameters = parameters
        for parameter in parameters.values():
            if parameter.value() is not None:
                self.cmd_s += (' ' + parameter.flag() + ' ' +
                               str(parameter.value()))

    def cmd(self):
        return self.cmd_s

    def set_cmd(self, cmd_s):
        self.cmd_s = cmd_s

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
            # print(line.decode('utf-8').strip('\n'))

    def generate_qsub_file(self, user_settings, file_p='./denovo_map.sh'):
        try:
            is_file_o(file_p)
            file_f = open(file_p, 'w')
            for name, setting in user_settings.items():
                file_f.write('# ' + setting.flag() + ' ' + setting.value() + '\n')
            file_f.write('\n' + self.cmd())
        except ValueError:
            print('** Error: could not generate qsub file.')
