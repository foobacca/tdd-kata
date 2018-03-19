class StringCalculator(object):

    def __init__(self, calc_input):
        if calc_input.startswith('//'):
            delimiter_part, self.calc_input = calc_input.split('\n', 1)
            self.delimiters = delimiter_part[2]
        else:
            self.calc_input = calc_input
            self.delimiters = ',\n'

    @classmethod
    def to_int(cls, part):
        if part == '':
            return 0
        else:
            return int(part)

    @classmethod
    def get_int(cls, part):
        int_part = cls.to_int(part)
        if int_part < 0:
            raise Exception('No negatives allowed')
        if int_part > 1000:
            int_part = 0
        return int_part

    def split_input(self, calc_input):
        part = []
        for char in calc_input:
            if char in self.delimiters:
                yield ''.join(part)
                part = []
            else:
                part.append(char)
        yield ''.join(part)

    def calculate(self):
        return sum(self.get_int(n) for n in self.split_input(self.calc_input))


def calculator(calc_input):
    return StringCalculator(calc_input).calculate()
