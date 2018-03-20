# PrecisionMedicineToolkit

# Introduction
Collaboration between clinical and bioinformatics work is difficult as data exchange formats for EMRs are very different. This toolkit searches through available databases to extract genetic information for a given EMR. A FHIR-compliant JSON will be created from the input EMR file.

# What is this
A FHIR-compliant JSON will be created from input EMR file. 

# How to use it 

# Requirements
SRA Toolkit

SnpEff (http://snpeff.sourceforge.net/index.html#)

TOPMed (Bravo API https://bravo.sph.umich.edu/freeze5/hg38/help)

GWAS

Ref of tools uses

# Workflow
![from the presentation](https://i.imgur.com/CcdnGVI.png)

# Installation
SRA Toolkit can be installed here: https://ncbi.github.io/sra-tools/install_config.html


# Bash template  
`./precisionmed_wrapper.sh -i inputjsonfile.txt -o outputjsonfile`