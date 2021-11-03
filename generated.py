def ignore_letter_prefix(a_student_number):
    return int(a_student_number[1:])

students = ["A0100", "A0050", "A0075"]
sorted_students = sorted(students, key=ignore_letter_prefix)
print(sorted_students)


