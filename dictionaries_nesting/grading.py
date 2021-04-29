student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

for key in student_scores:
    score = student_scores[key]
    if score >= 91:
        student_grades[key] = {"Outstanding"}
    elif 81 <= score <= 90:
        student_grades[key] = {"Exceeds Expectations"}
    elif 71 <= score <= 80:
        student_grades[key] = {"Acceptable"}
    else:
        student_grades[key] = {"Fail"}

print(student_grades)
