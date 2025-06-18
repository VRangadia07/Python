def write_data(n):
    with open("studentinfo.txt", "w") as info_f, open("studentmarks.txt", "w") as mark_f:
        for i in range(n):
            roll_no = input(f"\nEnter Roll Number of student {i + 1}: ")
            name = input(f"Enter Name of student {i + 1}: ")
            info_f.write(f"{roll_no}-{name}\n")
            
            print(f"Enter Marks of 3 Subjects of student {i + 1}: ")
            mark_1 = int(input("subject 1: "))
            mark_2 = int(input("subject 2: "))
            mark_3 = int(input("subject 3: "))
            mark_f.write(f"{roll_no}-{mark_1}-{mark_2}-{mark_3}\n")
            
        