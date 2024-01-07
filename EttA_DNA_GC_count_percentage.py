#Finding out the percentage of GC count from the DNA sequence using Python

dnaseq = '''GTGGCTCAATTCGTTTATACCATGCATCGTGTCGGCAAAGTTGTTCCGCCGAAACGTCATATTTTGAAAA
ACATCTCTCTGAGTTTCTTCCCTGGGGCAAAAATTGGTGTCCTGGGTCTGAATGGCGCGGGTAAGTCCAC
CCTGCTGCGCATTATGGCGGGCATTGATAAAGACATCGAAGGTGAAGCGCGTCCGCAGCCAGACATCAAG
ATTGGTTATCTGCCGCAGGAACCGCAGCTGAACCCGGAACACACCGTGCGTGAGTCCATTGAAGAAGCGG
TTTCAGAAGTGGTTAACGCCCTGAAACGCCTGGATGAAGTGTATGCGCTGTACGCCGATCCGGATGCCGA
TTTTGACAAGCTGGCCGCTGAACAAGGCCGTCTGGAAGAGATCATTCAGGCTCACGACGGTCATAATCTG
AACGTACAGCTGGAGCGTGCGGCGGATGCGCTACGTCTGCCGGACTGGGACGCGAAAATCGCTAACCTCT
CCGGTGGTGAACGTCGTCGCGTAGCGTTGTGCCGCCTGCTGCTGGAAAAACCAGACATGCTGCTGCTCGA
CGAACCGACCAACCACCTGGATGCCGAATCCGTGGCCTGGCTGGAACGCTTCCTGCACGACTTCGAAGGC
ACCGTTGTGGCGATTACCCACGACCGTTACTTCCTCGATAACGTTGCAGGCTGGATCCTCGAACTTGACC
GCGGTGAAGGTATTCCGTGGGAAGGTAACTACTCCTCCTGGCTGGAGCAGAAAGATCAGCGCCTGGCGCA
GGAAGCTTCACAAGAAGCGGCGCGTCGTAAGTCGATTGAGAAAGAGCTGGAATGGGTACGTCAAGGTACT
AAAGGCCGTCAGTCGAAAGGTAAAGCACGTCTGGCGCGCTTTGAAGAACTGAACAGCACCGAATATCAGA
AACGTAACGAAACCAACGAACTGTTTATTCCACCTGGACCGCGTCTGGGCGATAAAGTGCTGGAAGTCAG
CAACCTGCGTAAATCCTATGGCGATCGTCTGCTGATTGATGACCTGAGCTTCTCGATCCCGAAAGGAGCG
ATCGTCGGGATCATCGGTCCGAACGGTGCGGGTAAATCGACCCTGTTCCGTATGATCTCTGGTCAGGAAC
AGCCGGACAGCGGCACCATCACTTTGGGTGAAACGGTGAAACTGGCGTCGGTTGATCAGTTCCGTGACTC
AATGGATAACAGCAAAACCGTTTGGGAAGAAGTTTCCGGCGGGCTGGATATCATGAAGATCGGCAACACC
GAGATGCCAAGCCGCGCCTACGTTGGCCGCTTTAACTTTAAAGGGGTTGATCAGGGTAAACGCGTTGGTG
AACTCTCCGGTGGTGAGCGCGGTCGTCTGCATCTGGCGAAGCTGCTGCAGGTTGGCGGCAACATGCTGCT
GCTCGACGAACCAACCAACGACCTGGATATCGAAACCCTGCGCGCGCTGGAAAACGCCCTGCTGGAGTTC
CCGGGCTGTGCGATGGTTATCTCGCACGACCGTTGGTTCCTCGACCGTATCGCCACGCACATTCTGGATT
ACCAGGATGAAGGTAAAGTTGAGTTCTTCGAAGGTAACTTTACCGAGTACGAAGAGTACAAGAAACGCAC
GCTGGGCGCAGACGCGCTGGAGCCGAAGCGTATCAAGTACAAGCGTATTGCGAAGTAA'''

# ((G+C)/total nucleotide)*100

G_count = dnaseq.count("G")
C_count = dnaseq.count("C")

Total_GC = G_count + C_count

Total_nucleotide = len(dnaseq)

GC_Percentage = (Total_GC/Total_nucleotide)*100

print(round(GC_Percentage, 2))
