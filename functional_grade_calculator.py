from prettytable import *


def get_grade_summary() -> str:
    """Returns the user's current grade summary"""
    summary = PrettyTable()
    summary.field_names = ["Assessment", "weight", "grade"]
    curr_points = 0.0
    curr_weight = 0.0
    action = ""
    f = open("GradeCalculator/grades.txt", 'r')
    f.readline()
    line = f.readline()
    while line != "":
        line = line.rstrip().split(",")
        assessment = line[0]
        weight = float(line[1])
        grade = float(line[2])
        summary.add_row([assessment, str(weight) + " %", grade])
        curr_points += grade * (weight / 100)
        curr_weight += weight
        line = f.readline()
    # while action != "no":
    #     assessment = input("test/assessment name: ")
    #     weight = float(input("how much is it worth? "))
    #     grade = float(input("what did you get? "))
    #     summary.add_row([assessment, str(weight) + " %", grade])
    #     curr_points += grade * (weight / 100)
    #     curr_weight += weight
    #     print("____________________")
    #     action = input("Add more grades? ").lower().rstrip()
    #     print("____________________")

    if curr_weight == 0.0:
        return ""

    curr_grade = round((curr_points / curr_weight) * 100, 2)
    action = input("Do you want to calculate what you need to get from now to "
                   "get a desired grade?"
                   "\n    yes: calculate what you need from now on to get that "
                   "grade \n    no: just show me the summary\n")
    if action == "no":
        return summary.get_string() + "\n\n current grade: " + str(curr_grade)
    else:
        print("===current grade summary===")
        print(summary.get_string() + "\n\ncurrent grade: " + str(curr_grade))
        print("_______________")
        goal = float(input("what is your desired grade? "))
        print("_______________")

        return f"\nyou need to get " \
               f"{calculate_desired_grade(goal, curr_points, curr_weight)} " \
               f"from now" \
               f" to finish with a {goal} in this course"


def calculate_desired_grade(goal: float,
                            curr_points: float, curr_weight: float) -> str:
    """Returns what the user needs to get from now on to achieve their desired
    grade."""
    ungraded = 100 - curr_weight
    required_grade = (goal - curr_points) / ungraded
    return str(round(required_grade, 2) * 100)


if __name__ == "__main__":
    print(get_grade_summary())
