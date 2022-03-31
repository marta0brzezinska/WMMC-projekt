def int_to_list(inp):
    ''' convert int to list of bits '''
    result = [0]*64
    i = 63
    while inp > 0:
        result[i] = inp % 2
        inp = inp >> 1
        i = i-1
    return result


def list_to_int(inp):
    ''' convert list of bits to int '''
    result = 0
    for i in range(64):
        result = (result << 1) + inp[i]
    return result


def int_to_blocks(inp):
    ''' convert int to list of 8-bit blocks '''
    blocks = [0]*8
    i = 7
    while inp > 0:
        temp = inp >> 8
        blocks[i] = inp - (temp << 8)
        inp = inp >> 8
        i = i-1
    return blocks


def blocks_to_int(inp):
    ''' convert list of 8-bit blocks to int '''
    result = 0
    for i in inp:
        result += i
        result = result << 8
    result = result >> 8
    return result
    
    