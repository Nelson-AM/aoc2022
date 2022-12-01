# Reused from 2018
def load_file_as_list(filename, to_int=None):
    list_from_file = []
    with open(filename) as file:
        for line in file:
            line = line.strip("\n")
            if to_int and line is not '':
                list_from_file.append(int(line))
            else:
                list_from_file.append(line)
    return list_from_file


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

    print(max_calories)

    calories_per_elf.sort()

    print(calories_per_elf[:3])
    print(calories_per_elf[-3:])

    print(sum(calories_per_elf[-3:]))