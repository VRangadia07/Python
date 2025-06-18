def calculate(n):
    students = []
    
    for i in range(n):
        roll_no = input(f"\nEnter Roll number of student {i + 1}: ")
        name = input(f"Enter Name of student {i + 1}: ")
        marks = []
        for j in range(3):
            mark = float(input(f"Enter mark {j + 1} for student {i + 1}: "))
            marks.append(mark)
        avg = sum(marks) / 3
        students.append((roll_no, name, avg))
        
    
    students.sort(key=lambda x: x[2], reverse=True)
    
    
    with open("Agrade.txt", "w") as fa, \
         open("Bgrade.txt", "w") as fb, \
         open("Cgrade.txt", "w") as fc:
             
        for roll_no, name, avg in students:
            line = f"{roll_no}-{name}-{avg:.2f}\n"
            if 80 <= avg <= 100:
                fa.write(line)
            elif 60 <= avg <= 80:
                fb.write(line)
            elif 40 <= avg < 60:
                fc.write(line)

    
   
            
        
    