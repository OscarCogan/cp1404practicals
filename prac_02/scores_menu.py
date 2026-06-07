"""
CP1404 - Practical 2
Program to run menu relating to scores
"""

def main():
    score = int(input("Enter score: "))
    score = determine_valid_score(score)
    menu = """G - Get Score
    P - Print Result
    S - Show Stars
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter score: "))
            score = determine_valid_score(score)
        elif choice == "P":
            parameter = return_parameter(score)
            print(f"User score {score} is {parameter}")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Goodbye for now.")


def determine_valid_score(score):
    while score < 0 or score > 100:
        print("An invalid score has been entered. Please try again.")
        score = int(input("Enter score: "))
    return score


def return_parameter(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_stars(score):
    for i in range(0, score):
        print("*", end="")

main()
