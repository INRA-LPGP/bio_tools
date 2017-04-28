from bio_tools import Job, tools, environments

par = {'N_THREADS': 8,
       'IDENTICAL_READS_FOR_STACK': 5}

denovo = Job(tool=tools.stacks, module='denovo_map', env=environments.sge)
denovo.set_parameters(par)
denovo.create_qsub_file()
print(denovo.cmd)
