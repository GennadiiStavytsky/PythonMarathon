def list_maker(line, delim):
    if delim == '':
        delim = ' '
    return line.split(delim)
