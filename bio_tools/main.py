from tools import stacks
from job import Job
import os

analysis = 'denovo_map'
m = 10

root_dir = '/work/rferon/'
species_dir = os.path.join(root_dir, 'species')
batch_dir = os.path.join(root_dir, 'batch_processing')
shell_dir = os.path.join(batch_dir, 'shell')
sh_file = open(os.path.join(shell_dir, 'denovo_map_' + str(m) + '.sh'), 'w')

species = [d for d in os.listdir(species_dir)
           if os.path.isdir(os.path.join(species_dir, d))]

for specie in species:
    species_short = specie.split('_')[0][0] + '_' + specie.split('_')[1]
    rad_path = os.path.join(species_dir, specie, 'data', 'rad_seq')
    samples_path = os.path.join(rad_path, 'samples')
    analysis_path = os.path.join(species_dir, specie, 'analyses', 'rad_seq', analysis)
    if not os.path.isdir(analysis_path):
        os.mkdir(analysis_path)
    results_path = os.path.join(analysis_path, 'results_' + str(m))
    if not os.path.isdir(results_path):
        os.mkdir(results_path)
    qsub_path = os.path.join(analysis_path, 'denovo_map_' + str(m) + '.sh')

    batch_p = os.path.join(root_dir, 'batch_processing')
    results_p = os.path.join(batch_p, 'results')
    python_p = os.path.join(batch_p, 'python')
    shell_p = os.path.join(batch_p, 'shell')

    par = {'N_THREADS': 8,
           'IDENTICAL_READS_FOR_STACK': m,
           'POPULATION_MAP': os.path.join(rad_path, species_short + '_popmap.txt'),
           'BATCH_ID': 1,
           'OUTPUT_PATH': results_path,
           'SAMPLES_DIRECTORY': samples_path,
           'DISABLE_DATABASE': 'True'
           }

    settings = {"SHELL": "!/bin/sh",
                "EMAIL_ADRESS": "romain.feron@inra.fr",
                "MAIL_OPTIONS": "",
                "N_THREADS": "8",
                "MEM": "mem=8G",
                "H_VMEM": "h_vmem=10G",
                "JOB_NAME": specie + '_de_novo_' + str(m)}

    de_novo = Job(stacks, stacks.de_novo)
    de_novo.set_parameters(par)
    de_novo.set_user_settings(settings)
    de_novo.create_qsub_file(qsub_path)

    sh_file.write('qsub ' + qsub_path + '\n')
