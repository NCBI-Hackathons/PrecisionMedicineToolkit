import os
import os.path
import sys

### GLOBAL VARIABLES
sraListFile = sys.argv[1]
SRA_list = []
### FUNCTION DEFINITIONS
def createScripts(SRA_ID):
    subDirName = "SRR_scripts/" + SRA_ID
    if (not os.path.isdir(subDirName)):
        os.mkdir(subDirName)
    # Create the shell script file
    shellFile = open(subDirName + "/" + SRA_ID + ".sh", "w")
    # Write to the file
    shellFile.write("#!/bin/bash\n\n")
    shellFile.write("sratoolkit.2.9.0-centos_linux64/bin/vdb-validate " + SRA_ID + ".sra &> \
                     validation_outputs/" +  SRA_ID \
                     + ".validation_out\n\n")
    shellFile.write("if grep -q 'err' validation_outputs/" \
                     + SRA_ID + ".validation_out; then\n")
    shellFile.write("\techo 'Verification of " + SRA_ID + ".sra failed'\n")
    shellFile.write("\tcp validation_outputs/" \
                      + SRA_ID + ".validation_out validation_failures/\n")
    shellFile.write("else\n")
    shellFile.write("\techo 'No errors found in " + SRA_ID + ".sra'\n")
    shellFile.write("\t# Convert the SRA into fastq\n")
    shellFile.write("\tsratoolkit.2.9.0-centos_linux64/bin/fastq-dump -v --gzip --split-files \
                      -O fastq_files/sra/" \
                      + SRA_ID + ".sra\n")
    shellFile.write("fi\n")
    shellFile.close()

### IMPLEMENTATION
# Get the list of SRA IDs
with open(sraListFile) as F:
    for line in F:
       SRA_list.append(line.strip())
# Create the subdirectories and shell scripts
for i in SRA_list:
    createScripts(i)
