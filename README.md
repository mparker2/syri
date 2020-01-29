## Pre-requisite:
1. Python3.5 and the following packages: Cython, numpy, scipy, pandas, python-igraph, biopython, psutil, and pysam
2. C/C++ compiler: g++ 

## Installation:
Download/clone the repository, open the folder and run:

`python setup.py install`

This will install the cython modules.

## Running:
Executables will be in `syri/bin/` folder and can be run directly from the terminal.

Detailed information is available at: https://schneebergerlab.github.io/syri

## Citation:
Please cite:

`Goel, M., Sun, H., Jiao, W. et al. SyRI: finding genomic rearrangements and local sequence differences from whole-genome assemblies. Genome Biol 20, 277 (2019) doi:10.1186/s13059-019-1911-0`

## Current Limitations:
1. The homologous chromosomes in the two genomes need to represent the same strand. If the chromosomes are from the different strands, then the alignments between these chromosomes would be inverted. As SyRI only checks directed alignments for syntenic region identification, it would not be able to find syntenic regions and consequently rearranged regions. And might result in SyRI crashing.  
Current solution to the problem is to manually check alignments. If the majority of alignments between homologous chromosomes are inverted, then the chromosome in the query genome needs to be reverse-complemented. Then new alignment need to be generated using this corerctly oriented genome assembly. We are working on a method which can generate dot plots to automatically identify and reverser-complement the inverted-chromosomes.

2. Large translocations and duplications (consisting of multiple alignments) can result in high memory-usage and CPU runtime.
