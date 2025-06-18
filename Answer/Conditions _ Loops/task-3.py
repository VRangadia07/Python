marks = float(input("Enter marks: "))


if marks > 100:
    print("Invalid Marks")
elif marks >= 90:
    print("A grade")
elif marks >= 80:
    print("B grade")
elif marks >= 60:
    print("C grade")
elif marks >= 40:
    print("D grade")
else:
    print("Fail")
