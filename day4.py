from util import load_file_as_list, print_output


def convert_file_list_to_sets(file_list):

    new_list = []
    for row in file_list:
        new_row = []
        split_row = row.split(',')

        set_one = [int(i) for i in split_row[0].split('-')]
        set_two = [int(i) for i in split_row[1].split('-')]

        new_row.append({i for i in range(min(set_one), max(set_one) + 1)})
        new_row.append({i for i in range(min(set_two), max(set_two) + 1)})
        new_list.append(new_row)
    return new_list


def puzzle_one(file_list):
    list_with_sets = convert_file_list_to_sets(file_list)

    contained_pairs = 0
    for pair in list_with_sets:
        print(f'pair_one: {pair[0]}, pair_two: {pair[1]}')
        if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]):
            print('subset detected!')
            contained_pairs += 1
    return contained_pairs


if __name__ == '__main__':
    file_list = load_file_as_list('input/input_day_4')
    answer_one = puzzle_one(file_list)

    print_output(answer_one=answer_one)
