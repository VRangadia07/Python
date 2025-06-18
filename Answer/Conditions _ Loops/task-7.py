rows = int(input("Enter number of rows: "))

# Upper triangle
for i in range(1, rows + 1):
    
    for j in range(rows - i):
        print(" ", end="")
    
    
    for k in range(i):
        print("* ", end="")
    
    print()

# Lower triangle
for i in range(rows - 1, 0, -1):
    
    for j in range(rows - i):
        print(" ", end="")
    
    
    for k in range(i):
        print("* ", end="")
    
    print()
