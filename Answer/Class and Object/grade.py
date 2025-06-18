def calculate_grade(average):
    if 80 <= average <= 100:
        return 'A'
    elif 60 <= average < 80:
        return 'B'
    elif 40 <= average < 60:
        return 'C'
    else:
        return "Fail"
