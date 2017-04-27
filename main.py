from bio_tools import Job, tools

par = {'N_THREADS': 8,
       'IDENTICAL_READS_FOR_STACK': 5}

denovo = Job(tools.stacks, 'denovo_map')
denovo.set_parameters(par)
print(denovo.parameters.N_THREADS.value)
denovo.create_qsub_file()
