# 1:
name = input("Enter a name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2:
in_file = open("name.txt")
name = in_file.read()
in_file.close()
print(f"Hi {name.strip()}!")

# 3:
sum_of_numbers = 0
with open("numbers.txt") as in_file:
    numbers = in_file.readlines()
    for i in range(0, 2):
        sum_of_numbers += int(numbers[i])
    print(sum_of_numbers)