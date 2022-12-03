from util import load_file_as_list, print_output

if __name__ == '__main__':
    file_list = load_file_as_list('input_day_1')

    calories_per_elf = []
    calories_carried = 0
    for line in file_list:
        if len(line) > 0:
            calories_carried += int(line)
        else:
            calories_per_elf.append(calories_carried)
            calories_carried = 0

    max_calories = max(calories_per_elf)

    print_output(max_calories,
                 sum(calories_per_elf[-3:]))
