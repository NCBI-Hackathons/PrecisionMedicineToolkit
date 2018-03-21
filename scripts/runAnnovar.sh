#!/bin/bash

#An ANNOVAR wrapper for PMT

#	Created March 20, 2018
#	Blythe Hospelhorn

# Current version: 1.0.0

usage(){
cat << EOF
-----------------------------------------------------------------------------------------

PURPOSE:
	This script should initiate a basic annovar run on an input VCF.
	
ARGUMENTS:
	-i	FILE	[Required]	Input VCF containing variants to annotate.
	-o	FILE	[Required]	Output VCF path.
	-g	STRING	[Optional]	Genome build (Default: hg19)
					Valid options:
						hg19
						hg38
	
EXAMPLE USAGE:
	bash annovar.sh -i myvariants.vcf -o myvariants_anno.vcf

-----------------------------------------------------------------------------------------

EOF
}

INSTALLERVERSION="1.0.0"
GENOMEBUILD="hg19"
while getopts "i:o:g:" OPTION; do
    case $OPTION in
		i)
			InputVCF=$OPTARG;;
		o)
			OutputVCF=$OPTARG;;
		g)
			GENOMEBUILD=$OPTARG;;
        \?)
            usage
            exit 1
    esac
done

#From https://stackoverflow.com/questions/59895/getting-the-source-directory-of-a-bash-script-from-within
SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" 

#Navigate to Annovar directory and check for Annovar. If it's not there, then prompt to download.
#Unfortunately, for now it looks like Annovar has to be downloaded manually...
ANNODIR="$(dirname ${SCRIPTDIR})/annovar"
ANNOSCRIPT_MAIN="${ANNODIR}/annotate_variation.pl"
ANNOSCRIPT_QUICK="${ANNODIR}/table_annovar.pl"
if [ ! -s ${ANNOSCRIPT_MAIN} ]; then
	echo -e "ERROR!! ANNOVAR could not be found!" >&2
	echo -e "-----------------------------------" >&2
	echo -e "Due to its license, ANNOVAR must unfortunately be downloaded manually." >&2
	echo -e "Go to http://annovar.openbioinformatics.org/en/latest/user-guide/download/ to obtain the program.\n" >&2
	echo -e "Place the downloaded files in ${ANNODIR} ensuring that perl scripts are on the top level." >&2
	echo -e "In other words, the path to the main script should be ${ANNOSCRIPT_MAIN}" >&2
	echo -e "\nAlso make sure that perl is installed on your system!" >&2
	exit 1
fi

DateString=$(date +\"%Y%m%d%H%M%S\")
INSTALLSCRIPT="${SCRIPTDIR}/installAnnovar.sh"
INSTALLFILE="${ANNODIR}/pmt_install"
NEEDSINSTALL="false"
if [ ! -s ${INSTALLFILE} ]; then
	NEEDSINSTALL="true"
else
	#Grep for current installation version. If not present, reinstall.
	GREPRES=$(grep "${INSTALLERVERSION}" ${INSTALLFILE})
	if [ -z "${GREPRES}" ]; then
		NEEDSINSTALL="true"
	fi
fi

#Install if needed
if [ "${NEEDSINSTALL}" == "true" ]; then
	echo -e "Annovar databases current to version ${INSTALLERVERSION} could not be found..." >&2
	echo -e "Now downloading Annovar databases..." >&2
	bash ${INSTALLSCRIPT} -d ${ANNODIR}
fi

#Run annovar
OUTDIR=$(dirname ${OutputVCF})
echo -e "Now calling ANNOVAR. Direct output will be placed in ${OUTDIR}" >&2
#perl ${ANNOSCRIPT_QUICK} ${InputVCF} humandb/ -buildver ${GENOMEBUILD} -out ${OUTDIR}/pmtannovar${DateString} -remove -protocol refGene,exac03,avsnp150,gnomad_genome,clinvar_20170905 -operation g,f,f,f,f -nastring . -polish -vcfinput
perl ${ANNOSCRIPT_QUICK} ${InputVCF} humandb/ -buildver ${GENOMEBUILD} -out ${OUTDIR}/pmtannovar${DateString} -remove -protocol refGene,exac03,avsnp150,clinvar_20170905 -operation g,f,f,f -nastring . -polish -vcfinput

FINDRESULTS=$(find ${OUTDIR} -maxdepth 1 -iname "pmtannovar${DateString}*.vcf")
if [ -z "${FINDRESULTS}" ]; then
	echo -e "ANNOVAR output VCF could not be found. Please check ${OUTDIR} for candidates..." >&2
	exit 1
fi
OUTPUT=$(cat ${FINDRESULTS} | head -1)
echo -e "File ${FINDRESULTS} was found. Assuming to be ANNOVAR output..." >&2
mv ${OUTPUT} ${OutputVCF}
