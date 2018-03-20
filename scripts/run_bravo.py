import os
import sys
import argparse
import vcf
import subprocess

def run_bravo(input_vcf, bravo_dir):
    vcf_reader = vcf.Reader(open(input_vcf, 'r'))
    for record in vcf_reader:
        bash_command = 'curl -H "Authorization: Bearer `"' +
                        os.path.join(bravo_dir, 'bravo') +
                        ' print-access-token`"' +
                        ' "https://bravo.sph.umich.edu/freeze5/hg38/api/v1/variant?variant_id=chr"' +
                        record.CHROM + '-' + record.POS + '-' + record.REF + '-' +
                        record.ALT + '"'
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
                description = 'Grabs variants from JSON and outputs a VCF')
        p.add_argument(
                '-i', '--input',
                help = 'Input VCF')
        p.add_argument(
                '-o', '--output',
                help = 'Output file with Bravo results')
        p.add_argument(
                '-bd', '--bravo_dir',
                help = 'directory that contains the Bravo executable',
                default = '.'
            )
        return p

    def main(self, name, opts):
        if opts.input is None:
            raise SystemExit('Must specify input VCF file with -i')
        if opts.output is None:
            raise SystemExit('Must specify output file for Bravo results with -o')
        json2vcf(opts.input, opts.output)


if __name__ == '__main__':
    app = App()
    app.run(sys.argv)
