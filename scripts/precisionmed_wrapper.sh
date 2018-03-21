#!/bin/bash

WDIR=/home/ubuntu/PrecisionMedicineToolkit/scripts
OUTPUT_DIR=/home/ubuntu/PrecisionMedicineToolkit/output
programname=$0
version="0.1"

#./precisionmed_wrapper.sh -i inputjsonfile.txt -o outputjsonfile

function usage {
	echo "usage:  $programname -i inputFile [-o outDir]"
	echo ""
	echo "  -i inputFile JSON input file."
	echo "  -o outDir    Specify the directory for output - default is "$OUTPUT_DIR/json
	echo ""
}


echo "Precision Medicine Toolkit, version "$version

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
	          OUTPUT_DIR=${OPTARG}
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
if [ ! -d "$OUTPUT_DIR" ]; then
  echo "$OUTPUT_DIR" does not exist - exiting.
  exit 0
fi

if [ -z "$INPUTFILE" ]; then
  echo "Please supply the input file to use."
  exit 0
fi

#Go to working directory
cd $WDIR

# Step 1 - Convert JSON to VCF
python $WDIR/json2vcf.py -i $INPUTFILE -o $OUTPUT_DIR/vcf.$BASEINPUTFILE.vcf

# Step 2 - Run VCF on snpeff
$WDIR/snpeff_wrapper.sh -i $OUTPUT_DIR/vcf.$BASEINPUTFILE.vcf

# Step 3 - Run VCF on annovar -i -o -g hg19 / hg38
$WDIR/runAnnovar.sh -i $OUTPUT_DIR/vcf.$BASEINPUTFILE.vcf -o $OUTPUT_DIR/annv.vcf.$BASEINPUTFILE.vcf -g hg19

# Step 4 - Run Annotation result on GWAS for Snpeff output
python $WDIR/vcf_gwas.py -i $OUTPUT_DIR/ann.vcf.$BASEINPUTFILE.vcf -g $WDIR/../data/gwas_catalog_v1.0-associations_e91_r2018-03-13.tsv -o $OUTPUT_DIR/gwas.snp.$BASEINPUTFILE.gwas

# Step 4 - Run Annotation result on GWAS for annovar output
python $WDIR/vcf_gwas.py -i $OUTPUT_DIR/annv.vcf.$BASEINPUTFILE.vcf -g $WDIR/../data/gwas_catalog_v1.0-associations_e91_r2018-03-13.tsv -o $OUTPUT_DIR/gwas.anv.$BASEINPUTFILE.gwas

# Step 5 - Convert snp+gwas VCF Results to JSON
python $WDIR/gwas2json.py -i $OUTPUT_DIR/gwas.snp.$BASEINPUTFILE.gwas -o $OUTPUT_DIR/json/

# Step 6 - Convert anv+gwas VCF Results to JSON
python $WDIR/gwas2json.py -i $OUTPUT_DIR/gwas.anv.$BASEINPUTFILE.gwas -o $OUTPUT_DIR/json/