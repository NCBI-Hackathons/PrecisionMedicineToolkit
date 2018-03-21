#!/bin/bash

#Although it can't actually download ANNOVAR, it does take care of downloading and noting the locations
#of all the databases required by this program.

usage(){
cat << EOF
-----------------------------------------------------------------------------------------

PURPOSE:
	This script searches the target directory for files with the same names as the main annovar scripts. If it finds
	them, it creates a new database folder in that directory and downloads certain databases to it.
	
	IMPORTANT!!
	To repeat! This script will do NOTHING if it cannot find the annovar main script in the target directory!!
	
ARGUMENTS:
	-d	PATH	[Optional]	Installation directory. (Defaults to working directory)
	
EXAMPLE USAGE:
	bash installAnnovar.sh

-----------------------------------------------------------------------------------------

EOF
}

InstallDir=$(pwd)
while getopts "d:" OPTION; do
    case $OPTION in
		d)
			InstallDir=$OPTARG;;
        \?)
            usage
            exit 1
    esac
done

ANNOSCRIPT="annotate_variation.pl"
INSTALLERVERSION="1.0.0"

echo -e "Installation target directory: ${InstallDir}" >&2

#Search for script in target directory.
FINDRES=$(find ${InstallDir} -maxdepth 1 -name "${ANNOSCRIPT}")

if [ -z "${FINDRES}" ]; then
	echo -e "Annovar was not found in target directory. Please download Annovar and try again." >&2
	usage
	exit 1
fi

DBDIR="${InstallDir}/humandb"
if [ ! -d ${DBDIR} ]; then
	mkdir -p ${DBDIR}
	echo -e "${DBDIR} has been created..." >&2
fi

#Download databases...
ANNOSCRIPT="${InstallDir}/${ANNOSCRIPT}"

echo -e "Now downloading RefSeq (GRCh37)..." >&2
perl ${ANNOSCRIPT} -buildver hg19 -downdb -webfrom annovar refGene ${DBDIR}/

echo -e "Now downloading RefSeq (GRCh38)..." >&2
perl ${ANNOSCRIPT} -buildver hg38 -downdb -webfrom annovar refGene ${DBDIR}/

echo -e "Now downloading ENSEMBL (GRCh37)..." >&2
perl ${ANNOSCRIPT} -buildver hg19 -downdb -webfrom annovar ensGene ${DBDIR}/

echo -e "Now downloading ENSEMBL (GRCh38)..." >&2
perl ${ANNOSCRIPT} -buildver hg38 -downdb -webfrom annovar ensGene ${DBDIR}/

echo -e "Now downloading ExAC (GRCh37)..." >&2
perl ${ANNOSCRIPT} -buildver hg19 -downdb -webfrom annovar exac03 ${DBDIR}/

echo -e "Now downloading ExAC (GRCh38)..." >&2
perl ${ANNOSCRIPT} -buildver hg38 -downdb -webfrom annovar exac03 ${DBDIR}/

#echo -e "Now downloading gnomAD (GRCh37)..." >&2
#perl ${ANNOSCRIPT} -buildver hg19 -downdb -webfrom annovar gnomad_genome ${DBDIR}/

#echo -e "Now downloading gnomAD (GRCh38)..." >&2
#perl ${ANNOSCRIPT} -buildver hg38 -downdb -webfrom annovar gnomad_genome ${DBDIR}/

echo -e "Now downloading dbSNP (GRCh37)..." >&2
perl ${ANNOSCRIPT} -buildver hg19 -downdb -webfrom annovar avsnp150 ${DBDIR}/

echo -e "Now downloading dbSNP (GRCh38)..." >&2
perl ${ANNOSCRIPT} -buildver hg38 -downdb -webfrom annovar avsnp150 ${DBDIR}/

echo -e "Now downloading ClinVar (GRCh37)..." >&2
perl ${ANNOSCRIPT} -buildver hg19 -downdb -webfrom annovar clinvar_20170905 ${DBDIR}/

echo -e "Now downloading ClinVar (GRCh38)..." >&2
perl ${ANNOSCRIPT} -buildver hg38 -downdb -webfrom annovar clinvar_20170905 ${DBDIR}/

#I guess that's all I will include for now...?

#Mark completion of download
INSTALLFILE="${InstallDir}/pmt_install"
echo -e "${INSTALLERVERSION}" >> ${INSTALLFILE}
