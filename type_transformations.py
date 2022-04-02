def int_to_list(inp):
    """
    Converts given int value to a list of bits of the length 64.

    :param inp: int value to be converted
    :return: list of bits
    """
    result = [0]*64
    i = 63
    while inp > 0:
        result[i] = inp % 2
        inp = inp >> 1
        i = i-1
    return result


def list_to_int(inp):
    """
    Converts given list of bits of the length 64 to an int value.

    :param inp: list of bits to be converted
    :return: int value
    """
    result = 0
    for i in range(64):
        result = (result << 1) + inp[i]
    return result


def int_to_blocks(input,block_nr,block_size):
    """
    Splits int value into given number of blocks of the given bit length.

    :param input: int value to be split
    :param block_nr: number of blocks for the input to be split into
    :param block_size: size of an individual block
    :return: list of int values representing blocks
    """
    blocks = [0]*block_nr
    i = block_nr - 1
    while input > 0:
        temp = input >> block_size
        blocks[i] = input - (temp << block_size)
        input = input >> block_size
        i -= 1
    return blocks


def blocks_to_int(input, block_size):
    """
    Converts list of int values representing blocks of a given bit size to an int value.

    :param input: list of blocks
    :param block_size: size of an individual block
    :return: int value
    """
    result = 0
    for i in input:
        result += i
        result = result << block_size
    result = result >> block_size
    return result
    
    