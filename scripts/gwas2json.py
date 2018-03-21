import os
import sys
import argparse
import json
import math
import pandas as pd

def gwas2json(gwasfile, outputdir):
    """Function to grab entries from GWAS file and spit out FHIR-compliant JSON
    in outputdir. Currently I am making it output (a) ResearchStudy file(s)."""
    gwas = pd.read_table(gwasfile, header = 0)
    for index, row in gwas.iterrows():
        filename = 'gwas_result_{0}.json'.format(index)
        title = row['STUDY']
        url = row['LINK']
        disease = row['DISEASE/TRAIT']
        if type(row['INITIAL SAMPLE SIZE']) is str:
            initial_sample_size = row['INITIAL SAMPLE SIZE']
        else:
            initial_sample_size = 'No initial sample size provided'
        if type(row['REPLICATION SAMPLE SIZE']) is str:
            replication_sample_size = row['REPLICATION SAMPLE SIZE']
        else:
            replication_sample_size = 'No replication sample size provided'
        sample_info = initial_sample_size + '/' + replication_sample_size
        gene = row['REPORTED GENE(S)']
        rsid = row['SNPS']
        var_type = row['CONTEXT']
        write_ResearchStudy(filename = filename, title = title, url = url,
                            disease = disease, sample_info = sample_info,
                            gene = gene, rsID = rsid, var_type = var_type,
                            outputdir = outputdir)

def write_ResearchStudy(filename, title, url, disease, sample_info, gene, rsID,
                        var_type, outputdir):
    """See format here: https://www.hl7.org/fhir/researchstudy.html"""
    with open(filename, 'w') as outfile:
        json.dump({"resourceType" : "ResearchStudy",
                   "title" : title,
                   "status" : "completed",
                   "category" : [{
                           "text" : "gwas"
                       }],
                   "relatedArtifact" : [{
                           "type" : "citation",
                           "display" : title,
                           "url" : url
                       }],
                   "description" : ("1. **Disease**: " + disease + "  " +
                                   "2. **Sample Initial/Replicate**: " +
                                   sample_info + "  " +
                                   "3. **Gene**: " + gene + "  " +
                                   "4. **rsID**: " + rsID + "  " +
                                   "5. **Variant Type**: " + var_type)
                   }, outfile)

class App(object):

    def run(self, args):
        name = os.path.basename(args[0])
        parser = self.create_parser(name)
        opts = parser.parse_args(args[1:])
        return self.main(name, opts)

    def create_parser(self, name):
        p = argparse.ArgumentParser(
                prog = name,
                formatter_class = argparse.ArgumentDefaultsHelpFormatter,
                description = 'Grabs variants from JSON and outputs a VCF')
        p.add_argument(
                '-i', '--input',
                help = 'Input GWAS results tab-separated file')
        p.add_argument(
                '-o', '--output',
                help = 'Output directory')
        return p

    def main(self, name, opts):
        if opts.input is None:
            raise SystemExit('Must specify input GWAS results file with -i')
        if opts.output is None:
            raise SystemExit('Must specify output JSON file with -o')
        gwas2json(opts.input, opts.output)


if __name__ == '__main__':
    app = App()
    app.run(sys.argv)
