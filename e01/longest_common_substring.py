#Define strings
def LCS(seq1, seq2):

#Initiate empty string
    answer = ''

#Compare ranges of the different sequences
    len1 = len(seq1)
    len2 = len(seq2)

    for i in range(len1):
        match = ''
        for j in range(len2):
            if (i + j < len1 and seq1[i + j] == seq2[j]):
                match += seq2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ''
    return answer
