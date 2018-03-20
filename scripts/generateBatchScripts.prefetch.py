#!/usr/bin/python
import os
import os.path
import sys

### GLOBAL VARIABLES
sraListFile = sys.argv[1]
batchName = sys.argv[2]
batchFullPath = "base/batches/" + batchName
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
    shellFile.write("cd base/Project_Space\n\n")
    shellFile.write("# Download the SRA file\n")
    shellFile.write("sratoolkit.2.9.0-centos_linux64/bin/prefetch -L debug -t fasp -v -v " \
                     + SRA_ID + "\n\n")
    shellFile.close()
def makeJobListFile():
    jobListFile = open("base/jobLists/" + batchName + "_JobList.txt", "w")
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
