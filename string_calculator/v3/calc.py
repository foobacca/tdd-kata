import re


class StringCalculator(object):
    simple_delim_re = re.compile(r'^//(.)$')
    multi_char_delim_re = re.compile(r'^//\[(.+)\]$')

    def __init__(self, calc_input):
        if calc_input.startswith('//'):
            delim_spec, self.calc_input = calc_input.split('\n', 1)
            self.delimiters = self.parse_delim_spec(delim_spec)
        else:
            self.calc_input = calc_input
            self.delimiters = [',', '\n']

    @classmethod
    def parse_delim_spec(cls, delim_spec):
        simple_match = cls.simple_delim_re.match(delim_spec)
        if simple_match:
            return [simple_match.group(1)]
        multi_char_match = cls.multi_char_delim_re.match(delim_spec)
        if multi_char_match:
            return [multi_char_match.group(1)]
        raise Exception('Could not parse delimiter specification')

    @classmethod
    def find_next_delim(cls, calc_input, delim, current_index):
        next_index = calc_input.find(delim, current_index)
        if next_index == -1:
            next_index = len(calc_input)
        return next_index, len(delim)

    def find_next_break(self, calc_input, current_index):
        delim_indexes = [self.find_next_delim(calc_input, d, current_index) for d in self.delimiters]
        return min(delim_indexes, key=lambda d: d[0])

    def to_parts(self, calc_input):
        current_index = 0
        while current_index < len(calc_input):
            next_delim_index, len_delim = self.find_next_break(calc_input, current_index)
            yield calc_input[current_index:next_delim_index]
            current_index = next_delim_index + len_delim
        yield calc_input[current_index:]

    @classmethod
    def to_int(cls, part):
        if part == '':
            return 0
        int_part = int(part)
        if int_part < 0:
            raise Exception('no negatives!')
        if int_part > 1000:
            int_part = 0
        return int_part

    def calculate(self):
        return sum(self.to_int(num) for num in self.to_parts(self.calc_input))


def calculator(calc_input):
    return StringCalculator(calc_input).calculate()
