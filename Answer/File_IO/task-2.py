no_lines = int(input("Enter number of lines to write into file: "))


with open("task0.txt", "w") as f:
    for i in range(no_lines):
        line = input(f"Enter line {i + 1}: ")
        f.write(line + "\n")  

print("\nSuccessfully Written to 'task0.txt'.")

with open("task0.txt", "r") as f:
    lines = f.readlines()
 
print("\nRead data to file:")   
for line in lines:
    print(line, end='')
    
line_count = len(lines)
word_count = 0
chr_space = 0
chr_without_s = 0

for line in lines:
    word_count += len(line.split())
    chr_space += len(line)
    chr_without_s += len(line.replace(" ", "").replace("\n", ""))
    
print("\nCount lines:", line_count)
print("Count words:", word_count)
print("Count Chars_with_space:", chr_space)
print("Count Char_without_space:", chr_without_s)

