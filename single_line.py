with open ('data/salmonella_spi1_region.fna', 'r') as f, open('single_line.txt', 'w') as f_out:

    #Get all the lines
    lines = f.readlines()

    #Remove gaps
    for line in lines:
        line.rstrip()
        if not line.startswith('>'):
            f_out.write(line.rstrip())
