from util import load_file_as_list, print_output


def split_contents_of_rucksack(rucksack):
    chunk_length = int(len(rucksack) / 2)
    return [rucksack[i:i + chunk_length] for i in
            range(0, len(rucksack), chunk_length)]


def find_double_items(split_contents):
    # Find letters that appear in both parts of split_contents
    double_items = ''
    for item in split_contents[0]:
        if item in split_contents[1] and item not in double_items:
            double_items += item
    return double_items


def calculate_priority(double_items):
    # return [ord(char) - 96 for char in double_items]
    priority = 0
    for char in double_items:
        if char.isupper():
            priority += ord(char) - 38
        if char.islower():
            priority += ord(char) - 96
    return priority


def puzzle_one(file_list):
    global total_priority
    total_priority = 0
    for rucksack in file_list:
        split_contents = split_contents_of_rucksack(rucksack)
        double_items = find_double_items(split_contents)
        total_priority += calculate_priority(double_items)
    return total_priority


def split_list_by(file_list, step_size=3):
    return [file_list[idx:idx+step_size] for idx in range(0, len(file_list), step_size)]


def find_common_item(triplet):
    common_item = ''
    for char in triplet[0]:
        if char in triplet[1] and char in triplet[2]:
            common_item += char
            break
    return common_item


def puzzle_two(file_list):
    badge_priority = 0
    triplets = split_list_by(file_list)
    for triplet in triplets:
        common_item = find_common_item(triplet)
        badge_priority += calculate_priority(common_item)
    return badge_priority


if __name__ == '__main__':
    file_list = load_file_as_list('input/input_day_3')

    total_priority = puzzle_one(file_list)
    badge_priority = puzzle_two(file_list)

    print_output(answer_one=total_priority,
                 answer_two=badge_priority)
