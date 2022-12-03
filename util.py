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


def print_output(answer_one=None, answer_two=None):
    print(
        f"Answer I  = {answer_one}" + f", Answer II = "f""
                                      f"{answer_two}")
