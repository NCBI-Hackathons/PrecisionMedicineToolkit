#!/usr/bin/python
import os
import os.path
import sys

### GLOBAL VARIABLES
sraListFile = sys.argv[1]
SRA_list = []
### FUNCTION DEFINITIONS
def createScripts(SRA_ID):
    subDirName = SRA_ID
    if (not os.path.isdir(subDirName)):
        os.mkdir(subDirName)
    # Create the shell script file
    shellFile = open(subDirName + "/" + SRA_ID + ".sh", "w")
    # Write to the file
    shellFile.write("#!/bin/bash\n\n")
    shellFile.write("sratoolkit.2.9.0-centos_linux64/bin/prefetch -L debug -t fasp -v -v " \
                     + SRA_ID + "\n\n")
    shellFile.close()

### IMPLEMENTATION
# Get the list of SRA IDs
with open(sraListFile) as F:
    for line in F:
       SRA_list.append(line.strip())
# Create the subdirectories and shell scripts
for i in SRA_list:
    createScripts(i)
