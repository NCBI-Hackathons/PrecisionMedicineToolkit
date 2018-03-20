# Searching genomic databases and references for precision medecine

## The Challenge
- Collaboration between clinical work and bioinformatics is difficult because EMR data exchange format are different.
- The industry has been building large databases of bioinformatic data that could be useful for clinicians when diagnosing patients
- Some of these databases are:
	- TOPMed (Trans-Omics for Precision Medicine)
	- dbGaP
	- SRA
	- GWAS (Genome-Wide Association Study)
- Doing searches in these databases is currently manual and tedious
- Use case: While diagnosing a client who has a mutation on a specific gene, can I search public (or restricted access) database for the same variant, or populations of similar patients? 


## Our solution
- Precision Medicine Toolkit 
- Receives a Json from an EMR system with a variant to analyse
- Searches genomic databases and references for population that corresponds to the variant
- Returns a Json to the EMR with search results
