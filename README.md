# PrecisionMedicineToolkit

![FHIR-compliant output](https://i.imgur.com/tm9iZWM.png)

# Introduction

* EMR data must be easily accessible for experts from clinical informatics and bioinformatics to use.
* Polygenic SNP Search Tool (PSST) was invented to identify multiple SNPs that are associated with diseases. GenomicRobots is a web-based tool that simplifies the process of secure retrieval of patients genotypic information and sharing between collaborators. WGSA extracts information but does not give a FHIR-compliant output.
* FHIR-compliant output would be useful for scientists for extraction of variant information, RESTful API, and administrative actions.
* This toolkit addresses the needs to make this information easily accessible by creating a FHIR-compliant output that would be easily accessible by different types of bioinformaticians.

# What is this
This toolkit creates a FHIR-compliant JSON file from an input EMR file after extracting relevant biological information from databases. It runs the contents of the EMR file through various databases and collects information from them. PrecisionMedicineToolkit uses various steps for extracting genomic information.

![Workflow](https://i.imgur.com/PPOXC7U.png)

The workflow shows the steps and databases used in creating a FHIR-compliant JSON format.

![ANNOVAR output](https://i.imgur.com/jliJAzN.png)

ANNOVAR can compare variants to existing variant databases and annotate the variant records with any database values it retrieves. For example, it can note where relative to a known gene a variant falls (eg. if it is exonic, intergenic, etc.) and which genes it affects. It can compare a variant's position to regional annotations such as conserved or DNAse hypersensitive regions. Furthermore, it can also check specific annotation or scoring databases to see if a variant is present, such as dbSNP, PolyPhen, or 1000 genomes. Although it's developed for use with the human genome (defaulting to build hg18, though newer builds can be specified), genomes and databases for other species or samples may be used as well. Annovar exists as a suite of Perl scripts and supplementary data files, and thus can in theory be run on any system with a working perl interpreter. ANNOVAR annotates genetic variants detected from diverse genomes (including human genome hg18, hg19, hg38, as well as mouse, worm, fly, yeast and many others).

dbGaP provides APIs to access their respective data that allow metadata transfer in the XML or JSON formats. An API or Application Programming Interface provide an interface to data and services that other programs can directly use. The SRA toolkit is a software tool that allows researchers to obtain the sequence data (with appropriate access rights) from the SRA database. The search can be narrowed by various parameters, including the genomic region and type of sequence (e.g. mRNA and whole genome shotgun).

GWAS is a technique for determining genetic loci associated with common disease or traits using large groups of various across genomes.

![Sample variant copy identified](https://i.imgur.com/U0FlhJe.png)


# How to use it
`./precisionmed_wrapper.sh -i inputjsonfile.txt [-o outputDirectory]`

  -i inputFile JSON input file.
  -o outDir    Specify the directory for output - default is /home/ubuntu/PrecisionMedicineToolkit/output

# Requirements
SRA Toolkit (https://ncbi.github.io/sra-tools/install_config.html)

SnpEff (http://snpeff.sourceforge.net/index.html#)

TOPMed (Bravo API https://bravo.sph.umich.edu/freeze5/hg38/help)

GWAS (https://www.ebi.ac.uk/gwas/docs/about)

# Future Directions
* Modifying to accept multiple JSON variant files
* Adding annotation JSON files with relevant information from SnpEff and Annovar
* Integrating with a major EHR software company (such as EPIC)

# Authors
Halé Kpetigo (hale.kpetigo@gmail.com)

Syed Hussain Ather (shussainather@gmail.com)

Blythe Hospelhorn (blythe.hospelhorn@gmail.com)

Luli Zou (luli.zou@gmail.com)
