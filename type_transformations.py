def int_to_list(input):
    #TODO: poprawić kod (bytes->list)
    input = input

    l = len(input) * 8
    result = [0] * l
    pos = 0
    for ch in input:
        i = 7
        while i >= 0:
            if ch & (1 << i) != 0:
                result[pos] = 1
            else:
                result[pos] = 0
            pos += 1
            i -= 1
    return result


def list_to_int(input):
    #TODO: poprawić kod (list->bytes)
    result = []
    pos = 0
    c = 0
    while pos < len(input):
        c += input[pos] << (7 - (pos % 8))
        if (pos % 8) == 7:
            result.append(c)
            c = 0
        pos += 1
    return bytes(result)