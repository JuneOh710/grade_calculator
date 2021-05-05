from __future__ import annotations
from prettytable import PrettyTable
from typing import *


class GradeHolder:
    """Keeps track of the grades for a given course"""

    def __init__(self, name: str) -> None:
        """Initialize a GradeHolder"""
        self.name = name.lower()
        self.grade_table = PrettyTable()
        self.grade_table.field_names = ["Assessment", "Weight", "Grade"]
        self.curr_weight = 0.0
        self.curr_points = 0.0
        self.str_data = [[self.name]]

    def add_grade(self, grade: Grade) -> None:
        """Add a new grade to this grade holder"""
        if grade.mark == -1:
            return None
        self.grade_table.add_row([grade.assessment_name, grade.weight,
                                  grade.mark])
        self.str_data.append(
            [grade.assessment_name, grade.weight,
             grade.mark])
        self.curr_weight += grade.weight
        self.curr_points += grade.point
        f = open(f"{self.name}.txt", "w")
        f.write(f"{self.str_data[0][0]}\n")
        # the big-oh on this thing is terrible lol.
        for line in self.str_data[1:]:
            f.write(f"{line[0]}, {line[1]}, {line[2]}\n")
        f.close()

    def get_current_grade(self) -> str:
        """Returns the user's current grade"""
        curr_grade = round(100 * self.curr_points / self.curr_weight, 2)
        return f"current grade: {curr_grade}"

    def __str__(self) -> str:
        """String representation of a grade holder"""
        return self.grade_table.get_string() + "\n" + self.get_current_grade()

    def calculate_required_grade(self, grade: float) -> str:
        """Returns what the user needs on the final to achieve the desired grade
        """
        ungraded = 100 - self.curr_weight
        required_grade = (grade - self.curr_points) / ungraded
        return f"you need {str(round(required_grade, 2) * 100)}"


class Grade:
    """Grade class"""

    def __init__(self, name_p: str, weight_p: float, mark_p: float) -> None:
        """Initialize a new grade object"""
        self.assessment_name = name_p
        self.mark = mark_p
        self.point = mark_p * (weight_p / 100)
        self.weight = weight_p


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
