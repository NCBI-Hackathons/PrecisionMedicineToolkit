import os
import sys
import argparse
import json
import vcf

def json2vcf(jsonfile, outputfile):
    """Function to grab variant(s) from JSON file and spit out VCF in outputdir.
    Currently this function assumes that there is a chromosome field that
    has the chromosome number encoded in 'code'. Hopefully this generalizes."""
    # Make the vcf file w/ header
    vcf_filename = outputfile
    try:
        os.remove(vcf_filename)
    except OSError:
        pass

    # Get variant from JSON file
    j = json.load(open(jsonfile))
    chrom = j['referenceSeq']['chromosome']['coding'][0]['code']
    pos = j['variant'][0]['start']
    ref = j['variant'][0]['referenceAllele']
    alt = j['variant'][0]['observedAllele']
    patient = j['patient']['reference']
    rspos = j['repository'][0]['variantsetId'].find('rs')
    rsid = j['repository'][0]['variantsetId'][rspos:]
    # Write the entry
    with open(vcf_filename, 'a') as v:
        # Write the metadata header
        v.write('##fileformat=VCFv4.0\n')
        v.write(('##source=' + jsonfile + '\n'))
        v.write('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n')
        # Write the variant row
        v.write('{}\t{}\t{}\t{}\t{}\t.\t.\t.'.format(chrom, pos, rsid, ref,
                                                     alt))

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
                help = 'Input JSON')
        p.add_argument(
                '-o', '--output',
                help = 'Output VCF')
        return p

    def main(self, name, opts):
        if opts.input is None:
            raise SystemExit('Must specify input JSON file with -i')
        if opts.output is None:
            raise SystemExit('Must specify output VCF file with -o')
        json2vcf(opts.input, opts.output)


if __name__ == '__main__':
    app = App()
    app.run(sys.argv)
