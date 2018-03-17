def to_int(calc_part):
    if calc_part == '':
        return 0
    else:
        int_part = int(calc_part)
        if int_part < 0:
            raise Exception('we do not deal with negative numbers')
        return int_part


def get_split_char(calc_input):
    for char in ',\n':
        if char in calc_input:
            return char
    return ','


def get_parts(calc_input):
    part = []
    for char in calc_input:
        if char.isdigit() or char == '-':
            part.append(char)
        else:
            yield ''.join(part)
            part = []
    yield ''.join(part)


def calculator(calc_input):
    return sum(to_int(p) for p in get_parts(calc_input))
