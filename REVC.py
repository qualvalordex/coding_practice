#ROSALIND BIOINFORMATICS PROBLEMS
#http://rosalind.info/problems/revc/

def reverse_complement(dna_sequence):
    splited_sequence = list(dna_sequence)
    for position, nucleotide in enumerate(splited_sequence):
        if nucleotide == 'A':
            splited_sequence[position] = 'T'
        if nucleotide == 'T':
            splited_sequence[position] = 'A'
        if nucleotide == 'C':
            splited_sequence[position] = 'G'
        if nucleotide == 'G':
            splited_sequence[position] = 'C'
    
    result = "".join(splited_sequence)
    
    return result[::-1]

print(reverse_complement('GGTTCGATGTACAGGGCATGGAGTAGGGTTAAAGGAAACTGGGTCTTGCGTCCATGGGATCATTCATAGGCCGAAGTACTAATAGACGGTCACTATGGGGTCTTCCTCGAATCACTCGCGGCCATGCGTTCAACGGTATAACTCAGGCATAACTCCTTAACTGTAGCTCGGAACATATGAGTACCCATCTTGATATTGACACCCGCACAGCTTAGAGAGGACCGCCCGCAGGGCAGCTCACATAGTAGAACCGACCTACTGGCTCCGAGAGTTAAGGGCACCCTGCAATAGTCTCCTCTGCACTGTACGAGACGGGAGAATCACATGGGTATATACAGGGCGATGCGGAGTCTTTGCAGTACTCGGCGTGAGGCTTCGAACATTTTAAGTAGCAGTCGCGTCATACCCCTTACACACGGGGTCCATCTCGCTATCCTGCCCATGCGGTCGTCGCAACCCAATTTTCTTATGCACTGTTTAAAGAAGAGTGCTACGTAAAACCGTCTGGATTACCGGTATGCGAGACTGCTGACCTCCACGCTCTATCCGTATCCATGTATCTAAAAAGTCTCGTTCGTAGTGCAGCGGCGGCGCACCGATGAGGATGATTCAGAGACACTCTTACCGTGTCTCACGTAAGGGAATCGTGGCCGCCGGGGCTTTTGATCCGAGGAACCATGAAATTTCCCTACACCATGTAGACGAACGTTGCCAGCTACAGTCCACCGGGTTGGACACTCTCACTCCTTAGAAACGAACTGTCGTCGGTGCCACACAGTGATATTTGAGATAACCCGAACAGCTCCTCGAGATTCTGTTTTTAATTGTTTGAG'))
#LOGS CTCAAACAATTAAAAACAGAATCTCGAGGAGCTGTTCGGGTTATCTCAAATATCACTGTGTGGCACCGACGACAGTTCGTTTCTAAGGAGTGAGAGTGTCCAACCCGGTGGACTGTAGCTGGCAACGTTCGTCTACATGGTGTAGGGAAATTTCATGGTTCCTCGGATCAAAAGCCCCGGCGGCCACGATTCCCTTACGTGAGACACGGTAAGAGTGTCTCTGAATCATCCTCATCGGTGCGCCGCCGCTGCACTACGAACGAGACTTTTTAGATACATGGATACGGATAGAGCGTGGAGGTCAGCAGTCTCGCATACCGGTAATCCAGACGGTTTTACGTAGCACTCTTCTTTAAACAGTGCATAAGAAAATTGGGTTGCGACGACCGCATGGGCAGGATAGCGAGATGGACCCCGTGTGTAAGGGGTATGACGCGACTGCTACTTAAAATGTTCGAAGCCTCACGCCGAGTACTGCAAAGACTCCGCATCGCCCTGTATATACCCATGTGATTCTCCCGTCTCGTACAGTGCAGAGGAGACTATTGCAGGGTGCCCTTAACTCTCGGAGCCAGTAGGTCGGTTCTACTATGTGAGCTGCCCTGCGGGCGGTCCTCTCTAAGCTGTGCGGGTGTCAATATCAAGATGGGTACTCATATGTTCCGAGCTACAGTTAAGGAGTTATGCCTGAGTTATACCGTTGAACGCATGGCCGCGAGTGATTCGAGGAAGACCCCATAGTGACCGTCTATTAGTACTTCGGCCTATGAATGATCCCATGGACGCAAGACCCAGTTTCCTTTAACCCTACTCCATGCCCTGTACATCGAACC