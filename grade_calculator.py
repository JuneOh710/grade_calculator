import json
from typing import *


class CourseManager:
    def __init__(self) -> None:
        pass


class Course:
    """A university course"""
    _assessments: Dict[str, List[Any]]

    def __init__(self, name: str) -> None:
        """Initialize a Course object with its _assessments"""
        self.name = name
        self._assessments = {}
        self.configured = False

    def configure(self) -> None:
        """configures a new course"""
        weight = 0
        while weight < 100:
            ass_name = input("Assessment name: ").rstrip()
            ass_weight = \
                float(input("Assessment weight: ").rstrip())
            ass_count = int(input("How many parts does it consist? "))
            ass_grade = 0
            self._assessments[ass_name] = [ass_weight, ass_count, ass_grade]
            weight += ass_weight
            print("____________________")
            print(f"we currently got {weight}% of the course configured")
            print("____________________")
        if weight != 100:
            print("failed")
        with open(f"{self.name}.json", "w") as outfile:
            json.dump(self._assessments, outfile)
        self.configured = True

    def add_grade(self, ass_name: str, ass_grade: float) -> None:
        """Adds the grade of <ass_name>"""
        self._assessments[ass_name][2] = ass_grade
        with open(f"{self.name}.json", "w") as outfile:
            json.dump(self._assessments, outfile)
