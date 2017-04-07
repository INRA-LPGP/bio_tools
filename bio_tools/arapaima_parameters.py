from tools import stacks
from job import Job
import os

analysis = 'denovo_map'

n_values = [1, 2, 4]
M_values = [1, 3, 5, 8]

root_dir = '/work/rferon/species/arapaima_gigas/'
analysis_dir = os.path.join(root_dir, 'analyses', 'rad_seq', 'parameters')
rad_dir = os.path.join(root_dir, 'data', 'rad_seq')
samples_path = os.path.join(rad_dir, 'samples')
popmap_path = os.path.join(rad_dir, 'a_gigas_popmap.txt')

results_dir = os.path.join(analysis_dir, 'results')
qsub_dir = os.path.join(analysis_dir, 'qsub')
shell_dir = os.path.join(analysis_dir, 'shell')

qsub_file = open(os.path.join(qsub_dir, 'parameters.sh'), 'w')

for n in n_values:

    output_dir = os.path.join(results_dir, 'n_' + str(n))
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    sh_file = os.path.join(shell_dir, 'denovo_map_n_' + str(n) + '.sh')

    par = {'N_THREADS': 8,
           'IDENTICAL_READS_FOR_STACK': 10,
           'MISMATCHES_IN_CATALOG': n,
           'POPULATION_MAP': popmap_path,
           'BATCH_ID': 0,
           'OUTPUT_PATH': output_dir,
           'SAMPLES_DIRECTORY': samples_path,
           'DISABLE_DATABASE': 'True'
           }

    settings = {"SHELL": "!/bin/sh",
                "N_THREADS": "8",
                "MEM": "mem=8G",
                "H_VMEM": "h_vmem=10G",
                "JOB_NAME": 'de_novo_n_' + str(n)}

    de_novo = Job(stacks, 'denovo_map')
    de_novo.set_parameters(par)
    de_novo.set_user_settings(settings)
    de_novo.create_qsub_file(sh_file)

    qsub_file.write('qsub ' + sh_file + '\n')

for M in M_values:

    output_dir = os.path.join(results_dir, 'M_' + str(M))
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    sh_file = os.path.join(shell_dir, 'denovo_map_M_' + str(M) + '.sh')

    par = {'N_THREADS': 8,
           'IDENTICAL_READS_FOR_STACK': 10,
           'MISMATCHES_IN_INDIVIDUAL': M,
           'POPULATION_MAP': popmap_path,
           'BATCH_ID': 0,
           'OUTPUT_PATH': output_dir,
           'SAMPLES_DIRECTORY': samples_path,
           'DISABLE_DATABASE': 'True'
           }

    settings = {"SHELL": "!/bin/sh",
                "N_THREADS": "8",
                "MEM": "mem=8G",
                "H_VMEM": "h_vmem=10G",
                "JOB_NAME": 'de_novo_M_' + str(M)}

    de_novo = Job(stacks, 'denovo_map')
    de_novo.set_parameters(par)
    de_novo.set_user_settings(settings)
    de_novo.create_qsub_file(sh_file)

    qsub_file.write('qsub ' + sh_file + '\n')
