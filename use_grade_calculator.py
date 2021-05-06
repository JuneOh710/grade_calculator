from grade_calculator import *
courses = {
    "csc148": Course("csc148"),
    "csc165": Course("csc165")
}

message = "select action:\n" \
          "c: configure course\n"\
          "a: add grade\n"\
          "s: see course status\n"\
          "sa: see all courses\n"

action = input(message)
# this is a comment
if action == "sa":
    for course in courses:
        print(courses[course])
        print("_______________")
else:
    course_name = input("which course? ").lower()

    if action == "c":
        courses[course_name].configure()
    elif action == "a":
        assignment = input("assignment: ")
        grade = float(input("grade: "))
        courses[course_name].add_grade(assignment, grade)
    elif action == "s":
        print(courses[course_name])
    else:
        print("try again")
# this is a useless comment
