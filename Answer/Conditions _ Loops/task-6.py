#  reverse right-angled triangle pattern
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()




# center-aligned right-angled triangle 
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    
    for j in range(rows - i):
        print(" ", end="")
    
    
    for k in range(i):
        print("* ", end="")
    
    print()  
