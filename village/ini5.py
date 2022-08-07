with open('data/INI5.in', 'r') as fi, open('data/INI5.out', 'w+') as fo:
    i = 1
    for line in fi:
        if i % 2 == 0: 
            fo.write(line)
        i += 1