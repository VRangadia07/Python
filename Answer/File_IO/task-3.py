no_lines = int(input("Enter number of lines to write into file: "))


with open("demo.txt", "w") as f:
    for i in range(no_lines):
        line = input(f"Enter line {i + 1}: ")
        f.write(line + "\n")  

print("\nSuccessfully Written to 'demo.txt'.")


with open("demo.txt", "r") as f:
    lines = f.readlines()
    
print("\nRead data to file demo.txt:")
for line in lines:
    print(line.strip())
    
reverse_lines = lines[::-1]

with open("dummy.txt",  "w") as f:
    f.writelines(reverse_lines)
    
print("\nReversed data write to dummy.txt:")