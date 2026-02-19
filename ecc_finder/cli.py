#!/usr/bin/env python3

"""
# June 2021
# If using this pipeline please cite : XXXXXXXXXX
#--------------------------------------------------------------------------+
#
#	ecc_finder is a tool
#       to detect eccDNA using Illumina and ONT sequencing.
#
#--------------------------------------------------------------------------+
#
#	AUTHOR: panpan ZHANG
#	CONTACT: njaupanpan@gmail.com
#
#	LICENSE:
# 	GNU General Public License, Version 3
#	http://www.gnu.org/licenses/gpl.html
#
#	VERSION: 1.0.0
#
#--------------------------------------------------------------------------+
"""

import sys
from ecc_finder.eccFinder_lib.utilities import get_eccFinder_version

def main():
    VERSION = get_eccFinder_version()
    CITATION = """
Zhang et al. "Ecc_finder: a robust and accurate tool for detecting extrachromosomal circular DNA (eccDNA) from sequencing data"
    """

    description = """
ecc_Finder: Tool for detecting eccDNA loci using Illumina and ONT sequencing.
Version: %s

usage: ecc_finder <command> [options]

    Mapping mode:
      map-sr         Call candidate eccDNA loci from paired-end short reads
      map-ont        Call candidate eccDNA loci from Nanopore long reads

    Assembly mode:
      asm-sr         Assembly from paired-end short reads
      asm-ont        Assembly from Nanopore long reads

    options:
      -v, --version""" % VERSION

    arg_len = len(sys.argv)

    if arg_len == 1:
        print(description)

    if arg_len > 1:
        cmd = sys.argv[1]

        if cmd == "-h" or cmd == "--help":
            print(description)

        elif cmd == "-v" or cmd == "--version":
            print(VERSION)

        elif cmd == "map-sr":
            sys.argv = sys.argv[:1] + sys.argv[2:]
            from ecc_finder.map_sr import main as map_sr_main
            map_sr_main()

        elif cmd == "map-ont":
            sys.argv = sys.argv[:1] + sys.argv[2:]
            from ecc_finder.map_ont import main as map_ont_main
            map_ont_main()

        elif cmd == "asm-sr":
            sys.argv = sys.argv[:1] + sys.argv[2:]
            from ecc_finder.asm_sr import main as asm_sr_main
            asm_sr_main()

        elif cmd == "asm-ont":
            sys.argv = sys.argv[:1] + sys.argv[2:]
            from ecc_finder.asm_ont import main as asm_ont_main
            asm_ont_main()

        else:
            print(description)
            print("\n** unrecognized command: %s **" % cmd)

if __name__ == "__main__":
    main()
