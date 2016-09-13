#Function divides sequence into blocks

#Define function
def gc_blocks(seq, block_size):

    my_gc = list()

    #Split sequence
    for i in range(0, len(seq), block_size):
        block = seq[i: i+block_size]
        if len(block) < block_size:
            break

        #Count GC content
        my_gc.append((block.count('C') + block.count('G'))/ block_size)
    return tuple(my_gc)
