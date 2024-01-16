from input import data


def parse_input(string):
    return [list(map(int, line.split())) for line in string.split('\n')]


def calc_diff(seq):
    diffs = []
    for i in range(len(seq) - 1):
        diffs.append(seq[i+1] - seq[i])

    return diffs


def extrapolated_value(seq, prev=False):
    lists = [seq]
    values = seq
    while not all(s == 0 for s in values):
        new_list = calc_diff(values)
        lists.append(new_list)
        values = new_list

    extrapolation = 0
    for i in range(len(lists) - 1, 0, -1):
        if prev:
            extrapolation = lists[i - 1][0] - lists[i][0]
            lists[i - 1].insert(0, extrapolation)
        else:
            extrapolation = lists[i][-1] + lists[i - 1][-1]
            lists[i - 1].append(extrapolation)

    return extrapolation


def extrapolations_sum(string):
    lines = parse_input(string)
    missing_numbers = []
    prev_missing_numbers = []

    for line in lines:
        missing_numbers.append(extrapolated_value(line))
        prev_missing_numbers.append(extrapolated_value(line, True))

    print('Part 1: ' + str(sum(missing_numbers)))
    print('Part 2: ' + str(sum(prev_missing_numbers)))


if __name__ == '__main__':
    extrapolations_sum(data)
