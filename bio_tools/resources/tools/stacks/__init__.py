import os

# STACKS parameters
NAME = 'stacks'
PATH = 'stacks'
DEFAULTS = os.path.join(PATH, NAME, '.json')
INSTRUCTIONS = ['export PATH=/usr/local/bioinfo/src/Stacks/stacks-1.44/bin:$PATH',
                'module load compiler/gcc-4.9.1']

# Modules:
MODULES = {'denovo_map': os.path.join(PATH, 'denovo_map.json')}
