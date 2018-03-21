# PrecisionMedicineToolkit

![PrecisionMedicineToolkit](/images/pmtk.png)

# Introduction

* EMR data must be easily accessible for experts from clinical informatics and bioinformatics to use.
* Existing software annotatte variants and identify SNPs associated with disease, but no software integrates findings from variant annotation in a FHIR-compliant format.
* A FHIR-compliant output would be useful for scientists for extraction of variant information, RESTful API, and administrative actions.
* This toolkit addresses the needs to make this information easily accessible by creating a FHIR-compliant output that would be easily accessible by different types of bioinformaticians.

# What is this?
This toolkit creates a FHIR-compliant JSON file from an input EMR file after extracting relevant biological information from databases. It runs the contents of the EMR file through various databases and collects information from them. PrecisionMedicineToolkit uses various steps for extracting genomic information.

![Workflow](/images/pipeline.png)

The workflow shows the steps and databases used in creating a FHIR-compliant JSON format.

![ANNOVAR output](/images/annovar.png)

ANNOVAR can compare variants to existing variant databases and annotate the variant records with any database values it retrieves. Annovar exists as a suite of Perl scripts and supplementary data files, and thus can in theory be run on any system with a working perl interpreter. ANNOVAR annotates genetic variants detected from diverse genomes (including human genome hg18, hg19, hg38, as well as mouse, worm, fly, yeast and many others). PrecisionMedicineToolkit uses ANNOVAR along with SnpEff to filter variants for further analysis.

GWAS is a technique for determining genetic loci associated with common disease or traits using large groups of various across genomes. PrecisionMedicineToolkit uses the NHGRI GWAS catalog to annotate the input variants.


# How to use it
`./precisionmed_wrapper.sh -i inputjsonfile.txt [-o outputDirectory]`

  **-i inputFile** JSON input file.

  **-o outDir**    Specify the directory for output - default is /home/ubuntu/PrecisionMedicineToolkit/output/json.

  This bash script takes an into file which is a FHIR compliant JSON. The script is a wrapper that runs a combination of bash and Python scripts to produce
  ResearchStudy JSON files for GWAS results in the output directory.

  The underlying tools it runs:
  	** json2vcf.py --> Python script to convert JSON to VCF file
  	** snpeff_wrapper.sh --> Bash script that uses VCF to search using snpeff
	** runAnnovar.sh --> Bash script that uses VCF to search using Annovar
	** vcf_gwas.py --> Python script that uses VCF to search using GWAS
	** gwas2json.py --> Python script that converts GWAS output to JSON


## Example Input File

The following example input was taken from https://www.hl7.org/fhir/sequence-example.json.html
and edited manually to include chromosome and reference genome information.

![Example input](/images/example_input.png)

## Example Output File

An example of a generated GWAS FHIR-compliant ResearchStudy file (see https://www.hl7.org/fhir/researchstudy.html).

![Example output](/images/example_output.png)

# Requirements
SnpEff (http://snpeff.sourceforge.net/index.html#)

ANNOVAR (http://annovar.openbioinformatics.org/en/latest/)

GWAS catalog, located in /data (https://www.ebi.ac.uk/gwas/docs/about)

# Future Directions
* Modifying to accept multiple JSON variant files
* Adding annotation JSON files with relevant information from SnpEff and Annovar
* Integrate the following tools:
  - SRA Toolkit (https://ncbi.github.io/sra-tools/install_config.html)
  - TOPMed (Bravo API https://bravo.sph.umich.edu/freeze5/hg38/help)
* Integrating with a major EHR software company (such as EPIC)
* Expose toolkit to a web interface
* Validata JSON before processing
* Create docker component of the pipeline
* Pass in genome reference as a parameter
* Run in parallel to spead up result

# Authors
Halé Kpetigo (hale.kpetigo@gmail.com)

Syed Hussain Ather (shussainather@gmail.com)

Blythe Hospelhorn (blythe.hospelhorn@gmail.com)

Luli Zou (luli.zou@gmail.com)
