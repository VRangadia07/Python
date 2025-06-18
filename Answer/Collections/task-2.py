student = {}

n = int(input("Enter number of students: "))

for i in range(n):
    
    name = input("Enter name: ")
    roll_no = input("Enter roll number: ")
    marks = float(input("Enter marks: "))

    student[name] = {"roll_no": roll_no, "marks": marks}

print("\nStudent Dict:")
print(student)















# for name, value in student.items():
#     print(f"Name: {name}, Roll No: {value['roll_no']}, Marks: {value['marks']}")
