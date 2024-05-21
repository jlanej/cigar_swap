# swap the cigar string from one bam file to another bam file
import pysam
import sys


if __name__ == '__main__':
    # takes two bam files and swaps the cigar string from one to the other
    # this is useful for comparing the alignment of two different aligners
    # the first file is the source of the cigar string
    # the second file is the target of the cigar string
    # the output is the second file with the cigar string from the first file
    # the output is written to stdout

    source = pysam.AlignmentFile(sys.argv[1], "rb")
    target = pysam.AlignmentFile(sys.argv[2], "rb")
    for s, t in zip(source, target):
        t.cigar = s.cigar
        print(t.to_string())
