from tools import stacks
from job import Job

par = {'N_THREADS': 8,
       'IDENTICAL_READS_FOR_STACK': 5}

denovo = Job(stacks, 'denovo_map')
denovo.set_parameters(par)
print(denovo.parameters.N_THREADS.value)
denovo.create_qsub_file()
