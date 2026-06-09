"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError will occur if the numerator or the denominator are not valid integers (entering Test or 19.5 will cause this)
2. When will a ZeroDivisionError occur?
    A ZeroDivisionError will occur when and onl when the denominator is zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    The code could be altered to avoid the possibility of a ZeroDivisionError
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("ZeroDivisionError message")
print("Finished.")