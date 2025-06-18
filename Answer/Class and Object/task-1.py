from grade import calculate_grade

class StudentInfo:
    def __init__(self, student_roll_no, student_name):
        self.student_roll_no = student_roll_no
        self.student_name = student_name
        
        
class StudentMarks:
    def __init__(self, student_roll_no, m1, m2, m3):
        self.roll_no = student_roll_no
        self.mark1 = m1
        self.mark2 = m2
        self.mark3 = m3
        
    def average(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3
        
        
        
        
        
        
class Main:
    def __init__(self):
        self.student_info = []
        self.student_marks = []
        self.num_student = int(input("Enter Numbers of Students: "))
        self.get_std_data()
        self.get_results()
        
    def get_std_data(self):
        for i in range(self.num_student):
            print(f"\nStudent {i + 1}")
            roll_no = int(input("Enter Roll Number: "))
            name = input("Enter Name of Student: ")
            self.student_info.append(StudentInfo(roll_no, name))
            
            print("Enter Marks for 3 Subjects: ")
            m1 = int(input("Enter Mark 1: "))
            m2 = int(input("Enter Mark 2: "))
            m3 = int(input("Enter Mark 3: "))
            self.student_marks.append(StudentMarks(roll_no, m1, m2, m3))
            
            
    def get_results(self):
        print("\nStudents Results: ")
        for i in range(len(self.student_info)):
            info = self.student_info[i]
            marks = self.student_marks[i]
            avg = marks.average()
            grade = calculate_grade(avg)
            print(f"{info.student_roll_no}-{info.student_name} Marks of Average: {avg:.2f}, Grade: {grade}")
            
            

if __name__ == "__main__":
    Main()
    
    
            
            
        
            
            
            
            
        
        