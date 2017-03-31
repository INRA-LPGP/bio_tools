import os
from tools import stacks
from job import Job


root_dir = '/home/rferon/programming/bio_tools/test/'
samples_path = root_dir
results_path = root_dir
qsub_path = os.path.join(root_dir, 'qsub.sh')

par = {'N_THREADS': 8,
       'IDENTICAL_READS_FOR_STACK': 10,
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
            "JOB_NAME": '_de_novo_10'}

de_novo = Job(stacks, stacks.de_novo)
de_novo.set_parameters(par)
de_novo.set_user_settings(settings)
de_novo.create_qsub_file(qsub_path)
