# Parameter types
INT = 'INT'  # Value should be an integer (0, 1, 2, 5, 15, 173,...)
FLOAT = 'FLOAT'  # Value should be a float (0, 0.5, 1.73, 152.36, ...)
DIR = 'DIR'  # Value should be a string containing the path to an existing directory
FILE_I = 'FILE_I'  # Value should be a string containing the path to an existing file
FILE_O = 'FILE_O'  # Value should be a string containing the path to an output file in an existing directory
CROSS = 'CROSS'  # Value should be a string of type CROSS (see below)
BOOL = 'BOOL'  # Value should be a boolean ('True', 'False', 'T', 'F', 0, 1)
STR = 'STR'  # Value should be a string
PIPE = 'PIPE'  # Value should be a string containing a pipe command (ustacks:--max_locus_stacks 4)
MAIL = 'MAIL'  # Value should be an email adress ("xxx@xxx.xxx")
MEMORY = 'MEMORY'

# Possible values
CROSS_VALUES = {'CP', 'F2', 'BC1', 'DH', 'GEN'}
