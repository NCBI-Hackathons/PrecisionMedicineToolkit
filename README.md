# PrecisionMedicineToolkit

# Introduction
Collaboration between clinical and bioinformatics work is difficult as data exchange formats for EMRs are very different. This toolkit searches through available databases to extract genetic information for a given EMR. A FHIR-compliant JSON will be created from the input EMR file.

# What is this
This tool creates a FHIR-compliant JSON file from an input EMR file after extracting relevant biological information from databases. It runs the contents of the EMR file through various databases and collects information from them.  

# How to use it 

# Requirements
SRA Toolkit (https://ncbi.github.io/sra-tools/install_config.html)

SnpEff (http://snpeff.sourceforge.net/index.html#)

TOPMed (Bravo API https://bravo.sph.umich.edu/freeze5/hg38/help)

GWAS

# Workflow
![from the presentation](https://i.imgur.com/CcdnGVI.png)


# Bash template  
`./precisionmed_wrapper.sh -i inputjsonfile.txt -o outputjsonfile`

# Authors
Halé Kpetigo (hale.kpetigo@gmail.com)

Syed Hussain Ather (shussainather@gmail.com)

Blythe Hospelhorn (blythe.hospelhorn@gmail.com)

Luli Zou (luli.zou@gmail.com)
