from tools import stacks
from job import Job

values = {'N_THREADS': 16,
          'MISMATCHES_IN_INDIVIDUAL': 6,
          'POPULATION_MAP': ''}

de_novo = Job(stacks, stacks.de_novo)
de_novo.set_parameters(values)
de_novo.create_qsub_file()
