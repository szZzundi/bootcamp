"""Convert DNA to RNA"""

def rna(seq):
    """
    Convert a DNA sequence to RNA.
    """

    #Conver to uppercase
    seq = seq.upper()

    return seq.replace('T', 'U')
    
