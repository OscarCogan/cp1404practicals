"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random
def main():
    score = float(input("Enter score: "))
    parameter = return_parameter(score)
    print(f"User score {score} is {parameter}")
    if parameter == "Excellent":
        print("You get a prize!")

    score = random.randint(0, 100)
    parameter = return_parameter(score)
    print(f"Random: {score} = {parameter}")

def return_parameter(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()