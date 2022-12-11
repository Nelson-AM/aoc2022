from util import load_file_as_list, print_output


def calculate_shape_score(shape):
    """

    :param shape: X = rock, Y = paper, Z = scissors
    :return:
    """
    if shape is 'X':
        return 1
    if shape is 'Y':
        return 2
    if shape is 'Z':
        return 3
    print(f'Impossible shape detected: {shape}.')
    return 0


def calculate_round_score(round):
    loss = ['A Z', 'B X', 'C Y']
    draw = ['A X', 'B Y', 'C Z']
    win = ['A Y', 'B Z', 'C X']

    if round in loss:
        return 0
    if round in draw:
        return 3
    if round in win:
        return 6
    print(f'Impossible round detected: {round}')
    return 0


def calculate_round_score_puzzle_two(round):
    if 'X' in round:
        return 0
    if 'Y' in round:
        return 3
    if 'Z' in round:
        return 6
    print(f'Impossible round detected: {round}')
    return 0


def determine_shape(line):
    if 'X' in line:
        # loss
        if 'A' in line:
            return 'Z'
        if 'B' in line:
            return 'X'
        if 'C' in line:
            return 'Y'
    if 'Y' in line:
        # draw
        if 'A' in line:
            return 'X'
        if 'B' in line:
            return 'Y'
        if 'C' in line:
            return 'Z'
    if 'Z' in line:
        # win
        if 'A' in line:
            return 'Y'
        if 'B' in line:
            return 'Z'
        if 'C' in line:
            return 'X'
    print(f'Impossible line detected: {line}')
    return 0


def calculate_total_score(list_of_rounds):
    running_score = 0
    for line in list_of_rounds:
        shape = line.split()[1]
        shape_score = calculate_shape_score(shape)
        round_score = calculate_round_score(line)

        running_score += shape_score + round_score
    return running_score


def calculate_score_puzzle_two(list_of_rounds):
    running_score = 0
    for line in list_of_rounds:
        shape = determine_shape(line)
        shape_score = calculate_shape_score(shape)
        round_score = calculate_round_score_puzzle_two(line)

        running_score += shape_score + round_score
    return running_score


if __name__ == '__main__':
    file_list = load_file_as_list('input/input_day_2')

    total_score = calculate_total_score(file_list)
    updated_score = calculate_score_puzzle_two(file_list)
    print_output(answer_one=total_score,
                 answer_two=updated_score)
