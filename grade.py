class Grade:
    """Grade class"""
    mark: float
    assessment_name: str
    point: float
    weight: float

    def __init__(self, name_p: str, weight_p: float, mark_p: float) -> None:
        """Initialize a new grade object"""
        self.assessment_name = name_p
        self.mark = mark_p
        self.point = mark_p * (weight_p / 100)
        self.weight = weight_p


