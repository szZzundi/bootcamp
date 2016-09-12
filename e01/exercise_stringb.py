#Exercise 1.3b Using String Methods using no for loops

def complement_base(base, material='DNA'):
    """Return the Watson-Crick complement of a base"""

    if base in 'Aa':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
    elif base in 'TtUu':
        return 'A'
    elif base in 'Cc':
        return 'G'
    else:
        return 'C'

#Reverse sequence
reverse_compplement(seq, material='DNA')

seq_ref = seq[::-1]:

#Replace sequence with non-nucleotide
if material == 'DNA'
    seq_ref1 = seq_ref.replace('A', 'S')
    seq_ref2 = seq_ref1.replace('C', 'D')
    seq_ref3 = seq_ref2.replace('G', 'F')
    seq_ref4 = seq_ref3.replace('T', 'G')

#Replace sequence with nucleotides
        seq_ref5 = seq_ref4.replace('S', 'T')
        seq_ref6 = seq_ref5.replace('D', 'G')
        seq_ref7 = seq_ref6.replace('F', 'C')
        seq_ref8 = seq_ref7.replace('G', 'A')

elif
    seq_ref1 = seq_ref.replace('A', 'S')
    seq_ref2 = seq_ref1.replace('C', 'D')
    seq_ref3 = seq_ref2.replace('G', 'F')
    seq_ref4 = seq_ref3.replace('T', 'H')

#Replace sequence with nucleotides
        seq_ref5 = seq_ref4.replace('S', 'U')
        seq_ref6 = seq_ref5.replace('D', 'G')
        seq_ref7 = seq_ref6.replace('F', 'C')
        seq_ref8 = seq_ref7.replace('H', 'A')

print(seq_ref8)
