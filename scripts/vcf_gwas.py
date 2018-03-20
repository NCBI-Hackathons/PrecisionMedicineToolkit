import os
import sys
import argparse
import vcf
import subprocess

def vcf_gwas(input_vcf, gwas_catalog, output_file):
    vcf_reader = vcf.Reader(open(input_vcf, 'r'))
    for record in vcf_reader:
        rsid = record.ID
        bash_command = "grep '" + rsid + "' " + gwas_catalog + " > " + output_file
        os.system(bash_command)

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
                description = 'Grabs GWAS lines based on VCF lines')
        p.add_argument(
                '-i', '--input',
                help = 'Input VCF')
        p.add_argument(
                '-g', '--gwas',
                help = 'Path to GWAS catalog',
                default = './data/gwas_catalog_v1.0-associations_e91_r2018-03-13.tsv'
            )
        p.add_argument(
                '-o', '--output',
                help = 'Output file with filtered GWAS results')
        return p

    def main(self, name, opts):
        if opts.input is None:
            raise SystemExit('Must specify input VCF file with -i')
        if opts.output is None:
            raise SystemExit('Must specify output file for GWAS results')
        vcf_gwas(opts.input, opts.gwas, opts.output)


if __name__ == '__main__':
    app = App()
    app.run(sys.argv)
