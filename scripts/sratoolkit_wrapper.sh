#!/bin/bash

# Generate the jobList.txt file and the necessary bash scripts and put them within their own directory in the batches folder
python scripts/generateBatchScripts.prefetch.py /base/batches/batch_lists/batchX.txt batchX

# Grab the IDs in the batch file and check to see if each SRA filei is found in the sra folder
python /base/scripts/checkSRAsDownloaded.py /base/batches/batch_lists/batchX.txt

cd /base/Project_Space
/path/to/sra-toolkit/bin/vdb-validate <SAMPLE_ID>.sra &>   \
    /base/Project_Space/validation_outputs/batchX/<SAMPLE_ID>.validation_out
if grep -q 'err' /base/Project_Space/validation_outputs/batchX/<SAMPLE_ID>.validation_out;
then
else
fi
echo 'Verification of <SAMPLE_ID>.sra failed'
cp /base/Project_Space/validation_outputs/batchX/<SAMPLE_ID>.validation_out  \
   /projects/sciteam/baib/InputData_DoNotTouch/dbGaP-13335/validation_failures/batch5
echo 'No errors found in <SAMPLE_ID>.sra'
# Convert the SRA into fastq
/path/to/sra-toolkit/bin/fastq-dump -v --gzip --split-files \
       -O /base/fastq_files/batchX /base/Project_Space/sra/<SAMPLE_ID>.sra
