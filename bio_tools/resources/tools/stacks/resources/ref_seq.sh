#!/bin/sh
#$ -M qpan@rennes.inra.fr
#$ -m be
#$ -N arapaima_ref_map
#$ -pe parallel_smp 16
#$ -l mem=15G
#$ -l h_vmem=50G

export PATH=/usr/local/bioinfo/src/Stacks/stacks-1.44/bin:$PATH

module load compiler/gcc-4.9.1

denovo_map.pl -o /work/qpan/romain/arapaima_gigas/rad_seq/denovo_map -T 16 -m 5 --gapped -b 3 -B Romain_radtags -D "Arapaima_gigas denovo_map -m 5 all individuals and reads" \
-O /work/qpan/romain/arapaima_gigas/rad_seq/popmap.txt --samples /work/qpan/romain/arapaima_gigas/samples/
