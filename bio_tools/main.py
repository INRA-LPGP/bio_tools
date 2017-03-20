from parameters.loading import *
from tools.stacks.de_novo import *
from cmd.command import *
from commons.user import *

USR_PATH = './user.json'

parameters = initialize_tool(DE_NOVO)
user_settings = initialize_user()

set_parameters_from_json(parameters, './test/test.json')
set_parameters_from_json(user_settings, './test/user.json')

values = {N_THREADS: 5,
          MISMATCHES_IN_INDIVIDUAL: 6,
          POPULATION_MAP: './test/test.popmap',
          CMD: 'denovo_map.pl'
          }

set_parameters_from_dictionary(parameters, values)

cmd = Command(parameters, user_settings)
# print(cmd.cmd())
# cmd.run()
# cmd.submit()
