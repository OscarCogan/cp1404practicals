def main():
    filename = input("Enter filename: ")
    while filename != "":
        total_lines = 0
        is_finished = False
        try:
            with open(filename) as in_file:
                total_lines = count_file_lines(in_file, total_lines)
                print(f"{filename} has {total_lines} lines.")
        except FileNotFoundError:
            print(f"ERROR: {filename} not found")
        filename = input("Enter filename: ")


def count_file_lines(in_file, total_lines):
    for line in in_file:
        total_lines += 1
    return total_lines


main()