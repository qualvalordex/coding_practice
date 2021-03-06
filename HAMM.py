#ROSALIND BIOINFORMATICS PROBLEMS
#http://rosalind.info/problems/hamm/

def hamming_distance(dna_sequence_1, dna_sequence_2):
    if len(dna_sequence_1) == len(dna_sequence_2):
        count_mismatches = 0
        for position in range (len(dna_sequence_1)):
            if dna_sequence_1[position] != dna_sequence_2[position]:
                count_mismatches += 1
        return count_mismatches
    else:
        print('It is not possible to calculate Hamming Distance for different DNA length.')

# seq1 = 'GAGCCTACTAACGGGAT'
# seq2 = 'CATCGTAATGACGGCCT'
# print(hamming_distance(seq1, seq2))
# LOGS 7

seq1 = 'TATTAGGCACATTAGAGGATCTATTGTATTACACCTTTCCAGTGGACCTCCGCCCTCCAGGAGACTCGCCAGTTGTCTGTTGCGGACCGCACGGGAGGAACCAGCATTGAGGGCACGTGGGCTTGAGCGTCGCCAGCCGAAATATACCAATAGCCCCCCGTGCGAGCAAGCGGGGACACGCAGGCACGAGTAGTCAACCGTTCTCCTGCGGGGTCACGACACCCTGTGCTAGCCAGCAAACGACGAGGTCGCTCGAAGAATTTGGGCTTATAGTCAATGGTTATTAAAAAATGTTTCGTGGACTACATCACCTCTAACGACTGTGTACTTGTTTACCAGCGCACTTAAGCTAATACACGGGTGCCTGCGTTGCAGAGCGCGCTCGTCTTATATAAAGAAAGACTCTTTTCTCAAACACGGTTCTGTCTACGCCTAGGGCGTCCCCGTTGTGTCCTCAACCGTGCAGGGTTACGGCTGTTTCTCCATCTTGGTAGCACTTTCTTATGGCCCTATAAGGGGGTCCCCAAAGCTCGTCGGGGATACTTGCGTCGCGATAATAGAGACCGCGAGAATCTGTACAGCCCCGGAGTAGTTGTTGATTCCACACCTGTAAGGCACTGGGGCAGGGTCAAGAAGTTACTGGACGCCCAGGACCGCGATTACTGCAGGAGCCGTTAATCGGTTACTATGGCCCCGGGCGCGGAGGCGCGGAGGCTGCGACGGCAGTACCCTCCCTTGGACCCGCGCTCTTCACAGCTATCGAACAACTGTTAAACGTGAGGTCTCGTCCAGAGCGGCGATCCCCTCCAATAGTGGACAAAACACGGGCTCACGTCCCTCAGATATCCACCAAGGAGCTGGATAGAGGTTATCAGATGGCCAAGGGGCACGGGAGAGGTCTGTGAACGCTGCCCGAAAACATTCCCGTCGTCG'
seq2 = 'GATTAGTACAAAATCCCAAGGTATTGTGTCACAAGCCGATAGACGAATACCGCCTCCCACAAGTGTCGCCCTTTTCCAGTCGTATGGGAATAGCGATTTCCGGCCATAAGGAGTACACGGGCTTCGCAGTGGGCTGCCTTCACTTATCGTAGGCCCCTCGTGCATGCAAGGGCGGCCAAGCCATGTGGAGTTGTCGATCGTTCCATTAGGGGTTCCCGACCCCCTATGACAGACACTGAACGACGTGGTTTGCCTACAAGATTGGGATAGTAGTCCCAAGTTGAACGCTGGTGATTCGCGCACTTCTGCAAGGCGAACGACAGTGTTCTTGTAGTCGTGCACATAGTTTCAAGCTAAGAGGAGCCAGGTTGGTTCAAAGTTACCGGACTCTGTGGGCAGTTACTACTCGTATGGGTACGGTAGGGAACTCTCCCAGGGCGGAACCATTGTCCACTAACCACCGGGAGCTTCGGCCCACTATACCGGCGCATGAGAAATGACGAATGACGCTCGTGGGGTGACTCGATGCCCCATAAGTGCTCTTCAGGTAATGCGAGTATTGATGCGGACATAAAGTAACTCCACCTAGTATTCGTCGCGGCTAGGTCTGTTTGGCTTTGTGCTAGGGTGCTAGAGCCACTTAACAACCAGGCAAGAGCTGGAGGCCGACGACGCTTGTTGGTCAGCATGCCCCCTTGAACGGGGGCAAGCGCTTATCGTCGGCAGTCACGTACGGAGGCCCAGCGCTTCTGCCTGAGAGTGATAACACCTAAACAGGTAAGTGGCCTCAGGCGCGACGAGCGACTTCACGGGCGATGTGTGTTAGGGCTCACGTACGACATCTTGCGCTCAATGTAGTCGGTTAATGTAGTCAGGTAGGCACGAGCGAAAGGGGAATCATAGAAGCCCTGCCCGGAAACGTTGGGGTCGTCA'
print(hamming_distance(seq1, seq2))
# LOGS 466