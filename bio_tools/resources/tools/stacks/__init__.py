import os
# STACKS parameters
name = 'stacks'
path = 'stacks'
defaults = os.path.join(path, name, '.json')
instructions = ['export PATH=/usr/local/bioinfo/src/Stacks/stacks-1.44/bin:$PATH',
                'module load compiler/gcc-4.9.1']

# Modules:
modules = {'denovo_map': os.path.join(path, 'denovo_map.json')}
