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