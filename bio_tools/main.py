from parameters.loading import *
from tools.stacks.de_novo import *
from cmd.command import *
from commons.user import *

USR_PATH = './user.json'

parameters = initialize_tool(DE_NOVO)
user_settings = initialize_user()

set_parameters_from_json(parameters, 'test.json')
set_parameters_from_json(user_settings, 'user.json')

values = {N_THREADS: 5,
          MISMATCHES_IN_INDIVIDUAL: 6,
          POPULATION_MAP: 'test.popmap'
          }

set_parameters_from_dictionary(parameters, values)

cmd = Command(parameters)
# print(cmd.cmd())
# cmd.run()
cmd.generate_qsub_file(user_settings)
