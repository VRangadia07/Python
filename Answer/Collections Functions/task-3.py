students = {}

n = int(input("Enter number of students: "))

for i in range(1, n + 1):
    key = 's' + str(i)

    rollno = input(f"Enter roll number for student {i}: ")
    name = input(f"Enter name for student {i}: ")
    marks = float(input(f"Enter marks for student {i}: "))


    if 90 <= marks <= 100:
        grade = 'A'
    elif 80 <= marks < 90:
        grade = 'B'
    elif 60 <= marks < 80:
        grade = 'C'
    elif 40 <= marks < 60:
        grade = 'D'
    elif marks < 40:
        grade = 'Fail'
    else:
        grade = 'Invalid'  

    
    students[key] = {
        'rollno': rollno,
        'name': name,
        'marks': marks,
        'grade': grade
    }


print("\nStudent Dic.")
print(students)





























# for s_id, value in students.items():
#     print(f"{s_id}: Roll No = {value['rollno']}, Name = {value['name']}, Marks = {value['marks']}, Grade = {value['grade']}")
