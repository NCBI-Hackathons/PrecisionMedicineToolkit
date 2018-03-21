# PrecisionMedicineToolkit

# Introduction
Collaboration between clinical and bioinformatics work is difficult as data exchange formats for Electronic Medical Records (EMRs) are very different. This toolkit searches through available databases to extract genetic information for a given EMR. A FHIR-compliant JSON will be created from the input EMR file.

EMR data must be easily accessible for experts from clinical informatics and bioinformatics to use. Polygenic SNP Search Tool (PSST) was invented to identify multiple SNPs that are associated with diseases. GenomicRobots is a web-based tool that simplifies the process of secure retrieval of patients genotypic information and sharing between collaborators. WGSA extracts information but does not give a FHIR-compliant output. 

A FHIR-compliant output would allow module components (called resources) to be accessed and assembled into working systems. The way clinical informaticians and bioinformaticians access the data can be streamlined and reduced down to the output of extracting genetic information from databases. The FHIR format output would give a standardized way to work with the clinical genetics data. Resources as basic units of interoperability and modular components that can be assembled into working systems can be used to solve clinical, administrative and infrastructural issues. FHIR has resources for administrative concepts such as patients, providers, organizations, and devices as well as a variety of clinical concepts including problems, medications, diagnostics, care plans and financial concerns, among others. FHIR also uses RESTful architecture programming interface (API) that would be compatible with health systems that use the REST web service. 

A physician who uses whole-genome sequencing to find a a variant in their patient can query the variants. The phenotype information about these variants can be extracted. An arbitrary note can be attached to the EMR for a patient using a simple API. The IT systems would have a chance to remain relevant in the healthcare integration space as FHIR become more widely adopted and integrated into healthcare information. 

This toolkit addresses the needs to make this information easily accessible by creating a FHIR-compliant output that would be easily accessible by different types of bioinformaticians. 

# What is this
This tool creates a FHIR-compliant JSON file from an input EMR file after extracting relevant biological information from databases. It runs the contents of the EMR file through various databases and collects information from them.  

# How to use it 

# Requirements
SRA Toolkit (https://ncbi.github.io/sra-tools/install_config.html)

SnpEff (http://snpeff.sourceforge.net/index.html#)

TOPMed (Bravo API https://bravo.sph.umich.edu/freeze5/hg38/help)

GWAS

# Workflow
![from the presentation](https://i.imgur.com/PPOXC7U.png)


# Bash template  
`./precisionmed_wrapper.sh -i inputjsonfile.txt -o outputjsonfile`

# Authors
Halé Kpetigo (hale.kpetigo@gmail.com)

Syed Hussain Ather (shussainather@gmail.com)

Blythe Hospelhorn (blythe.hospelhorn@gmail.com)

Luli Zou (luli.zou@gmail.com)
