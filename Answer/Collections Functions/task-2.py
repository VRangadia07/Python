students = {}

n = int(input("Enter number of students: "))

for i in range(1, n + 1):
    key = f's{i}'
    rollno = input(f"Enter roll number for student {i}: ")
    name = input(f"Enter name for student {i}: ")
    marks = float(input(f"Enter marks for student {i}: "))
    
    students[key] = {
        'rollno': rollno,
        'name': name,
        'marks': marks,
        'grade': None
    }

print("\nStudent Dic.:")
print(students)








# for s_id, value in students.items():
#     print(f"{s_id}: Roll No = {value['rollno']}, Name = {value['name']}, Marks = {value['marks']}, Grade = {value['grade']}")
