from prettytable import PrettyTable
from grade import Grade


class GradeHolder:
    """Keeps track of the grades for a given course"""

    def __init__(self, name: str) -> None:
        """Initialize a GradeHolder"""
        self.name = name.lower()
        self.grade_table = PrettyTable()
        self.grade_table.field_names = ["Assessment", "Weight", "Grade"]
        self.curr_weight = 0.0
        self.curr_points = 0.0
        # self.str_data = [[self.name]]

    def initialize_from_file(self, file_name: str) -> None:
        """fill in this course from an existing file"""
        grade_file = open(file_name, "r")
        self.name = grade_file.readline().rstrip()
        line = grade_file.readline().rstrip().split(",")
        while line != ['']:
            grade = Grade(line[0], float(line[1]), float(line[2]))
            # add this grade to grade_table.
            self.add_grade(grade)
            line = grade_file.readline().rstrip().split(",")
        grade_file.close()

    def add_grade(self, grade: Grade, write=False) -> None:
        """Add a new grade to this grade holder (grade_table)

        Optional: write this new grade to the data file
        """
        self.grade_table.add_row([grade.assessment_name, grade.weight,
                                  grade.mark])
        # self.str_data.append(
        #     [grade.assessment_name, grade.weight,
        #      grade.mark])
        self.curr_weight += grade.weight
        self.curr_points += grade.point
        if write:
            f = open(f"grades/{self.name}.txt", "a")
            f.write(f"{grade.assessment_name}, {grade.weight}, {grade.mark}\n")
            # f.write(f"{self.str_data[0][0]}\n")
            # # the big-oh on this thing is terrible lol.
            # for line in self.str_data[1:]:
            #     f.write(f"{line[0]}, {line[1]}, {line[2]}\n")
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
