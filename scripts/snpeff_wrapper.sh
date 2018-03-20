#!/bin/bash

SNPEFF_DIR=/home/ubuntu/SnpEff/snpEff/
SNPEFF_OUTPUT=/home/ubuntu/PrecisionMedicineToolkit/output
programname=$0
version="0.1"

function usage {
	echo "usage:  $programname -i inputFile [-o outDir]"
	echo ""
	echo "  -i inputFile VCF input file."
	echo "  -o outDir    Specify the directory for output - default is "$SNPEFF_OUTPUT
	echo ""
}


echo "Precision Medicine Toolkit - Variant Annotation Module, version "$version

# Basic flag option validation
if [ $# -eq 0 ]; then     # Cannot be called meaningfully without flags
	usage
	exit 0
fi

while getopts ":i:o:" o; do
    case "${o}" in
        i)
            INPUTFILE=${OPTARG}
            BASEINPUTFILE=$(basename $INPUTFILE)
            ;;
	     o)
	          SNPEFF_OUTPUT=${OPTARG}
	           ;;
	:)
	   echo  "Invalid option: $OPTARG requires an argument"
	   usage
	   exit 0
	   ;;
        \?)	
            usage
	    exit 0
            ;;
    esac
done
shift $((OPTIND-1))

# More sophisticated validation
if [ ! -d "$SNPEFF_OUTPUT" ]; then
  echo "$SNPEFF_OUTPUT" does not exist - exiting.
  exit 0
fi

if [ -z "$INPUTFILE" ]; then
  echo "Please supply the input file to use."
  exit 0
fi

java -Xmx4g -jar $SNPEFF_DIR/snpEff.jar GRCh37.75 $INPUTFILE > $SNPEFF_OUTPUT/ann.$BASEINPUTFILE
