# Students dictionary
students = {"Ahmed" : 87, "Waleed" : 69, "Hesham" : 92}

# Khaled grades
kh_grades = {"Math": 86, "English": 74}

#1 Add Khaled and his grades to students
students["Khaled"] = kh_grades

# Print out students
print(students)

#2 Print out Khaled grade in English
print(students["Khaled"]["English"])
