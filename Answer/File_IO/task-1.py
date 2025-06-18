no_lines = int(input("Enter number of lines to write into file: "))


with open("task.txt", "w") as f:
    for i in range(no_lines):
        line = input(f"Enter line {i + 1}: ")
        f.write(line + "\n")  

print("\nSuccessfully Written to 'task.txt'.")

print("\nReading data from file:")
with open("task.txt", "r") as f:
    str = f.read()
    print(str)
