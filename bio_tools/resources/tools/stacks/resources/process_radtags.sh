#!/bin/sh
#$ -M qpan@rennes.inra.fr
#$ -m be
#$ -N process_radtags

export PATH=/usr/local/bioinfo/src/Stacks/stacks-1.44/bin:$PATH
module load compiler/gcc-4.9.1

process_radtags -f /work/qpan/Project_PhyloSex.280/Run_2_RAD_libraries.9666/RawData/Agigas_S8_L004_R1_001.fastq.gz -i gzfastq -o /work/qpan/romain/arapaima_gigas/samples -b /work/qpan/romain/arapaima_gigas/stacks/barcodes -c -q -r -e sbfI