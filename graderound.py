def gradingStudents(grades):
    for x, i in enumerate(grades):
        if(i >= 38) and (i % 5) >= 3:
            grades[x] = i+5-(i % 5)
    return grades


grades = [78, 96, 45, 38, 41]
result = gradingStudents(grades)
print(result)
