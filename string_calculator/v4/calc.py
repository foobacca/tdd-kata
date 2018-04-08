import re


class StringCalculator(object):
    default_delimeters = [',', '\n']

    def __init__(self, calc_input):
        self.calc_input, self.delimeters = self.extract_delimeters(calc_input)

    @classmethod
    def extract_delimeters(cls, calc_input):
        if not calc_input.startswith('//'):
            return calc_input, cls.default_delimeters
        delim_part, real_calc_input = calc_input.split('\n', 1)
        match = re.match(r'^//((?P<single>.)|\[(?P<multi>.+)\])$', delim_part)
        if not match:
            raise Exception('Bad delimeter spec')
        if match.group('single'):
            delimeter = match.group('single')
            return real_calc_input, [delimeter]
        else:
            delimeter_text = match.group('multi')
            return real_calc_input, cls.extract_multi_delimiters(delimeter_text)

    @classmethod
    def extract_multi_delimiters(cls, delimeter_text):
        assert delimeter_text[0] != '[' and delimeter_text[-1] != ']'
        return delimeter_text.split('][')

    @classmethod
    def part_to_num(cls, calc_part):
        if calc_part == '':
            return 0
        int_part = int(calc_part)
        if int_part < 0:
            raise Exception('no negative numbers')
        if int_part > 1000:
            return 0
        return int_part

    def find_next_delimeter(self, delimeter, index):
        end_index = self.calc_input.find(delimeter, index)
        if end_index == -1:
            end_index = len(self.calc_input)
        return end_index, len(delimeter)

    def find_next_end_length(self, index):
        next_end_lengths = [self.find_next_delimeter(d, index) for d in self.delimeters]
        end_length = next_end_lengths[0]
        for new_end_length in next_end_lengths[1:]:
            if new_end_length[0] < end_length[0]:
                end_length = new_end_length
        return end_length

    def to_parts(self):
        index = 0
        while index < len(self.calc_input):
            end, delim_length = self.find_next_end_length(index)
            yield self.calc_input[index:end]
            index = end + delim_length

    def calc(self):
        return sum(self.part_to_num(p) for p in self.to_parts())


def calc(calc_input):
    return StringCalculator(calc_input).calc()
