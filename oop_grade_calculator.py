from __future__ import annotations
from typing import *
from GradeHolder import GradeHolder
from grade import Grade


def initialize_from_file(file: TextIO) -> GradeHolder:
    """Initialize and return a GradeHolder object from the given file"""
    holder = GradeHolder(file.readline().rstrip())
    line = file.readline().rstrip().split(",")
    while line != ['']:
        grade = Grade(line[0], float(line[1]), float(line[2]))
        holder.add_grade(grade)
        line = file.readline().rstrip().split(",")
    return holder


if __name__ == "__main__":
    course_name = input("which course? ").lower().rstrip()
    grade_holder = GradeHolder(course_name)

    initialize = True
    while initialize:
        action = input("would you like use the data from "
                       "an existing file? (yes, no)\n").lower().rstrip()
        if action == "yes":
            f = open(f"{course_name}.txt", "r")
            grade_holder = initialize_from_file(f)
            initialize = False
        elif action == "no":
            initialize = False
        else:
            pass

    is_on = True
    while is_on:
        print("============")
        action = input("a: add new grade \ns: see current grade\nc: calculate "
                       "what you need on the final\nPress any other key to "
                       "end the program\n").lower().rstrip()
        print("============")

        if action == "a":
            name = input("name of assessment: ")
            weight = float(input("weight of assessment: "))
            mark = float(input("Grade you got: "))
            new_grade = Grade(name, weight, mark)
            grade_holder.add_grade(new_grade)
        elif action == "s":
            print(grade_holder)
        elif action == "c":
            goal = float(input("what is your goal? "))
            print(grade_holder.calculate_required_grade(goal))

        else:
            is_on = False
