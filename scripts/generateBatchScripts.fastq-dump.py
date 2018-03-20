import os
import os.path
import sys
### GLOBAL VARIABLES
sraListFile = sys.argv[1]
batchName = sys.argv[2]
batchFullPath = "batches/" + batchName
SRA_list = []
### FUNCTION DEFINITIONS
def createScripts(SRA_ID):
    subDirName = batchFullPath + "/" + SRA_ID
    # Create the subdirectory within the batch directory
    if (not os.path.isdir(subDirName)):
        os.mkdir(subDirName)
    # Create the shell script file
    shellFile = open(subDirName + "/" + SRA_ID + ".sh", "w")
    # Write to the file
    shellFile.write("#!/bin/bash\n\n")
    shellFile.write("cd Project_Space\n\n")
    shellFile.write("sratoolkit.2.9.0-centos_linux64/bin/vdb-validate " + SRA_ID + ".sra &> \
                     Project_Space/validation_outputs/" + batchName + "/" +  SRA_ID \
                     + ".validation_out\n\n")
    shellFile.write("if grep -q 'err' Project_Space/validation_outputs/" \
                     + batchName + "/" + SRA_ID + ".validation_out; then\n")
    shellFile.write("\techo 'Verification of " + SRA_ID + ".sra failed'\n")
    shellFile.write("\tcp Project_Space/validation_outputs/" + batchName + "/" \
                      + SRA_ID + ".validation_out Project_Space/validation_failures/" \
                      + batchName + "\n")
    shellFile.write("else\n")
    shellFile.write("\techo 'No errors found in " + SRA_ID + ".sra'\n")
    shellFile.write("\t# Convert the SRA into fastq\n")
    shellFile.write("\tsratoolkit.2.9.0-centos_linux64/bin/fastq-dump -v --gzip --split-files \
                      -O fastq_files/" + batchName + " Project_Space/sra/" \
                      + SRA_ID + ".sra\n")
    shellFile.write("fi\n")
    shellFile.close()

def makeJobListFile():
    jobListFile = open("jobLists/" + batchName + "_JobList.txt", "w")
    for i in SRA_list:
        # Write the jobList for the Anisimov launcher
        # Something like "/base/batches/batch1/SRR123 SRR123.sh"
        jobListFile.write(batchFullPath + "/" + i + " " + i + ".sh\n")
    jobListFile.close()
### IMPLEMENTATION
# Get the list of SRA IDs
with open(sraListFile) as F:
    for line in F:
       SRA_list.append(line.strip())
# If the batch directory does not exist, create it
if (not os.path.isdir(batchFullPath)):
    os.mkdir(batchFullPath)
# Create the subdirectories and shell scripts
for i in SRA_list:
    createScripts(i)
makeJobListFile()
try:# Create directory in the validation folders
    os.mkdir("Project_Space/validation_outputs/" + batchName)
    os.mkdir(“Project_Space/validation_failures/" + batchName)
except: pass
