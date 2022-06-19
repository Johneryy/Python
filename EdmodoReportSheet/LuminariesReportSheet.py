print("""
                *** *** *** *** *** *** *** *** *** *** ***
                         WELCOME TO SEMICOLON SCHOOL
                *** *** *** *** *** *** *** *** *** *** ***  
""")


def student():
    num_of_students = int(input("Enter number of students -> "))
    print()
    num_of_course = int(input("Enter number of courses -> "))
    print()
    list_of_student_names = [input(f"Enter name of student {x + 1}: ") for x in range(num_of_students)]
    print()
    print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ENTER THE STUDENTS SUBJECT SCORES
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    list_of_courses = [input(f"Enter name of subject {y + 1}: ") for y in range(num_of_course)]
    print()
    student_records = []

    for z in range(num_of_students):
        student_records.append([])
        for a in range(num_of_course):
            student_records[z].append(int(input(f"Enter {list_of_student_names[z]}'s "
                                                f"Score for {list_of_courses[a]}: ")))
        print()

    return student_records, list_of_student_names

print(student())
