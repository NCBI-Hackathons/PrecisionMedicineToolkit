import os
import sys
import argparse
import json
import pandas as pd

def gwas2json(gwasfile, outputdir):
    """Function to grab entries from GWAS file and spit out FHIR-compliant JSON
    in outputdir. Currently I am making it output (a) ResearchStudy file(s)."""
    gwas = pd.read_table('results.txt', header = None)
    for index, row in gwas.iterrows():
        title = row['6']
        relatedArtifact_display = row['5']
        disease = row['7']


def write_ResearchStudy(title, url, disease, sample_info, gene, rsID, var_type):






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

gwas = pd.read_table('results.txt', header=None)
print(gwas.head(1))
