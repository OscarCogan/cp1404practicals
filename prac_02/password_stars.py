"""Module docstring"""

def main():
    """Function docstring"""
    minimum_length = 3
    password = get_password(minimum_length)
    print_asterisks(password)

def print_asterisks(password):
    for i in range(0, len(password)):
        print("*", end="")


def get_password(minimum_length):
    password = input("Enter a password: ")
    while len(password) < minimum_length:
        print("Error. Password is shorter than the minimum length.")
        password = input("Enter a password: ")
    return password

main()

