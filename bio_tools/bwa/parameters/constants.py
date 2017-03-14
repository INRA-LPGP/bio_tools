# Modes
INDEX = 'index'
MEM = 'mem'
ALN = 'aln'
SAMSE = 'samse'
SAMPE = 'sampe'
BWASW = 'bwasw'

# INDEX specific option
ALGORITHM = 'algorithm'

# MEM specific options
SEED_LENGTH = 'seed_length'
BAND_WIDTH = 'band_width'
X_DROPOFF = 'x_dropoff'
RESEEDING = 'reseeding'
DISCARD_THRESHOLD = 'discard_threshold'
PAIR_END_SW = 'pair_end_sw'
CLIPPING_PENALTY = 'clipping_penalty'
UNPAIRED_PENALTY = 'unpaired_penalty'
INTERLEAVED_PAIRED_END = 'interleaved_paired_end'
OUTPUT_SCORE_THRESHOLD = 'output_score_threshold'
OUTPUT_ALL_ALIGNMENTS = 'output_all_alignments'
APPEND_FASTX_COMMENT = 'append_fastx_comment'
USE_HARD_CLIPPING = 'use_hard_clipping'
SHORT_AS_SECONDARY = 'short_as_secondary'
VERBOSE = 'verbose'

# ALN specific options
MAX_EDIT_DISTANCE = 'max_edit_distance'
MAX_GAP_OPEN = 'max_gap_open'
MAX_GAP_EXTEND = 'max_gap_extend'
LONG_DELETION_END_THRESHOLD = 'long_deletion_end_threshold'
INDEL_END_THRESHOLD = 'indel_end_threshold'
SEED_SUBSEQUENCE_SIZE = 'seed_subsequence_size'
SEED_MAX_EDIT_DISTANCE = 'seed_max_edit_distance'
SUBOPTIMAL_USE_THRESHOLD = 'suboptimal_use_threshold'
DISABLE_ITERATIVE_SEARCH = 'disable_iterative_search'
READ_TRIMMING = 'read_trimming'
ILLUMINA_READ_FORMAT = 'illumina_read_format'
BARCODE_STARTING_LENGTH = 'barcode_starting_length'
INPUT_BAM_FORMAT = 'input_bam_format'
INPUT_BAM_OPTION = 'input_bam_option'

# SAMSE specific options
OUTPUT_ALIGNMENTS_N = 'output_alignments_n'
READS_SAI_FILE = 'reads_sai_file'

# SAMPE specific options
MAX_INSERT_SIZE = 'max_insert_size'
MAX_READ_OCCURENCE = 'max_read_occurence'
LOAD_FM_INDEX = 'load_fm_index'
OUTPUT_ALIGNMENT_PROPER_N = 'output_alignment_proper_n'
OUTPUT_ALIGNMENT_DISCORDANT_N = 'output_alignment_discordant_n'
READS_SAI_FILE_1 = 'reads_sai_file_1'
READS_SAI_FILE_2 = 'reads_sai_file_2'
READS_FILE_1 = 'reads_file_1'
READS_FILE_2 = 'reads_file_2'

# BWASW specific options
BAND_WIDTH = 'band_width'
MINIMUM_SCORE_THRESHOLD = 'minimum_score_threshold'
THRESHOLD_ADJUSTMENT_COEFF = 'threshold_adjustment_coeff'
Z_BEST_HEURISTIC = 'z_best_heuristic'
MAX_SA_INTERVAL = 'max_sa_interval'
MIN_SEED_NUMBER = 'min_seed_number'

# Shared options
DATABASE_PREFIX = 'database_prefix'  # INDEX, MEM, ALN, SAMSE, BWASW
OUTPUT_FILE = 'output_file'  # INDEX, MEM, ALN, SAMSE, SAMPE, BWASW
READS_FILE = 'reads_file'  # MEM, ALN, SAMSE, BWASW
MATES_FILE = 'mates_file'  # MEM
N_THREADS = 'n_threads'  # MEM, ALN, BWASW
MATCHING_SCORE = 'matching_score'  # MEM, BWASW
MISMATCH_PENALTY = 'mismatch_penalty'  # MEM, ALN, BWASW
GAP_OPEN_PENALTY = 'gap_open_penalty'  # MEM, ALN, BWASW
GAP_EXTEND_PENALTY = 'gap_extend_penalty'  # MEM, ALN, BWASW
READ_GROUP_HEADER = 'read_group_header'  # MEM, SAMSE
