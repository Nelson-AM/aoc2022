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


''' 
A = rock, B = paper, C = scissors
X = rock, Y = paper, Z = scissors
Rock beats scissors
Paper beats rock
Scissors beat paper
'''


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


if __name__ == '__main__':
    file_list = load_file_as_list('input_day_2')

    total_score = 0
    for line in file_list:
        shape = line.split()[1]
        shape_score = calculate_shape_score(shape)
        round_score = calculate_round_score(line)

        total_score += shape_score + round_score
    print_output(answer_one=total_score)
