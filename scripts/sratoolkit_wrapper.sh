#!/bin/bash

function usage {
        echo "usage:  $programname -s data/example_SRR_list.txt -r reference_genome.fasta"
        echo ""
        echo "  -s example_SRR_list.txt         List of SRR values to extract - always required."
        echo "  -r reference_genome.fasta       Reference Genome for using bowtie2 to index - always required."
        echo ""
        documentTaxList

}

while getopts ":s:r:" o; do
case "${s}" in 
s)

SRR_LIST=${OPTARG}
;;
r)
REFERENCE=${OPTARG}
;;
:)
echo "Invalid option: $OPTARG requires an argument"
usage
exit 0
;;
esac
done

mkdir SRR
cd SRR

# Generate the  bash scripts
# Perform prefetch to get the SRA data
while read SRR_LIST; do
prefetch -L debug -t fasp -v -v $SRR_LIST
done 

while read SRR_LIST; do
vdb-validate $SRR_LIST.sra &> $SRR_LIST.validation_out
done

while read SRR_LIST; do
fastq-dump -v --gzip --split-files -O fastq_files/$SRR_LIST $SRR_List.sra
done

