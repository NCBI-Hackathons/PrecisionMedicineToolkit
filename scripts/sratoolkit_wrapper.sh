#!/bin/bash

# Generate the  bash scripts
# Perform prefetch to get the SRA data
python scripts/generateBatchScripts.prefetch.py data/example_SRRlist.txt

# Convert the SRA into fastq
python scripts/generateBatchScripts.fastq-dump.py data/example_SRRlist.txt

# Align fastq to reference index

